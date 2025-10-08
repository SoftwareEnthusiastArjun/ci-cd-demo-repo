from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

def get_weather(city):
    """Get weather data for a city (mock version)"""
    # In real app, this would call a weather API
    weather_data = {
        "london": {"temp": 15, "condition": "cloudy"},
        "paris": {"temp": 20, "condition": "sunny"},
        "tokyo": {"temp": 25, "condition": "rainy"}
    }
    return weather_data.get(city.lower(), {"error": "City not found"})

@app.route('/weather/<city>')
def weather_endpoint(city):
    """API endpoint to get weather for a city"""
    weather = get_weather(city)
    return jsonify({"city": city, **weather})

@app.route('/')
def home():
    return jsonify({"message": "Weather API is running!"})

if __name__ == '__main__':
    app.run(debug=True)