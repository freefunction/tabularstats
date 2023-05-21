```markdown
# TabularStats

TabularStats is a Python package that provides descriptive analysis functionalities for tabular data from XLSX or CSV files. It is designed to help users gain insights into their data by calculating summary statistics, generating correlation matrices, identifying missing values, and retrieving unique values in specific columns.

## Installation

You can install TabularStats using pip:

```bash
pip install TabularStats
```

### Usage

Import the necessary functions from the TabularStats package:

```python
from TabularStats import load_data, summary_statistics, correlation_matrix, missing_data, unique_values
```

Load Data
To load tabular data from an XLSX or CSV file, use the `load_data` function:

```python
data = load_data('data.xlsx')
```
The `load_data` function takes the file path as the argument and returns the loaded data as a pandas DataFrame. It supports both XLSX and CSV file formats.

Summary Statistics
To calculate summary statistics for each column of the tabular data, use the `summary_statistics` function:

```python
statistics = summary_statistics(data)
print(statistics)
```

The `summary_statistics` function calculates common statistics, such as count, mean, standard deviation, minimum, maximum, and quartiles, for each column in the data. The result is returned as a pandas DataFrame, making it easy to analyze and interpret the summary statistics.

Correlation Matrix
To compute the correlation matrix for the numerical columns of the tabular data, use the `correlation_matrix` function:

```python
correlation = correlation_matrix(data)
print(correlation)
```

The `correlation_matrix` function selects the numerical columns from the data and calculates the pairwise correlation between them. The result is returned as a pandas DataFrame, which can be visualized or further analyzed to understand the relationships between different variables in the data.

Missing Data
To identify missing values in the tabular data, use the `missing_data` function:

```python
missing = missing_data(data)
print(missing)
```

The `missing_data` function checks each column of the data for missing values and returns a DataFrame indicating the count and percentage of missing values in each column. This information helps users understand the data quality and determine how to handle missing values in their analysis.

Unique Values
To retrieve the unique values in a specific column of the tabular data, use the `unique_values` function:

```python
unique = unique_values(data, 'Column1')
print(unique)
```

The `unique_values` function takes the data and the name of the column as arguments and returns a list of unique values in that column. This can be useful for understanding the distinct categories or values present in a particular column.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository. We appreciate your feedback and contributions to make TabularStats even better.

## License

This project is licensed under the MIT License . You are free to use, modify, and distribute this package according to the terms of the license.

We hope you find TabularStats helpful for your descriptive analysis needs! If you have any questions or need assistance, feel free to reach out.

Happy analyzing!
```