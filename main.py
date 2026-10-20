import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    if not API_KEY:
        print("API key not found.")
        print("Please configure OPENWEATHER_API_KEY first.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 404:
            print("City not found. Please check the spelling.")
            return

        response.raise_for_status()
        data = response.json()

        weather = data["weather"][0]
        details = data["main"]

        print("\n========== WEATHER REPORT ==========")
        print(f"City: {data['name']}")
        print(f"Country: {data['sys']['country']}")
        print(f"Condition: {weather['description'].title()}")
        print(f"Temperature: {details['temp']} °C")
        print(f"Feels Like: {details['feels_like']} °C")
        print(f"Humidity: {details['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print("====================================")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Network error. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print(f"Weather API error: {error}")

    except (KeyError, IndexError, ValueError):
        print("Unable to process the weather information.")


def main():
    print("===== WEATHER APPLICATION =====")

    while True:
        city = input(
            "\nEnter a city name (or 'exit' to quit): "
        ).strip()

        if city.lower() == "exit":
            print("Thank you for using Weather Application!")
            break

        if not city:
            print("City name cannot be empty.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()