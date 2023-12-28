# Column Name Matching and Renaming Tool

## Overview

This script is designed to match column names in a CSV file with a predefined set of names stored in a JSON file. If a match is found, the script renames the corresponding columns in the CSV file using the values associated with the matched keys.

## Usage

1. **Input Files:**
   - Ensure that you have the CSV file containing the original column names.
   - Create a JSON file with a dictionary mapping original column names to their desired new names.

2. **Code Execution:**
   - Execute the Python script.
   - The script reads the JSON file to obtain the column name mapping.
   - It loads the CSV file into a Pandas DataFrame.

3. **Column Matching and Renaming:**
   - For each column in the DataFrame, the script checks if there is a match with any key in the JSON file.
   - If a match is found, the script renames the column using the associated value from the JSON file.

4. **Output:**
   - The modified DataFrame is saved to a new CSV file with the updated column names.

## Example

Consider the following JSON file (`columnnames.json`):

```json
{
  "old_column_1": "new_column_1",
  "old_column_2": "new_column_2",
  "old_column_3": "new_column_3"
}
```

And the CSV file with columns:

```
old_column_1, old_column_2, old_column_3, other_column
```

After running the script, the new CSV file will have the columns:

```
new_column_1, new_column_2, new_column_3, other_column
```

## Dependencies

- Python 3.x
- pandas library

## Author

Sanjana Ramesh
