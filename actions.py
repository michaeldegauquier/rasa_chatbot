# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
import requests
import os
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello World!")

        return []


# reset of insurance data without the name of the person (user)
def overwrite_insurance():
    with open('database/clean_person_data.json', 'r') as file:
        data = json.load(file)

    with open('database/person_data.json', 'r') as file1:
        data1 = json.load(file1)

    data['person']['person_name'] = data1['person']['person_name']
    os.remove('database/person_data.json')

    with open('database/person_data.json', 'w') as file:
        json.dump(data, file, indent=4)


# write insurance data to the file
def write_insurance(intent, entity_name, entity_value):
    with open('database/person_data.json', 'r') as file:
        data = json.load(file)
        data[intent][entity_name] = entity_value

    os.remove('database/person_data.json')

    with open('database/person_data.json', 'w') as file:
        json.dump(data, file, indent=4)


# checking the data of the insurance that is not filled in
def check_insurance(intent, entity_name):
    with open('database/person_data.json', 'r') as file:
        data = json.load(file)
        if data[intent][entity_name] == "":
            return 0
        else:
            return 1


# full reset of the insurance data
def reset_insurance():
    with open('database/clean_person_data.json', 'r') as file:
        data = json.load(file)

    os.remove('database/person_data.json')

    with open('database/person_data.json', 'w') as file:
        json.dump(data, file, indent=4)


# get the sentiment (percentage) of the user his input
def sentiment_analysis(text):
    url = 'https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment'

    body = {
        "documents": [
            {
                "language": "en",
                "id": "1",
                "text": text
            }
        ]
    }

    api_key = open('secret_env.txt').readlines()[0].split(':')[1].strip()

    headers = {'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': api_key}

    r = requests.post(url, data=json.dumps(body), headers=headers)
    data = r.json()
    sentiment = data['documents'][0]['score']
    print(sentiment)

    return sentiment


# this makes a choice which character trait it has to take based on the sentiment
def choice_character_trait(character_traits_dict, text):
    array_size = len(character_traits_dict)

    if array_size == 1:
        return list(character_traits_dict.keys())[0]
    elif array_size > 1:
        sentiment = sentiment_analysis(text)

        if 'aggressive' in character_traits_dict and ((0 <= sentiment <= 0.017) or (0.019 <= sentiment <= 0.060)):
            print('aggressive')
            return 'aggressive'
        else:
            closest_key, closest_value = min(character_traits_dict.items(), key=lambda x: abs(sentiment - x[1]))
            print(closest_key)
            return closest_key


# it filters the character trait list and returns a dictionary with the right character traits
def filter_list(character_traits):
    character_traits_dict = {"friendly": 0.6, "happy": 0.9, "aggressive": -10, "rude": 0.0, "lazy": 0.3, "pushy": 0.4}
    new_dict = {}

    for key in character_traits_dict.keys():
        for character_trait in character_traits:
            if key == character_trait:
                new_dict[key] = character_traits_dict[key]
    return new_dict


# function to store data about the car insurance
# the chatbot knows with this function which questions it has to ask to the user about the car insurance
class ActionGetCarDataPerson(Action):

    def name(self):
        return "action_get_car_data_person"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        user_text = tracker.latest_message['text']
        print(user_text)

        with open('database/character_traits') as some_file:
            character_traits = some_file.read().split(",")

        character_traits_dict = filter_list(character_traits)
        print(character_traits_dict)
        character_trait = choice_character_trait(character_traits_dict, user_text)

        random_response = random.randint(0, 1)
        print(random_response)

        if intent is not None:
            with open('responses/responses.json') as json_file:
                data = json.load(json_file)

        if check_insurance("person", "person_name") == 0:
            person_name = next(tracker.get_latest_entity_values('person_name'), None)
            if person_name is not None:
                write_insurance("person", "person_name", person_name)
            else:
                dispatcher.utter_message(f"{data['ask_person_name'][character_trait][random_response]}")

        elif check_insurance("car_insurance", "new_car") == 0:
            new_car = next(tracker.get_latest_entity_values('new_car'), None)
            if new_car is not None:
                write_insurance("car_insurance", "new_car", new_car)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_new_car'][character_trait][random_response]}")

        elif check_insurance("car_insurance", "car_type") == 0:
            car_type = next(tracker.get_latest_entity_values('car_type'), None)
            if car_type is not None:
                write_insurance("car_insurance", "car_type", car_type)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_car_type'][character_trait][random_response]}")

        elif check_insurance("car_insurance", "year_car") == 0:
            year_car = next(tracker.get_latest_entity_values('year'), None)
            if year_car is not None:
                write_insurance("car_insurance", "year_car", year_car)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_year_car'][character_trait][random_response]}")

        elif check_insurance("car_insurance", "type_fuel") == 0:
            type_fuel = next(tracker.get_latest_entity_values('type_fuel'), None)
            if type_fuel is not None:
                write_insurance("car_insurance", "type_fuel", type_fuel)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_type_fuel'][character_trait][random_response]}")

        elif check_insurance("car_insurance", "closed") == 0:
            write_insurance("car_insurance", "closed", "true")
            dispatcher.utter_message(f"{data['another_questions'][character_trait][random_response]}")

        elif check_insurance("car_insurance", "closed") == 1:
            overwrite_insurance()

        return []


