import mysql.connector
import datetime

# import statement for creating logs
import yaml
import logging.config

import configparser
import propertise


def logAndClearData():
    try:
        config = configparser.RawConfigParser()
        config.read('/home/ubuntu/utils/db_details.properties')

        # Creating database connection object and connecting to database
        db = mysql.connector.connect(
            host=propertise.host,
            user=propertise.username,
            password=propertise.password,
            database=propertise.database
        )

        # creating different datetime objects

        currentDate = datetime.datetime.today().date()
        previousday = currentDate - datetime.timedelta(days=1)
        daybeforeyesterday = currentDate - datetime.timedelta(days=2)
        week = currentDate - datetime.timedelta(days=7)

        # creating cursor object to execute sql queries
        cursor = db.cursor()
        logger.info("Creating cursor object.")

        # deleting today's alert data
        alert = """delete from alert_alert where timestamp like %s"""
        par = str(previousday) + "%"
        val = (par,)
        cursor.execute(alert, val)
        logger.info("Alert data deleted." + str(previousday))

        # Deleting yesterday data from daily-temperature table
        daily = """delete from sensors_dailytemperaturehumidity where timestamp like %s """
        par = str(previousday) + "%"
        val = (par,)
        cursor.execute(daily, val)
        logger.info("Daily Sensor data deleted." + str(previousday))

        # deleting last week data from weekly sensor table
        weeklydata = """delete from  sensors_weeklytemperaturehumidity  where timestamp like %s """
        par = str(week) + "%"
        val = (par,)
        cursor.execute(weeklydata, val)
        logger.info("Weekly sensor data deleted." + str(week))

        # commitng the changes to the database
        db.commit()

    except Exception as err:
        print(err)
        logger.exception(err)

    finally:
        # Closing cursor object
        cursor.close()
        logger.info("Closed cursor object.")


# the program execution starts from here
if __name__ == "__main__":
    # with open('/home/ubuntu/logs/logging_error.yaml', 'r') as stream:
    #     logger_config = yaml.load(stream, yaml.FullLoader)
    # logging.config.dictConfig(logger_config)
    logger = logging.getLogger('DailyDeletion -')

    logAndClearData()
