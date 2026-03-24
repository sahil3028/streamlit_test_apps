# 🌦️ Weather Dashboard (Streamlit App)

A simple and interactive weather forecasting web app built using Streamlit, Plotly, and the OpenWeather API.

## 🚀 Features

-> Get weather forecast for any city
-> Select forecast range (1 to 5 days)
-> Visualize temperature trends using interactive charts
-> View sky/weather conditions using icons
-> Clean and interactive UI

## 🛠️ Tech Stack

-> Python
-> Streamlit
-> Plotly
-> OpenWeather API
-> python-dotenv

## 📂 Project Structure

weather_dashboard/
│
├── image/
├── .env
├── backend.py
├── main.py
└── README.md

## 🔑 Setup Instructions

1. Clone the repository
   git clone <your-repo-link>
   cd weather_dashboard

2. Install dependencies
   pip install streamlit plotly requests python-dotenv

3. Add API key
   Create a `.env` file in the root folder and add:
   API=your_openweather_api_key

Get your API key from: https://openweathermap.org/api

4. Run the app
   streamlit run main.py

## 📊 Usage

-> Enter a city name
-> Select number of forecast days
-> Choose data type (temperature or sky)

## ⚠️ Notes

-> Invalid city names will return an error
-> Requires internet connection
-> API usage is limited on free tier

## 📸 Screenshots

See this on Linkedin:
<a href="https://www.linkedin.com/posts/sahil-sah-130280355_python-streamlit-datavisualization-activity-7442079792205828096-OBmQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFh-sLQBxkOkulZQNwte5C_OvJo6k5oqKk4">LinkedIN</a>
## 💡 Future Improvements

-> Add caching for API calls
-> Improve UI with custom CSS
-> Add more weather metrics (humidity, wind speed)
-> Deploy online (Streamlit Cloud)

## 🧑‍💻 Author

Sahil Sah