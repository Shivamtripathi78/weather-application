# 🌦️ Weather Application

A Python application that retrieves current weather information for cities using the OpenWeather API.

## ✨ Features

- Search weather by city name
- Display temperature in Celsius
- Show feels-like temperature
- Display humidity and wind speed
- Show current weather conditions
- Handle invalid city names
- Handle network errors and API failures
- Keep API credentials outside the source code

## 🛠️ Technologies Used

- Python
- Requests
- REST API
- JSON
- Environment variables
- Exception handling

## 🚀 Getting Started

### Prerequisites

- Python 3
- An OpenWeather API key

### Installation

Clone the repository:

```bash
git clone https://github.com/Shivamtripathi78/weather-application.git
```

Navigate to the project folder:

```bash
cd weather-application
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Configure the API Key

In PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY_HERE"
```

Replace the placeholder with your actual API key.

### Run the Application

```bash
python main.py
```

Enter a city name to view its current weather.

## 🔒 Security

The application reads the API key from an environment variable.

Never commit API keys or credentials to GitHub.

## 🎯 Learning Outcomes

- Calling REST APIs
- Processing JSON responses
- Managing environment variables
- Exception handling
- Working with external services

## 🔮 Future Improvements

- Add a graphical user interface
- Display weather forecasts
- Support temperature unit selection
- Add weather icons
- Save recent city searches

## 👨‍💻 Author

Shivam Tripathi

GitHub: [@Shivamtripathi78](https://github.com/Shivamtripathi78)
