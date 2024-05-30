# Simple ETL Pipeline in Python

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline implemented in Python. The ETL pipeline processes data from CSV files, performs basic transformations, and writes the transformed data to a new CSV file.

## Installation

1. Ensure you have Python installed on your system.
2. Install the necessary library by running the following command in your terminal:
   ```bash
   pip install pandas∂
   ```

## Project Structure

- `etl_pipeline.py`: The main script that implements the ETL pipeline.
- `data/source_data.csv`: The source CSV file containing the initial data.
- `data/transformed_data.csv`: The target CSV file where the transformed data will be saved.

## Steps

### Step 1: Create Example Data

Create a CSV file named `source_data.csv` in the `data` directory with the following content:

```
First_Name,Last_Name,Age
John,Doe,28
Jane,Smith,34
Jim,Beam,
Jack,Daniels,45
```

### Step 2: Run the ETL Pipeline

Execute the ETL pipeline by running the `etl_pipeline.py` script:

```bash
python etl_pipeline.py
```

### Step 3: Output

The transformed data will be saved in a CSV file named `transformed_data.csv` in the `data` directory. The content of the transformed CSV file will look like this:

```
First_Name,Last_Name,Age,Full_Name
John,Doe,28,john doe
Jane,Smith,34,jane smith
Jack,Daniels,45,jack daniels
```

## Summary

- **Extract**: The pipeline reads data from `source_data.csv`.
- **Transform**: The pipeline cleans the data by dropping rows with missing values, creates a new `Full_Name` column by concatenating `First_Name` and `Last_Name`, and converts the `Full_Name` to lowercase.
- **Load**: The pipeline writes the transformed data to `transformed_data.csv`.
