import sqlite3
from . import parser as parserMod
import os

# Settingpath for database file
project_root = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(project_root, '..' ,'data', 'birds.db')

def getBird(state: str):
    # Setting connection
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    # Executing query
    row = cursor.execute(f"select * from birds where abbreviation = '{state}';")
    res = row.fetchall()
    list_accumulator = []
    for item in res:
        list_accumulator.append(parserMod.constructBirdInformationData(item))
    return list_accumulator