class ActionGetFireDataPerson(Action):

    def name(self):
        return "action_get_fire_data_person"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        user_text = tracker.latest_message['text']
        print(user_text)

        with open('database/character_traits') as some_file:
            character_traits = some_file.read().split(",")

        character_traits_dict = filter_list(character_traits)
        print(character_traits_dict)
        character_trait = choice_character_trait(character_traits_dict, user_text)

        random_response = random.randint(0, 1)
        print(random_response)

        if intent is not None:
            with open('responses/responses.json') as json_file:
                data = json.load(json_file)

        if check_insurance("person", "person_name") == 0:
            person_name = next(tracker.get_latest_entity_values('person_name'), None)
            if person_name is not None:
                write_insurance("person", "person_name", person_name)
            else:
                dispatcher.utter_message(f"{data['ask_person_name'][character_trait][random_response]}")

        elif check_insurance("fire_insurance", "type_building") == 0:
            type_building = next(tracker.get_latest_entity_values('type_building'), None)
            if type_building is not None:
                write_insurance("fire_insurance", "type_building", type_building)
            else:
                dispatcher.utter_message(
                    f"{data['ask_fire_insurance_type_building'][character_trait][random_response]}")

        elif check_insurance("fire_insurance", "construction_year") == 0:
            construction_year = next(tracker.get_latest_entity_values('year'), None)
            if construction_year is not None:
                write_insurance("fire_insurance", "construction_year", construction_year)
            else:
                dispatcher.utter_message(
                    f"{data['ask_fire_insurance_construction_year'][character_trait][random_response]}")

        elif check_insurance("fire_insurance", "construction_home") == 0:
            construction_home = next(tracker.get_latest_entity_values('construction_home'), None)
            if construction_home is not None:
                write_insurance("fire_insurance", "construction_home", construction_home)
            else:
                dispatcher.utter_message(
                    f"{data['ask_fire_insurance_construction_home'][character_trait][random_response]}")

        elif check_insurance("fire_insurance", "business_home") == 0:
            business_home = next(tracker.get_latest_entity_values('business_home'), None)
            if business_home is not None:
                write_insurance("fire_insurance", "business_home", business_home)
            else:
                dispatcher.utter_message(
                    f"{data['ask_fire_insurance_business_home'][character_trait][random_response]}")

        elif check_insurance("fire_insurance", "closed") == 0:
            write_insurance("fire_insurance", "closed", "true")
            dispatcher.utter_message(f"{data['another_questions'][character_trait][random_response]}")

        elif check_insurance("fire_insurance", "closed") == 1:
            overwrite_insurance()

        return []


# chatbot returns a response to the user based on the incoming intent
class ActionGetIntent(Action):

    def name(self):
        return "action_get_intent"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        user_text = tracker.latest_message['text']

        print(user_text)

        with open('database/character_traits') as some_file:
            character_traits = some_file.read().split(",")

        # character_traits = ["friendly", "happy"]
        character_traits_dict = filter_list(character_traits)
        print(character_traits_dict)

        random_response = random.randint(0, 1)
        print(random_response)

        if intent is not None:
            character_trait = choice_character_trait(character_traits_dict, user_text)

            with open('responses/responses.json') as json_file:
                data = json.load(json_file)

            if intent == "goodbye":
                reset_insurance()

            dispatcher.utter_message("{}".format(data[intent][character_trait][random_response]))
        else:
            dispatcher.utter_message("I don't know what you are talking about.")

        return []


class ActionAnotherQuestion(Action):

    def name(self):
        return "action_another_question"

    def run(self, dispatcher, tracker, domain):
        with open('database/character_traits') as some_file:
            character_traits = some_file.read().split(",")

        user_text = tracker.latest_message['text']
        print(user_text)

        character_traits_dict = filter_list(character_traits)
        print(character_traits_dict)
        character_trait = choice_character_trait(character_traits_dict, user_text)

        random_response = random.randint(0, 1)
        print(random_response)

        with open('responses/responses.json') as json_file:
            data = json.load(json_file)

        dispatcher.utter_message("{}".format(data['another_questions'][character_trait][random_response]))

        return []


class ActionWrongAnswer(Action):

    def name(self):
        return "action_wrong_answer"

    def run(self, dispatcher, tracker, domain):
        with open('database/character_traits') as some_file:
            character_traits = some_file.read().split(",")

        user_text = tracker.latest_message['text']
        print(user_text)

        character_traits_dict = filter_list(character_traits)
        print(character_traits_dict)
        character_trait = choice_character_trait(character_traits_dict, user_text)

        random_response = random.randint(0, 1)
        print(random_response)

        with open('responses/responses.json') as json_file:
            data = json.load(json_file)

        dispatcher.utter_message(f"{data['wrong_answer'][character_trait][random_response]}")

        return []


class ActionNoInformation(Action):

    def name(self):
        return "action_no_information"

    def run(self, dispatcher, tracker, domain):
        with open('database/character_traits') as some_file:
            character_traits = some_file.read().split(",")

        user_text = tracker.latest_message['text']
        print(user_text)

        character_traits_dict = filter_list(character_traits)
        print(character_traits_dict)
        character_trait = choice_character_trait(character_traits_dict, user_text)

        random_response = random.randint(0, 1)
        print(random_response)

        with open('responses/responses.json') as json_file:
            data = json.load(json_file)

        dispatcher.utter_message(f"{data['no_information'][character_trait][random_response]}")

        return []

# Rasa. Actions. Geraadpleegd via
# https://rasa.com/docs/rasa/1.0.9/core/actions/
# Geraadpleegd op 18 januari 2020

# Extracting the current intent from a custom action. Geraadpleegd via
# https://forum.rasa.com/t/solved-extracting-the-current-intent-from-a-custom-action/1446
# Geraadpleegd op 22 februari 2020
