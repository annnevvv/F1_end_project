import requests
import pandas as pd
def unpack_lists(driver):

    result = []
    for key in driver.keys():
        if isinstance(driver[key], dict):
            result.append(driver[key])
    return result




def get_sprint_result(year=None, race=None):
    if year or race:
        assert year and race, 'You must specify both a year and a race'
        url = 'http://ergast.com/api/f1/{}/{}/sprint.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/last/sprint.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    race_result = r.json()
    result_dict = race_result["MRData"]['RaceTable']['Races'][0]['SprintResults']

    # Unpack the lists of dicts in result_dict and reformat the result
    for driver in result_dict:
        drive_dict = unpack_lists(driver)
        driver_info = drive_dict[0]
        constructor_info = drive_dict[1]
        driver['driver'] = driver_info['givenName'] + ' ' + driver_info['familyName']
        driver['driverID'] = driver_info['driverId']
        driver['nationality'] = driver_info['nationality']
        driver['constructor'] = constructor_info['name']
        driver['constructorID'] = constructor_info['constructorId']

    # Select the columns that are relevant to the race result
    cols = ['number', 'position', 'positionText', 'grid', 'points', 'driverID', 'driver',
            'nationality', 'constructorID', 'constructor', 'laps', 'status', 'Time']
    return pd.DataFrame(result_dict)[cols]

