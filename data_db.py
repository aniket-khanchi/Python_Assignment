import pandas as pd
from sqlalchemy import create_engine


def add_table(df, table_name):

    # Connect to the database
    engine = create_engine('sqlite:///output\\output_db.db', echo=True)
    connection = engine.connect()
    df.to_sql(table_name, connection, if_exists='replace', index=False)
    connection.close()
    return

