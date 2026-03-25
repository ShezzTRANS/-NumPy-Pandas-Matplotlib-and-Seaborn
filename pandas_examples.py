"""
Pandas Examples - DataFrame Operations and Data Analysis
"""

import pandas as pd
import numpy as np


def create_dataframe():
    """Demonstrate various ways to create DataFrames."""
    print("=== Creating DataFrames ===")
    
    # From dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
        'Salary': [50000, 60000, 75000, 80000, 55000]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame from dictionary:")
    print(df)
    print()
    
    return df


def dataframe_info(df):
    """Display information about the DataFrame."""
    print("=== DataFrame Information ===")
    
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Data types:\n{df.dtypes}")
    print(f"\nFirst 3 rows:\n{df.head(3)}")
    print(f"\nLast 2 rows:\n{df.tail(2)}")
    print(f"\nBasic statistics:\n{df.describe()}")
    print()


def data_selection(df):
    """Demonstrate data selection and filtering."""
    print("=== Data Selection and Filtering ===")
    
    # Select column
    print("Names column:")
    print(df['Name'])
    print()
    
    # Select multiple columns
    print("Name and Age columns:")
    print(df[['Name', 'Age']])
    print()
    
    # Filter rows
    print("People older than 30:")
    print(df[df['Age'] > 30])
    print()
    
    # Multiple conditions
    print("People older than 25 with Salary > 55000:")
    print(df[(df['Age'] > 25) & (df['Salary'] > 55000)])
    print()


def data_manipulation(df):
    """Demonstrate data manipulation operations."""
    print("=== Data Manipulation ===")
    
    # Add new column
    df_copy = df.copy()
    df_copy['Bonus'] = df_copy['Salary'] * 0.1
    print("DataFrame with Bonus column:")
    print(df_copy)
    print()
    
    # Modify existing column
    df_copy['Age'] = df_copy['Age'] + 1
    print("After incrementing Age by 1:")
    print(df_copy[['Name', 'Age']])
    print()
    
    # Drop column
    df_dropped = df_copy.drop('Bonus', axis=1)
    print("After dropping Bonus column:")
    print(df_dropped.columns.tolist())
    print()


def sorting_operations(df):
    """Demonstrate sorting operations."""
    print("=== Sorting Operations ===")
    
    # Sort by single column
    print("Sorted by Age (ascending):")
    print(df.sort_values('Age')[['Name', 'Age']])
    print()
    
    # Sort by multiple columns
    print("Sorted by Salary (descending):")
    print(df.sort_values('Salary', ascending=False)[['Name', 'Salary']])
    print()


def groupby_operations():
    """Demonstrate groupby operations."""
    print("=== GroupBy Operations ===")
    
    # Create sample data
    data = {
        'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'Finance'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Salary': [70000, 60000, 75000, 65000, 72000, 80000],
        'Years': [2, 5, 3, 7, 4, 10]
    }
    df = pd.DataFrame(data)
    
    print("Sample DataFrame:")
    print(df)
    print()
    
    # Group by Department
    print("Average salary by Department:")
    print(df.groupby('Department')['Salary'].mean())
    print()
    
    print("Multiple aggregations by Department:")
    print(df.groupby('Department').agg({
        'Salary': ['mean', 'max', 'min'],
        'Years': 'mean'
    }))
    print()


def missing_data_handling():
    """Demonstrate handling missing data."""
    print("=== Missing Data Handling ===")
    
    # Create DataFrame with missing values
    data = {
        'A': [1, 2, np.nan, 4, 5],
        'B': [5, np.nan, np.nan, 8, 9],
        'C': [10, 11, 12, 13, 14]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame with missing values:")
    print(df)
    print()
    
    print("Check for missing values:")
    print(df.isnull().sum())
    print()
    
    print("Fill missing values with 0:")
    print(df.fillna(0))
    print()
    
    print("Drop rows with missing values:")
    print(df.dropna())
    print()


def merge_join_operations():
    """Demonstrate merge and join operations."""
    print("=== Merge and Join Operations ===")
    
    # Create two DataFrames
    df1 = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David']
    })
    
    df2 = pd.DataFrame({
        'ID': [1, 2, 3, 5],
        'Salary': [50000, 60000, 75000, 80000]
    })
    
    print("DataFrame 1:")
    print(df1)
    print()
    
    print("DataFrame 2:")
    print(df2)
    print()
    
    # Inner join
    print("Inner join:")
    print(pd.merge(df1, df2, on='ID', how='inner'))
    print()
    
    # Left join
    print("Left join:")
    print(pd.merge(df1, df2, on='ID', how='left'))
    print()


def time_series_operations():
    """Demonstrate time series operations."""
    print("=== Time Series Operations ===")
    
    # Create date range
    dates = pd.date_range('2024-01-01', periods=10, freq='D')
    
    # Create time series DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Value': np.random.randint(10, 100, 10)
    })
    
    print("Time series DataFrame:")
    print(df)
    print()
    
    # Set date as index
    df.set_index('Date', inplace=True)
    
    print("With date as index:")
    print(df)
    print()


def apply_operations():
    """Demonstrate apply operations."""
    print("=== Apply Operations ===")
    
    data = {
        'Name': ['alice', 'bob', 'charlie'],
        'Score': [85, 92, 78]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    print()
    
    # Apply function to column
    df['Name_Upper'] = df['Name'].apply(lambda x: x.upper())
    
    print("After applying upper() to Name:")
    print(df)
    print()
    
    # Apply function to calculate grade
    def get_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        else:
            return 'C'
    
    df['Grade'] = df['Score'].apply(get_grade)
    
    print("After adding Grade column:")
    print(df)
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("Pandas Examples")
    print("=" * 60)
    print()
    
    df = create_dataframe()
    dataframe_info(df)
    data_selection(df)
    data_manipulation(df)
    sorting_operations(df)
    groupby_operations()
    missing_data_handling()
    merge_join_operations()
    time_series_operations()
    apply_operations()
    
    print("=" * 60)
    print("All Pandas examples completed successfully!")
    print("=" * 60)
