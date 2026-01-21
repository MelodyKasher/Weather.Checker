import requests
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Weather App 🌦️")

city = st.text_input("Enter a city (e.g., Tel Aviv, London):", value="Tel Aviv")
fetch = st.button("Fetch weather")

api_key = st.secrets["api_key"]

if fetch:
    city = city.title()

    # CURRENT WEATHER
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        st.subheader(f"{data['name']}, {data['sys']['country']}")
        st.write("Temperature (°C):", data["main"]["temp"])

        # PLOTLY (CURRENT SNAPSHOT)
        df = {
            "Metric": ["Temp (°C)", "Humidity (%)"],
            "Value": [data["main"]["temp"], data["main"]["humidity"]]
        }
        fig = px.bar(df, x="Metric", y="Value", title="Current weather metrics")
        st.plotly_chart(fig, use_container_width=True)

        # MATPLOTLIB (FORECAST LINE)
        forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
        forecast_params = {"q": city, "appid": api_key, "units": "metric"}

        forecast_response = requests.get(forecast_url, params=forecast_params)
        forecast_data = forecast_response.json()

        if forecast_response.status_code != 200:
            st.warning("Could not load forecast data.")
        else:
            times = [item["dt_txt"][11:16] for item in forecast_data["list"][:8]]
            temps = [item["main"]["temp"] for item in forecast_data["list"][:8]]

            fig, ax = plt.subplots()
            ax.plot(times, temps, marker="o")
            ax.set_title("Forecast temperature (next ~24h)")
            ax.set_xlabel("Time")
            ax.set_ylabel("°C")
            ax.tick_params(axis="x", rotation=45)
            st.pyplot(fig)

    elif response.status_code == 404:
        st.error(f"City '{city}' not found. Please check the spelling.")
    else:
        st.error(data.get("message", "An error occurred"))
