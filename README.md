# `TE-Assignment`
Is a Flask web based API project. To process payment using external gateways.

### How to run the project
Run the following command to do so:
1. Clone the project from git on your system
2. cd `TE-Assignment`
3. Create a virtual environment and activate it
4. Install the site packages by command `pip install requirements.txt` 
5. Create an env variable named `Environment` = `development` or `production`
6. Run the command in the terminal `python app_main.py` to start the app
7. Import the post collection `TE-postman_collection` in the post to make APi call.

### How to run tests
1. Start the flask server
2. Open a separate terminal and execute ` python app/tests/test.py`