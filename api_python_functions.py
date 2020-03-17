# main.py
from flask import Flask
from flask import url_for, jsonify, render_template, Response
import json
import os
import requests
import sys

app = Flask(__name__)

# this api is for running python functions via JavaScript
@app.route('/reset_bot')
def index():
    try:
        url = 'https://wcl0c5rsb4.execute-api.us-east-1.amazonaws.com/deployct/character-trait'

        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        data = r.json()
        character_traits_list = data['Items'][0]['character_traits']

        with open('./database/character_traits', 'w') as file:
            file.write("")

        with open('./database/character_traits', 'a') as file:
            for c in character_traits_list:
                if len(character_traits_list) == 1:
                    file.write(c)
                else:
                    file.write(c + ",")

        with open('./database/clean_person_data.json', 'r') as file:
            data = json.load(file)

        os.remove('./database/person_data.json')

        with open('./database/person_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        response = jsonify({"message": "Chatbot has been reset!"})
        response.headers.add('Access-Control-Allow-Origin', '*')
    except:
        response = jsonify({"message": "Reset chatbot failed"})
        response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/test', methods=['GET'])
def character_traits():
    response = jsonify({"message": "test"})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    app.run(port=8080, debug=True)

# Reddit. Execute a python script on button click? Geraadpleegd via
# https://www.reddit.com/r/learnpython/comments/9xyozb/execute_a_python_script_on_button_click/
# Geraadpleegd op 14 maart 2020
