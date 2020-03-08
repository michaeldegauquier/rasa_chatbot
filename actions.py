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


def overwrite_car_insurance():
    with open('database/clean_person_data.json', 'r') as file:
        data = json.load(file)

    with open('database/person_data.json', 'r') as file1:
        data1 = json.load(file1)

    data['person']['person_name'] = data1['person']['person_name']
    os.remove('database/person_data.json')

    with open('database/person_data.json', 'w') as file:
        json.dump(data, file, indent=4)


def write_car_insurance(intent, entity_name, entity_value):
    with open('database/person_data.json', 'r') as file:
        data = json.load(file)
        data[intent][entity_name] = entity_value

    os.remove('database/person_data.json')

    with open('database/person_data.json', 'w') as file:
        json.dump(data, file, indent=4)


def check_car_insurance(intent, entity_name):
    with open('database/person_data.json', 'r') as file:
        data = json.load(file)
        if data[intent][entity_name] == "":
            return 0
        else:
            return 1


def reset_car_insurance():
    with open('database/clean_person_data.json', 'r') as file:
        data = json.load(file)

    os.remove('database/person_data.json')

    with open('database/person_data.json', 'w') as file:
        json.dump(data, file, indent=4)


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

    headers = {'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': 'dc75b701d8574555849d6235161a32d7'}

    r = requests.post(url, data=json.dumps(body), headers=headers)
    data = r.json()
    sentiment = data['documents'][0]['score']
    print(sentiment)

    return sentiment


def choice_character_trait(character_traits_dict, text):
    array_size = len(character_traits_dict)
    sentiment = sentiment_analysis(text)

    if array_size == 1:
        print(list(character_traits_dict.keys())[0])
    elif array_size > 1:
        if 'aggressive' in character_traits_dict and (0 <= sentiment <= 0.017) or (0.019 <= sentiment <= 0.060):
            print('aggressive')
            return 'aggressive'
        else:
            closest_key, closest_value = min(character_traits_dict.items(), key=lambda x: abs(sentiment - x[1]))
            print(closest_key)
            return closest_key


def filter_list(character_traits):
    character_traits_dict = {"friendly": 0.6, "happy": 0.9, "aggressive": -10}
    new_dict = {}

    for key in character_traits_dict.keys():
        for character_trait in character_traits:
            if key == character_trait:
                new_dict[key] = character_traits_dict[key]
    return new_dict


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

        if intent is not None:
            with open('responses/responses.json') as json_file:
                data = json.load(json_file)

        if check_car_insurance("person", "person_name") == 0:
            person_name = next(tracker.get_latest_entity_values('person_name'), None)
            if person_name is not None:
                write_car_insurance("person", "person_name", person_name)
            else:
                dispatcher.utter_message(f"{data['ask_person_name'][character_trait][0]}")

        elif check_car_insurance("car_insurance", "new_car") == 0:
            new_car = next(tracker.get_latest_entity_values('new_car'), None)
            if new_car is not None:
                write_car_insurance("car_insurance", "new_car", new_car)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_new_car'][character_trait][0]}")

        elif check_car_insurance("car_insurance", "car_type") == 0:
            car_type = next(tracker.get_latest_entity_values('car_type'), None)
            if car_type is not None:
                write_car_insurance("car_insurance", "car_type", car_type)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_car_type'][character_trait][0]}")

        elif check_car_insurance("car_insurance", "year_car") == 0:
            year_car = next(tracker.get_latest_entity_values('year_car'), None)
            if year_car is not None:
                write_car_insurance("car_insurance", "year_car", year_car)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_year_car'][character_trait][0]}")

        elif check_car_insurance("car_insurance", "type_fuel") == 0:
            type_fuel = next(tracker.get_latest_entity_values('type_fuel'), None)
            if type_fuel is not None:
                write_car_insurance("car_insurance", "type_fuel", type_fuel)
            else:
                dispatcher.utter_message(
                    f"{data['ask_car_insurance_type_fuel'][character_trait][0]}")
        elif check_car_insurance("car_insurance", "closed") == 0:
            write_car_insurance("car_insurance", "closed", "true")
            dispatcher.utter_message(f"{data['another_questions'][character_trait][0]}")

        elif check_car_insurance("car_insurance", "closed") == 1:
            overwrite_car_insurance()

        return []


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

        # random_character_trait = randint(0, len(character_traits) - 1)
        # print(random_character_trait)

        if intent is not None:
            character_trait = choice_character_trait(character_traits_dict, user_text)

            with open('responses/responses.json') as json_file:
                data = json.load(json_file)

            if intent == "goodbye":
                reset_car_insurance()

            dispatcher.utter_message("{}".format(data[intent][character_trait][0]))
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

        with open('responses/responses.json') as json_file:
            data = json.load(json_file)

        dispatcher.utter_message("{}".format(data['another_questions'][character_trait][0]))

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

        with open('responses/responses.json') as json_file:
            data = json.load(json_file)

        dispatcher.utter_message(f"{data['wrong_answer'][character_trait][0]}")

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

        with open('responses/responses.json') as json_file:
            data = json.load(json_file)

        dispatcher.utter_message(f"{data['no_information'][character_trait][0]}")

        return []