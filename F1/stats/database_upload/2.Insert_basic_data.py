from User_data import host, user, password
import pymysql

pymysql.install_as_MySQLdb()

drivers = [('max_verstappen', 'Max Verstappen','Dutch','red_bull'),
           ('hamilton', 'Lewis Hamilton','British','mercedes'),
           ('alonso', 'Fernando Alonso','Spanish','aston_martin'),
           ('stroll', 'Lance Stroll','Canadian','aston_martin'),
           ('perez', 'Sergio Pérez','Mexican','red_bull'),
           ('norris', 'Lando Norris','British','mclaren'),
           ('hulkenberg', 'Nico Hülkenberg','German','haas'),
           ('piastri', 'Oscar Piastri','Australian','mclaren'),
           ('zhou', 'Guanyu Zhou','Chinese','alfa'),
           ('tsunoda', 'Yuki Tsunoda','Japanese','alphatauri'),
           ('bottas', 'Valtteri Bottas','Finnish','alfa'),
           ('sainz', 'Carlos Sainz','Spanish','ferrari'),
           ('gasly', 'Pierre Gasly','French','alpine'),
           ('ocon', 'Esteban Ocon','French','alpine'),
           ('de_vries', 'Nyck de Vries','Dutch','alphatauri'),
           ('sargeant', 'Logan Sargeant','American','williams'),
           ('kevin_magnussen', 'Kevin Magnussen','Danish','haas'),
           ('russell', 'George Russell','British','mercedes'),
           ('albon', 'Alexander Albon','Thai','williams'),
           ('leclerc', 'Charles Leclerc','Monegasque','ferrari')
]

constructors = [('red_bull','Red Bull'),
                ('mercedes','Mercedes'),
                ('aston_martin','Aston Martin'),
                ('mclaren','McLaren'),
                ('haas','Haas F1 Team'),
                ('alfa','Alfa Romeo'),
                ('alphatauri','AlphaTauri'),
                ('ferrari','Ferrari'),
                ('alpine','Alpine F1 Team'),
                ('williams','Williams')]

circuits = [(1,'Bahrain Grand Prix', 'Bahrain', 'Sakhir', '2023-3-5', '15:00:00'),
            (2,'Saudi Arabian Grand Prix', 'Saudi Arabia', 'Jeddah',
             '2023-3-19','17:00:00'),
            (3,'Australian Grand Prix', 'Australia', 'Melbourne',
             '2023-4-2','05:00:00'),
            (4, 'Azerbaijan Grand Prix', 'Azerbaijan', 'Baku', '2023-4-30', '11:00:00'),
            ('4s', 'Azerbaijan Grand Prix', 'Azerbaijan', 'Baku', '2023-4-30', '11:00:00'),
            (5, 'Miami Grand Prix', 'USA', 'Miami, FL', '2023-5-7', '19:30:0'),
            (6, 'Grand Prix de Monaco', 'Monaco', 'Monaco', '2023-5-28', '13:00:00'),
            (7, 'Gran Premio de Espana', 'Spain', 'Barcelona', '2023-6-4', '13:00:00'),
            (8, 'Grand Prix du Canada', 'Canada', 'Montreal', '2023-6-18', '18:00:00'),
            (9, 'Grosser Preis von Osterreich', 'Austria', 'Spielberg',
             '2023-7-2', '13:00:00'),
            (10, 'British Grand Prix', 'Great Britain', 'Silverstone',
             '2023-7-9', '14:00:00'),
            (11, 'Hungarian Grand Prix', 'Hungary', 'Budapest', '2023-7-23', '13:00:00'),
            (12, 'Belgian Grand Prix', 'Belgium', 'Spa', '2023-7-30', '13:00:00'),
            (13, 'Dutch Grand Prix', 'Netherlands', 'Zandvoort',
             '2023-8-27', '13:00:00'),
            (14, "Gran Premio d'Italia", 'Italy', 'Monza', '2023-9-3', '13:00:00'),
            (15, 'Singapore Grand Prix', 'Singapore', 'Singapore',
             '2023-9-17', '12:00:00'),
            (16, 'Japanese Grand Prix', 'Japan', 'Suzuka', '2023-9-24', '05:00:00'),
            (17, 'Qatar Grand Prix', 'Qatar', 'Losail', '2023-10-8', '14:00:00'),
            (18, 'United States Grand Prix', 'USA', 'Austin, TX',
             '2023-10-22', '19:00:00'),
            (19, 'Gran Premio de la Ciudad de Mexico', 'Mexico',
             'Mexico City', '2023-10-29', '20:00:00'),
            (20, 'Grande Premio de Sao Paulo', 'Brazil', 'Sao Paulo',
             '2023-11-5', '17:00:00'),
            (21, 'Las Vegas Grand Prix', 'USA', 'Las Vegas, NV',
             '2023-11-19', '06:00:00'),
            (22,'Abu Dhabi Grand Prix', 'United Arab Emirates', 'Abu Dhabi',
            '2023-11-26', '13:00:00')]

driver_standings = [('max_verstappen', 'red_bull'),
                    ('perez', 'red_bull'),
                    ('alonso', 'aston_martin'),
                    ('hamilton', 'mercedes'),
                    ('sainz', 'ferrari'),
                    ('stroll', 'aston_martin'),
                    ('russell', 'mercedes'),
                    ('norris', 'mclaren'),
                    ('hulkenberg', 'haas'),
                    ('leclerc', 'ferrari'),
                    ('bottas', 'alfa'),
                    ('ocon', 'alpine'),
                    ('piastri', 'mclaren'),
                    ('gasly', 'alpine'),
                    ('zhou', 'alfa'),
                    ('tsunoda', 'alphatauri'),
                    ('kevin_magnussen', 'haas'),
                    ('albon', 'williams'),
                    ('sargeant', 'williams'),
                    ('de_vries', 'alphatauri')]

constructor_standings = [('red_bull'),
                ('mercedes'),
                ('aston_martin'),
                ('mclaren'),
                ('haas'),
                ('alfa'),
                ('alphatauri'),
                ('ferrari'),
                ('alpine'),
                ('williams')]


db = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     database='formula1')

with db:
    cursor = db.cursor()
    for constructor in constructors:
        cursor.execute(
            "insert into constructors(constructorID, name) values(%s, %s)",
            constructor)
        db.commit()

    for driver in drivers:
        cursor.execute(
            "insert into drivers(driverID,driver, country, constructorID) values(%s, %s, %s, %s)",
            driver)
        db.commit()

    for circuit in circuits:
        cursor.execute(
            "insert into circuits(circuitID, name, country, city, date, time) values(%s, %s, %s, %s, %s, %s)",
            circuit)
        db.commit()

    for ds in driver_standings:
        cursor.execute(
            "insert into driver_standings(driverID, constructorID) values(%s, %s)",ds)
        db.commit()

    for cs in constructor_standings:
        cursor.execute(
            "insert into constructor_standings(constructorID) values(%s)",cs)
        db.commit()

