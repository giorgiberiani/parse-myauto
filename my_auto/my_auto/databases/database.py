from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, adapt, AsIs
import psycopg2


class MyAutoDB():

    def __init__(self, hostname, username, password, database, port):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.make_connection(database)

    def make_connection(self, db_name):
        self.connection = psycopg2.connect(
            port=self.port,
            host=self.hostname,
            user=self.username,
            password=self.password,
            dbname=db_name)
        print('Connected to database {}'.format(db_name))

    def create_database(self, db_name):
        cur = self.connection.cursor()
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute("CREATE DATABASE {};".format(db_name))
        self.connection.commit()
        print('{} database created'.format(db_name))

    def use_database(self, db_name):
        self.make_connection(db_name)
        print("Using database {}".format(db_name))

    def create_table(self, table_name):
        cur = self.connection.cursor()
        cur.execute("CREATE TABLE if not exists {} (\
                    carid text,\
                    time text,\
                    customs text,\
                    location text,\
                    manufacturer text,\
                    model text,\
                    year text,\
                    category text,\
                    fuel_type text,\
                    engine_volume text,\
                    mileage text,\
                    cylinders text,\
                    gear_type text,\
                    drive_wheels text,\
                    doors text,\
                    wheel text,\
                    color text,\
                    interior_color text,\
                    airbags text,\
                    abs text,\
                    el_windows text,\
                    air_condintioner text,\
                    climate_system text,\
                    leather_interior text,\
                    disks text,\
                    navigation_system text,\
                    central_lock text,\
                    hatch text,\
                    alarm text,\
                    board_computer text,\
                    hydraulics text,\
                    anti_skid text,\
                    chair_warming text,\
                    parking_control text,\
                    rear_view_camera text,\
                    price text,\
                    description text,\
                    primary key (carid, time));".format(table_name))
        self.connection.commit()
        print("{} table created".format(table_name))

    def insert(self, table, item):
        cur = self.connection.cursor()
        columns = item.keys()
        values = ['null' if not item[column] else "'" +
                  str(item[column]).replace("'", "''") +
                  "'" for column in columns]
        columns = ','.join(columns)
        values = ','.join(values)
        query = "INSERT INTO {}({}) VALUES ({}) ON CONFLICT DO NOTHING".format(
            table, columns, values)
        try:
            cur.execute(query)
        except psycopg2.Error as ex:
            self.connection.rollback()
            print('cant write', ex)
            return
        self.connection.commit()
        print("insertion success in {}, {}".format(table, item['carid']))

    def drop_database(self, db_name):
        cur = self.connection.cursor()
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute("DROP DATABASE {};".format(db_name))
        self.connection.commit()
        print("{} database deleted".format(db_name))

    def drop_table(self, table_name):
        cur = self.connection.cursor()
        cur.execute("DROP TABLE {}".format(table_name))
        self.connection.commit()
        print("{} table deleted".format(table_name))
