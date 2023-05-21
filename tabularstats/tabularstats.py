# tabularstats.py

import pandas as pd

def load_data(file_path, file_type='xlsx'):
    """
    Load tabular data from an XLSX or CSV file.
    Args:
        file_path (str): The path to the file.
        file_type (str): The type of file, either 'xlsx' or 'csv'.
    Returns:
        pandas.DataFrame: The loaded tabular data.
    """
    if file_type == 'xlsx':
        data = pd.read_excel(file_path)
    elif file_type == 'csv':
        data = pd.read_csv(file_path)
    else:
        raise ValueError("Invalid file type. Supported types: 'xlsx', 'csv'")
    
    return data

def summary_statistics(data):
    """
    Calculate summary statistics for each column of the tabular data.
    Args:
        data (pandas.DataFrame): The tabular data.
    Returns:
        pandas.DataFrame: A DataFrame containing the summary statistics.
    """
    statistics = data.describe(include='all').transpose()
    return statistics

def correlation_matrix(data):
    """
    Calculate the correlation matrix for the numerical columns of the tabular data.
    Args:
        data (pandas.DataFrame): The tabular data.
    Returns:
        pandas.DataFrame: The correlation matrix.
    """
    numerical_columns = data.select_dtypes(include='number').columns
    correlation_matrix = data[numerical_columns].corr()
    return correlation_matrix

def missing_data(data):
    """
    Identify missing values in the tabular data.
    Args:
        data (pandas.DataFrame): The tabular data.
    Returns:
        pandas.DataFrame: A DataFrame with columns representing the columns of the input data
                          and rows indicating whether the corresponding column has missing values.
    """
    missing_values = data.isnull().sum().to_frame(name='Missing Values')
    missing_values['Percentage'] = (missing_values['Missing Values'] / len(data)) * 100
    return missing_values

def unique_values(data, column):
    """
    Get the unique values in a specific column of the tabular data.
    Args:
        data (pandas.DataFrame): The tabular data.
        column (str): The name of the column to retrieve unique values from.
    Returns:
        list: A list of unique values in the specified column.
    """
    unique_vals = data[column].unique().tolist()
    return unique_vals
