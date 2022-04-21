import mysql.connector
import datetime
from datetime import timedelta
# import statement for creating logs
import yaml
import logging.config

import configparser


def weekly(db):
    try:
        cursor = db.cursor()
        currentDate1 = datetime.date.today()
        currentDate = currentDate1 - timedelta(days=1)
        sqldayavg = "select asset_id,round(avg(p.temperature)) as temperature, p.time from (select asset_id,temperature, date_format(timestamp-interval minute(timestamp)%30 minute, '%Y-%m-%d %H:%i') as time from sensors_dailytemperaturehumidity where timestamp like '" + str(
            currentDate) + "%' group by date_format(timestamp-interval minute(timestamp)%30 minute, '%Y-%m-%d %H:%i'), temperature, asset_id) as p  group by p.time, asset_id;"

        cursor.execute(sqldayavg)
        result = cursor.fetchall()
        if result is not None:
            for row in result:
                print((row[1]), str(row[2]), str(row[0]))
                sql = "insert into sensors_weeklytemperaturehumidity (temperature, timestamp, asset_id) values(" + str(
                    row[1]) + ",'" + str(row[2]) + "'," + str(row[0]) + ");"
                cursor.execute(sql)
                db.commit()
            logger.info("Weekly thermal data stored.")
            return True

    except Exception as err:
        logger.exception(err)
        return False

    finally:
        cursor.close()


def monthly(db):
    try:
        cursor = db.cursor()
        today1 = datetime.datetime.today().date()
        today = today1 - timedelta(days=1)
        sql = "select distinct DATE(timestamp) as time,asset_id,round(avg(temperature)) from sensors_weeklytemperaturehumidity where timestamp like '" + \
              str(today) + "%' group by asset_id, time;"

        cursor.execute(sql)
        result1 = cursor.fetchall()
        if result1 is not None:

            for row in result1:
                print(row[2], row[0], row[1])
                sql = "insert into sensors_monthlytemperaturehumidity (temperature, timestamp, asset_id) values(" + str(
                    row[2]) + ",'" + str(row[0]) + "'," + str(row[1]) + ");"
                cursor.execute(sql)
                db.commit()
            logger.info("Monthly thermal data stored.")

    except Exception as err:
        logger.exception(err)

    finally:
        cursor.close()


if __name__ == '__main__':

    # with open('/home/ubuntu/logs/logging_error.yaml', 'r') as stream:
    #     logger_config = yaml.load(stream, yaml.FullLoader)

    # logging.config.dictConfig(logger_config)
    logger = logging.getLogger('Temp/Humid -')

    config = configparser.RawConfigParser()
    config.read('./db_details.properties')

    host = config.get('DatabaseSection', 'database.host')
    dbname = config.get('DatabaseSection', 'database.dbname')
    user = config.get('DatabaseSection', 'database.user')
    password = config.get('DatabaseSection', 'database.password')

    print(host, dbname, user)
    # Creating database connection object and connecting to data base
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=dbname
    )

    if weekly(db):
        monthly(db)
