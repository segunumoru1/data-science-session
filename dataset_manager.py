# Use OOP concepts by building a Python class that loads, filters, and summarizes data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DatasetManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def preview_data(self, num_rows=5):
        return self.df.head(num_rows)

    def filter_data(self, column, value):
        self.df = self.df[self.df[column] >= value]

    def summarize_data(self):
        return self.df.describe()

# Example usage
if __name__ == "__main__":
    # Initialize the DatasetManager with a CSV file path
    manager = DatasetManager('C:\\Users\\SEGUN\\Documents\\Ify Data Science MC\\week1_customer_data.csv')

    # Preview the first 5 rows of the dataset
    print("Data Preview:")
    print(manager.preview_data())

    # Filter the dataset where 'purchase_amount' equals 'value'
    purchase_value = 50.23  # Example value to filter by
    manager.filter_data('purchase_amount', purchase_value)

    # Summarize the filtered dataset
    print("\nData Summary:")
    print(manager.summarize_data())

    # calculate the average age by gender
    average_age_gender = manager.df.groupby('gender')['age'].mean()
    print("\nAverage Age by Gender:")
    print(average_age_gender)

    # visualize the average age by gender using pie chart
    average_age_gender.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Average Age by Gender')
    plt.show()