import pytest
from app import app, get_weather

# Test client for Flask app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Unit tests for the function
def test_get_weather():
    assert get_weather("london") == {"temp": 15, "condition": "cloudy"}
    assert get_weather("paris") == {"temp": 20, "condition": "sunny"}
    assert get_weather("unknown") == {"error": "City not found"}

# Integration tests for API endpoints
def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Weather API is running!" in response.data

def test_weather_endpoint_success(client):
    response = client.get('/weather/london')
    assert response.status_code == 200
    assert b"london" in response.data
    assert b"temp" in response.data

def test_weather_endpoint_not_found(client):
    response = client.get('/weather/unknown')
    assert response.status_code == 200
    assert b"error" in response.data