start python -m rasa_core_sdk.endpoint --actions actions
start rasa run -m models --enable-api --cors "*" --debug
start python api_python_functions.py