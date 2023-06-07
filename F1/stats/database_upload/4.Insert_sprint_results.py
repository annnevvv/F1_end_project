from User_data import host, user, password
import pandas as pd
import workings_sprint_results
from sqlalchemy import create_engine

"""
for error 'No module named 'MySQLdb'' - pip install mysqlclient

"""
sprint = input("Type sprint number associated with race: ")

try:
    data = workings_sprint_results.get_sprint_result(year=2023, race=sprint)
    columns = ['position', 'points', 'driverID', 'constructorID', 'laps']
    result = pd.DataFrame(data, columns=columns)
    result = result.astype({'position': 'int'})
    result = result.set_index(['position'])
    result['circuitID'] = sprint+'s'
    con = create_engine(f'mysql://{user}:{password}@{host}:3306/formula1')
    result.to_sql('drivers_results', con=con, if_exists='append')
except IndexError:
    print(f"Race {sprint} has not yet taken place. Please refer to Circuit schedule  ")
except AssertionError:
    print(f"Please insert INT number ")







