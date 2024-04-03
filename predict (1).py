import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from datetime import datetime

# Load the dataset
dataset = pd.read_csv("C:\\Users\\udgir\\OneDrive\\Desktop\\miniproject2\\mydataset.csv")

# Convert the "Date" column to a datetime object
dataset['Date'] = pd.to_datetime(dataset['Date'])

# Define a function to categorize the day of the week
def categorize_day(day_of_week):
    if day_of_week == 6:  # Sunday
        return "High"
    else:  # Working days (Monday to Friday)
        return "Low"

# Apply the categorization to the dataset
dataset['CrowdCategory'] = dataset['Date'].dt.dayofweek.apply(categorize_day)

# Convert the categorical labels into one-hot encoding
dataset = pd.get_dummies(dataset, columns=['CrowdCategory'], drop_first=True)

# Input a date from the user
user_date = input("Enter a date (YYYY-MM-DD): ")

# Convert the user input to a datetime object
user_date = datetime.strptime(user_date, "%Y-%m-%d")

# Filter the dataset for the user's date
user_data = dataset[dataset['Date'] == user_date]

if len(user_data) == 0:
    print(f"No data available for {user_date.strftime('%Y-%m-%d')}.")
else:
    # Define features and target variable
    X = dataset[['IsHoliday', 'Precipitation', 'CrowdCategory_Low']]
    y = dataset['CrowdSize']

    # Initialize and train a decision tree regressor
    model = DecisionTreeRegressor()
    model.fit(X, y)

    # Predict the crowd size for the user's date
    user_day_category = categorize_day(user_date.weekday())
    if user_day_category == "Low":
        user_features = [int(user_date in dataset['Date']), 0, 1]  # 1 corresponds to 'Low' category
    else:
        user_features = [int(user_date in dataset['Date']), 0, 0]  # 0 corresponds to 'High' category
    predicted_crowd_size = model.predict([user_features])[0]

    # Calculate the percentage of predicted crowd size
    reference_value = dataset['CrowdSize'].max()
    percentage_predicted = (predicted_crowd_size / reference_value) * 100

    print(f"Predicted crowd size for {user_date.strftime('%Y-%m-%d')} as a percentage of the maximum: {percentage_predicted:.2f}%")
