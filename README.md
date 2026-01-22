Weather Checker Application

What is this project?
This project is a small web application written in Python using Streamlit.
It allows a user to enter a city name and see the current temperature, humidity,
and simple visualizations of the weather.

Why does this project exist?
This project was built as part of a Python course to practice REST API calls,
working with JSON data, building a simple web UI, and visualizing data.

Which file should be executed?
The main file to run is main.py.

Streamlit public app
This app will be deployed to Streamlit Cloud.
The public link: https://weatherchecker-n3fbtbypv92ryrgufaporc.streamlit.app/

Why is secrets.toml used?
The OpenWeatherMap API requires an API key.
This key is private and must not be uploaded to GitHub.
For this reason, the API key is stored in a secrets.toml file.

How to run the project locally

Requirements:
- Python 3.10 or higher
- Poetry installed

Step 1: Install dependencies
Run the following command in the terminal:
poetry install

Step 2: Add your OpenWeatherMap API key
Create a file called .streamlit/secrets.toml inside the project folder.
Inside that file, add the following line:
api_key = "YOUR_OPENWEATHERMAP_API_KEY"

Step 3: Run the app
Run the following command in the terminal:
poetry run streamlit run main.py

Open a browser and go to:
http://localhost:8501
