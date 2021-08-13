from sqlalchemy import create_engine
import pandas as pd
from secrets import sql_conn

db_string = f"postgresql://{sql_conn['user']}:{sql_conn['password']}@{sql_conn['host']}:{sql_conn['port']}"

engine = create_engine(db_string)
conn = engine.connect()

upload_df = pd.read_csv('big_data.csv')

upload_df.to_sql('athlete_activities', conn, if_exists='replace', index=False)

