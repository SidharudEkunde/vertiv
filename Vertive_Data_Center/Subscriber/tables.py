from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, LargeBinary, ForeignKey, DateTime
from sqlalchemy.sql import func

Base = declarative_base()


class System(Base):
    __tablename__ = 'system_system'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    sysid = Column(Integer)
    image = Column(LargeBinary)
    capacity = Column(Integer)


class Sensor(Base):
    """ creating a sensor_temperaturehumidity class for accessing the sensor_temperaturehumidity tables attributes """

    __tablename__ = 'sensors_temperaturehumidity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    macid = Column(String(20))
    temperature = Column(Float)
    systemid_id = Column(ForeignKey(System.id, ondelete='CASCADE'))
    lastseen = Column(DateTime(timezone=True))
    battery = Column(Float)
    min = Column(Float)
    max = Column(Float)


class alert_alert(Base):
    """ creating alert_alert class for accessing the alert_alert tables attributes """

    __tablename__ = 'alert_alert'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    lastseen = Column(DateTime(timezone=True), server_default=func.now())
    macid_id = Column(ForeignKey(Sensor.id, ondelete='CASCADE'))


class SensorDailyTempHumi(Base):
    __tablename__ = 'sensors_dailytemperaturehumidity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float)
    timestamp = Column(DateTime(timezone=True))
    asset_id = Column(ForeignKey(
        Sensor.id, ondelete='CASCADE'))


# class SensorWeekly(Base):
#     __tablename__ = 'sensors_weeklytemperaturehumidity'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     temperature = Column(Float)
#     humidity = Column(Float)
#     timestamp = Column(DateTime(timezone=True))
#     asset_id = Column(ForeignKey(
#         Sensor.id, ondelete='CASCADE'))
#
#
# class SensorMonthly(Base):
#     __tablename__ = 'sensors_monthlytemperaturehumidity'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     temperature = Column(Float)
#     humidity = Column(Float)
#     timestamp = Column(DateTime(timezone=True))
#     asset_id = Column(ForeignKey(
#         Sensor.id, ondelete='CASCADE'))
#
#
# class SensorIAQ(Base):
#     __tablename__ = 'sensors_iaq'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     macid = Column(String(20))
#     lastseen = Column(DateTime(timezone=True))
#     battery = Column(Float)
#     co2 = Column(Float)
#     floor_id = Column(ForeignKey(FloorMap.id, ondelete='CASCADE'))
#     tvoc = Column(Float)
#     x = Column(Float)
#     y = Column(Float)
#
#
# class SensorDailyIAQ(Base):
#     __tablename__ = "sensors_dailyiaq"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     co2 = Column(Float)
#     tvoc = Column(Float)
#     timestamp = Column(DateTime(timezone=True))
#     asset_id = Column(ForeignKey(SensorIAQ.id, ondelete='CASCADE'))
#
#
# class SensorWeeklyIAQ(Base):
#     __tablename__ = "sensors_weeklyiaq"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     co2 = Column(Float)
#     tvoc = Column(Float)
#     timestamp = Column(DateTime(timezone=True))
#     asset_id = Column(ForeignKey(SensorIAQ.id, ondelete='CASCADE'))
#
#
# class SensorMonthlyIAQ(Base):
#     __tablename__ = "sensors_monthyiaq"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     co2 = Column(Float)
#     tvoc = Column(Float)
#     timestamp = Column(DateTime(timezone=True))
#     asset_id = Column(ForeignKey(SensorIAQ.id, ondelete='CASCADE'))
#
#
# class SignalRepeater(Base):
#     __tablename__ = 'signalrepeator_signalrepeator'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     macid = Column(String(20))
#     lastseen = Column(DateTime(timezone=True))
#
#
# class zones_zones(Base):
#     __tablename__ = 'zones_zones'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     x1 = Column(Float)
#     y1 = Column(Float)
#     x2 = Column(Float)
#     y2 = Column(Float)
#     floor = Column(ForeignKey(FloorMap.id, ondelete='CASCADE'))
#
#
# """ RackTracking model: """
#
#
# class RackTracking(Base):
#     __tablename__ = 'zones_racktracking'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     rackid_id = Column(ForeignKey(Rack.id, ondelete='CASCADE'))
#     tagid_id = Column(ForeignKey(Asset.id, ondelete='CASCADE'))
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())
