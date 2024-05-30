import pandas as pd

def extract(file_path):
    """Extract data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def transform(data):
    """Transform the data by cleaning and enriching."""
    # Example transformation: Drop rows with missing values
    data = data.dropna()

    # Example transformation: Create a new column based on existing data
    data['Full_Name'] = data['First_Name'] + ' ' + data['Last_Name']
    
    # Example transformation: Convert all text to lowercase
    data['Full_Name'] = data['Full_Name'].str.lower()

    return data

def load(data, target_file_path):
    """Load the transformed data into a new CSV file."""
    data.to_csv(target_file_path, index=False)

def etl_pipeline(source_file_path, target_file_path):
    """Run the full ETL pipeline."""
    # Step 1: Extract
    data = extract(source_file_path)
    print("Data extracted successfully.")

    # Step 2: Transform
    data = transform(data)
    print("Data transformed successfully.")

    # Step 3: Load
    load(data, target_file_path)
    print("Data loaded successfully.")

# Example usage
source_file = 'data/source_data.csv'
target_file = 'data/transformed_data.csv'

etl_pipeline(source_file, target_file)
