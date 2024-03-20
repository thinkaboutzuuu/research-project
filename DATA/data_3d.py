'''
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Get a list of all CSV files in the folder
folder_path = 'Cleaned Datas'  # Specify the folder path
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Create an empty DataFrame to store all data
all_data = pd.DataFrame()

# Read data from all CSV files and concatenate into one DataFrame
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    all_data = pd.concat([all_data, df])

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data points
ax.scatter(all_data['Date'], all_data['Close'], all_data['Volume'], c='blue', marker='o', label='Close Price')

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.set_zlabel('Volume')
ax.set_title('3D Scatter Plot of Stock Data')

# Rotate the plot
ax.view_init(azim=45)

# Show plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read data from CSV file
df = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the path to your CSV file

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data points
ax.scatter(df['Date'], df['Close'], df['Volume'], c='blue', marker='o', label='Close Price')

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.set_zlabel('Volume')
ax.set_title('3D Scatter Plot of Stock Data')

# Rotate the plot
ax.view_init(azim=45)

# Show plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data (replace this with your actual dataset)
data = {
    'Date': ['2011-09-15', '2006-07-11', '1998-02-19', '2013-06-18', '1999-07-20'],
    'Open': [11.19950008392334, 1.7869999408721924, 0.2554689943790436, 13.95400047302246, 3.2281250953674316],
    'High': [11.359999656677246, 1.7960000038146973, 0.2645829916000366, 14.145500183105469, 3.234375],
    'Low': [11.0625, 1.750499963760376, 0.2541669905185699, 13.905500411987305, 3.00156307220459],
    'Close': [11.33899974822998, 1.7829999923706057, 0.26145800948143, 14.088000297546388, 3.003124952316284],
    'Volume': [112176000.0, 121772000.0, 88728000.0, 42922000.0, 344436000.0]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data points
ax.scatter(df['Date'], df['Close'], df['Volume'], c='blue', marker='o', label='Close Price')

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.set_zlabel('Volume')
ax.set_title('3D Scatter Plot of Stock Data')

# Rotate the plot
ax.view_init(azim=45)

# Show plot
plt.show()
'''