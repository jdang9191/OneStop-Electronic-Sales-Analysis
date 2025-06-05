from sqlalchemy import create_engine

def upload_to_postgres(df, table_name):
    engine = create_engine('postgresql://Jonny@localhost:5432/one_stop_electronics')
    df.to_sql(table_name, engine, if_exists='replace', index=False)