from User_data import host, user, password
import pandas as pd
import pyergast.pyergast
from sqlalchemy import create_engine

"""
for error 'No module named 'MySQLdb'' - pip install mysqlclient
Insert race number - 1-3 - this is run number in current season

"""
race = input("Type race number: ")

try:
    data = pyergast.pyergast.get_race_result(year=2023, race=race)
    columns = ['position', 'points', 'driverID', 'constructorID', 'laps']
    result = pd.DataFrame(data, columns=columns)
    result = result.astype({'position': 'int'})
    result = result.set_index(['position'])
    result['circuitID'] = race
    con = create_engine(f'mysql://{user}:{password}@{host}:3306/formula1')
    result.to_sql('drivers_results', con=con, if_exists='append')
except IndexError:
    print(f"Race {race} has not yet taken place. Please refer to Circuit schedule  ")
except AssertionError:
    print(f"Please insert INT number ")







