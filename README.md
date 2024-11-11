# Household Power Consumption Prediction

This project leverages machine learning to predict household power consumption for the next hour based on historical data from the last five hours. The model is deployed using Flask, providing both a web interface and an API for real-time predictions.

## Features

- **Power Consumption Prediction**: The app takes the following data from the past 5 hours and predicts the next hour’s power consumption:
  - **Global Active Power** (kW)
  - **Global Reactive Power** (kVAR)
  - **Voltage** (Volts)
  - **Sub Metering 1** (kW)
  - **Sub Metering 2** (kW)
  - **Sub Metering 3** (kW)
  - **Date** and **Time** for each hour
- **Web Interface**: A form-based user interface for submitting data and receiving predictions.
- **API**: An API endpoint that allows you to send POST requests with the data and receive the prediction in return.

## Technologies Used

- **Flask**: A lightweight Python web framework used to deploy the machine learning model and serve the web interface and API.
- **Scikit-Learn**: Machine learning library used to train the model, specifically using a Gradient Boosting algorithm for predicting power consumption.
- **Pickle**: A Python module used to serialize the trained machine learning model for deployment.
- **HTML/CSS**: For creating the frontend user interface.
- **requests**: To make HTTP requests to the API endpoint for testing.

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Set up a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:

    ```bash
    flask run
    ```

    The app will be available at `http://127.0.0.1:5000`.

## How to Use

### 1. Web Interface

- Open the web app in your browser.
- Navigate to the provided URL: [https://electric-power-forecasting.onrender.com](https://electric-power-forecasting.onrender.com).
- Enter the Date, Time, and power consumption data for the last 5 hours:
    - Global Active Power (kW)
    - Global Reactive Power (kVAR)
    - Voltage (Volts)
    - Sub Metering 1 (kW)
    - Sub Metering 2 (kW)
    - Sub Metering 3 (kW)
- Click "Predict" to receive the predicted power consumption for the next hour.

### 2. API Usage

The app also exposes an API endpoint for making predictions programmatically.

- **Endpoint**: `/predict-api`
- **Method**: POST

#### Request Payload (JSON format):

```json
{
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
```

## Model Details

The machine learning model is trained using historical data to predict future power consumption based on features such as global active power, global reactive power, voltage, and sub-metering values.

The model was trained using a Gradient Boosting algorithm, which was serialized using Pickle and is loaded for use in the app.

  
