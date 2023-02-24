from manga import connection
from psycopg2 import sql

from manga.models.classes import Demographic

def add_Demographic(demographic):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Demographics(demo)
    VALUES (%s)
    """)
    cursor.execute(user_sql, (demographic,))
    connection.commit()
    cursor.close()

def delete_Demographic(demographic):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Demographics
    WHERE demo=%s
    """)
    cursor.execute(user_sql, (demographic,))
    connection.commit()
    cursor.close()

def select_Demographics():
    cursor = connection.cursor()
    sql = """
    SELECT demo, description FROM Demographics
    ORDER BY demo ASC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    demographics = []
    for demo in results:
        demographics.append(Demographic(demo))
    return demographics

def connect_Demographic(series, series_year, demo):
    if series == "" or series_year == "" or demo == "":
        return
    if check_Demographic_Exists(demo) == False:
        add_Demographic(demo)

    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Demographic_Of(series, series_year, demo)
    VALUES (%s, %s, %s)
    """)
    cursor.execute(user_sql, (series, series_year, demo))
    connection.commit()
    cursor.close()

def check_Demographic_Exists(demographic):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT * FROM Demographics
    WHERE demo=%s
    """)
    cursor.execute(user_sql, (demographic,))
    result = cursor.fetchone()
    cursor.close()
    return (result != None)