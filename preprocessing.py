import pandas as pd
import numpy as np

def process_time_series_data(data):
    """
    Processes JSON-like data into a pandas DataFrame, performs transformations, 
    and extracts cyclical features from the time series.
    
    Parameters:
        data (dict): JSON-like dictionary containing time series data. Expected to have a 'data' key 
                     with a list of records, each having 'Date', 'Time', 'Global_active_power', 
                     'Sub_metering_1', 'Sub_metering_2', and 'Sub_metering_3'.
    
    Returns:
        pd.DataFrame: DataFrame with the processed features.
    """
    # Convert JSON-like data to DataFrame
    df = pd.DataFrame(data)
    
    # Combine 'Date' and 'Time' columns into a datetime index
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M:%S')
    df.set_index('Datetime', inplace=True)
    
    # Calculate Power_Sub_Diff
    df['Power_Sub_Diff'] = df['Global_active_power'] - (df['Sub_metering_1'] + df['Sub_metering_2'] + df['Sub_metering_3'])
    
    # Extract hour, day of year, and month for cyclical features
    hours = df.index.hour
    days = df.index.dayofyear
    months = df.index.month
    
    # Hour of the day
    df['sin_Hour'] = np.sin(2 * np.pi * hours / 24)
    df['cos_Hour'] = np.cos(2 * np.pi * hours / 24)
    
    # Day of the year
    df['sin_Day'] = np.sin(2 * np.pi * days / 365)
    df['cos_Day'] = np.cos(2 * np.pi * days / 365)
    
    # Month of the year
    df['sin_Month'] = np.sin(2 * np.pi * months / 12)
    df['cos_Month'] = np.cos(2 * np.pi * months / 12)
    
    # Drop the original 'Date' and 'Time' columns
    df.drop(['Date', 'Time'], axis=1, inplace=True)
    
    return df


def df_to_X_single_sample(df, window_size=5):
    """
    Extracts the last `window_size` sequence from a DataFrame, but raises an error if the 
    DataFrame has fewer than `window_size` rows.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame with time series data.
        window_size (int): Number of time steps in the input sequence (default is 5).
    
    Returns:
        np.array: 3D array of shape (1, window_size, num_features) for the feature (X) sample.
    
    Raises:
        ValueError: If the DataFrame has fewer than `window_size` rows.
    """
    # Check if the DataFrame has enough rows
    if len(df) < window_size:
        raise ValueError(f"The DataFrame has fewer than {window_size} rows. Cannot extract a sequence.")
    
    # Take the last `window_size` rows
    X_single = df.iloc[-window_size:].to_numpy()

    # Reshape to 3D array with one sample (1, window_size, num_features)
    X_single = np.expand_dims(X_single, axis=0)
    # Reshape to 2D array with one sample (1, window_size * num_features)
    return X_single.reshape(X_single.shape[0],-1)


