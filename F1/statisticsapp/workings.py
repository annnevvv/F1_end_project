from django.db import models
from statisticsapp.models import RaceResults
from django.db import transaction
import pandas as pd
import pyergast.pyergast


"""
for error 'No module named 'MySQLdb'' - pip install mysqlclient
Insert race number - 1-3 - this is run number in current season

"""
race = input("Type race number: ")

try:
    data = pyergast.pyergast.get_race_result(year=2023, race=race)
    columns = ['position', 'points', 'driver', 'driverID', 'constructor', 'laps']
    result = pd.DataFrame(data, columns=columns)
    result = result.astype({'position': 'int'})
    result = result.set_index(['position'])
    result['circuitID'] = race


    with transaction.atomic():
        for index, row in result.iterrows():
            race_result = RaceResults(
                driverID=row['driverID'],
                driver=row['driver'],
                position=row['position'],
                points=row['points'],
                constructor=row['constructor'],
                laps=row['laps'],
                circuitID=row['circuitID']
            )
            race_result.save()

except IndexError:
    print(f"Race {race} has not yet taken place. Please refer to Circuit schedule.")
except AssertionError:
    print(f"Please insert INT number.")