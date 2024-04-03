import pandas as pd
import numpy as np
import os

# Define the date range
date_range = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Create a DataFrame
data = {
    "Date": date_range,
    "IsHoliday": np.random.choice([0, 1], len(date_range)),
    "Precipitation": np.random.uniform(0, 10, len(date_range)),
    "DayOfWeek": date_range.dayofweek,
}

# Define crowd size based on day of the week
# Higher crowds on Sunday, lower crowds on working days
data["CrowdSize"] = np.where(data["DayOfWeek"] == 6, np.random.randint(800, 1000, len(date_range)), np.random.randint(100, 400, len(date_range)))

df = pd.DataFrame(data)

# Save the dataset to a specific directory (use double backslashes)
save_directory = "C:\\Users\\udgir\\OneDrive\\Desktop\\miniproject2"
df.to_csv(os.path.join(save_directory, "mydataset.csv"), index=False)

current_directory = os.getcwd()
print("Current working directory:", current_directory)

# List files in the current directory
files = os.listdir(current_directory)
print("Files in the current directory:", files)
