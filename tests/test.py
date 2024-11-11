import requests

# URL of the Flask API endpoint
url = 'http://127.0.0.1:5000/predict_api'

# Data for the last 5 hours (use the data provided above)
data = {
    "data": [
        {
            "Date": "16/12/2006",
            "Time": "17:24:00",
            "Global_active_power": 4.216,
            "Global_reactive_power": 0.418,
            "Voltage": 234.840,
            "Global_intensity": 18.400,
            "Sub_metering_1": 0.000,
            "Sub_metering_2": 1.000,
            "Sub_metering_3": 17.000
        },
        {
            "Date": "16/12/2006",
            "Time": "17:25:00",
            "Global_active_power": 4.220,
            "Global_reactive_power": 0.420,
            "Voltage": 234.850,
            "Global_intensity": 18.420,
            "Sub_metering_1": 0.000,
            "Sub_metering_2": 1.000,
            "Sub_metering_3": 17.000
        },
        {
            "Date": "16/12/2006",
            "Time": "17:26:00",
            "Global_active_power": 4.230,
            "Global_reactive_power": 0.425,
            "Voltage": 234.860,
            "Global_intensity": 18.430,
            "Sub_metering_1": 0.000,
            "Sub_metering_2": 1.000,
            "Sub_metering_3": 17.000
        },
        {
            "Date": "16/12/2006",
            "Time": "17:27:00",
            "Global_active_power": 4.240,
            "Global_reactive_power": 0.430,
            "Voltage": 234.870,
            "Global_intensity": 18.440,
            "Sub_metering_1": 0.000,
            "Sub_metering_2": 1.000,
            "Sub_metering_3": 17.000
        },
        {
            "Date": "16/12/2006",
            "Time": "17:28:00",
            "Global_active_power": 4.250,
            "Global_reactive_power": 0.435,
            "Voltage": 234.880,
            "Global_intensity": 18.450,
            "Sub_metering_1": 0.000,
            "Sub_metering_2": 1.000,
            "Sub_metering_3": 17.000
        }
    ]
}

# Send the POST request to the Flask API
response = requests.post(url, json=data)

# Print the prediction response
print(response.json())
