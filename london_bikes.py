import pandas as pd

bikes = pd.read_csv("C://Users//addam//Documents//london-bike-sharing-dataset//london_merged.csv")

# Generate the first 5 rows of the dataframe
print(bikes.head())

# Exploring the data
print(bikes.info())

# After loading the CSV: Verify dataframe size (rows, cols)
print(bikes.shape)

# Count the unique values in the weather_code column
print(bikes.weather_code.value_counts())

# Count the unique values in the season column
print(bikes.season.value_counts())

# Specifying the column names that I want to use
new_cols_dict = {
    'timestamp': 'time',
    'cnt': 'count',
    't1': 'temp_real_C',
    't2': 'temp_feels_like_C',
    'hum': 'humidity_percent',
    'wind_speed': 'wind_speed_kph',
    'weather_code': 'weather',
    'is_holiday': 'is_holiday',
    'is_weekend': 'is_weekend',
    'season': 'season',
}

# Renaming the columns to the specified column names
bikes = bikes.rename(columns=new_cols_dict)

# Changing the humidity values to percentage (i.e. a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent / 100

# Creating a season dictionary so that we can map the integers to the actual written values

season_dict = {
    '0.0': 'Spring',
    '1.0': 'Summer',
    '2.0': 'Autumn',
    '3.0': 'Winter',
}

# Creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0': 'Clear',
    '2.0': 'Scattered Clouds',
    '3.0': 'Broken Clouds',
    '4.0': 'Cloudy',
    '7.0': 'Rain',
    '10.0': 'Rain with Thunderstorm',
    '26.0': 'Snowfall',
}

# Changing the seasons column data type to string
bikes.season = bikes.season.astype('str')
# Mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)


# Changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')
# Mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dict)

# Checking our dataframe to see if the mappings have worked
print(bikes.head())

# Writing the final dataframe to an Excel file that we will use in our tableau visualisation
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')