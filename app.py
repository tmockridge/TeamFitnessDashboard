import pandas as pd
# from sqlalchemy import create_engine
# import psycopg2

maindf = pd.read_json("data1.json")
print(maindf.info())

pages = [2,3,4,5,6,7,8]
for page in pages:
    print(f"loadingpage{page}")

    df = pd.read_json(f"data{page}.json")
    # print(df.info())
    maindf = maindf.append(df)

    print(maindf.info())

maindf.to_csv('data.csv')