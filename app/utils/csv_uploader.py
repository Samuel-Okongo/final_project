import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file to load.
    
    Returns:
        DataFrame: A pandas DataFrame containing the CSV data.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        raise

def validate_data(df):
    """
    Validate the DataFrame columns and data.
    
    Args:
        df (DataFrame): The DataFrame to validate.
    
    Returns:
        bool: True if the data is valid, or False.
    """
    required_columns = {'username', 'email', 'role'}
    if not required_columns.issubset(df.columns):
        print("CSV file is missing one or more required columns: username, email, role.")
        return False
    
    # Example of basic data validation
    if df['email'].apply(lambda x: '@' not in x).any():
        print("Some email addresses are invalid.")
        return False
    
    return True

def create_user(username, email, role):
    """
    Simulate creating a user in the database.
    
    Args:
        username (str): The user's username.
        email (str): The user's email.
        role (str): The user's role.
    """
    print(f"Creating user {username} with email {email} and role {role}")
    # Here you would add the logic to insert the user into your database.
    # For example: User.create(username=username, email=email, role=role)

def process_csv_data(file_path):
    """
    Process a CSV file to load and create user profiles.
    
    Args:
        file_path (str): The path to the CSV file.
    """
    df = load_csv(file_path)
    if validate_data(df):
        df.apply(lambda row: create_user(row['username'], row['email'], row['role']), axis=1)
        print("All users have been created successfully.")
    else:
        print("Data validation failed.")

