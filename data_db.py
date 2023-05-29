import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file into a DataFrame
df = pd.read_csv('data\\train.csv')

# Connect to the database
# engine = create_engine('sqlite:///output\\output_db.db', echo=True)

def add_table(df, table_name):

    # Connect to the database
    engine = create_engine('sqlite:///output\\output_db.db', echo=True)
    connection = engine.connect()
    df.to_sql(table_name, connection)
    connection.close()
    return


# # Add DataFrame to the database
# table_name = 'train_data'

# df.to_sql(table_name, engine, if_exists='replace', index=False)