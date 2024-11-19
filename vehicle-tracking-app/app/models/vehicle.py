from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Location(Base):
    __tablename__ = "locations"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    location_type = Column(String)
    
class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    license_number = Column(Integer, unique=True)
    contact_number = Column(Integer) 
    schedules = relationship("Schedule",back_populates ="driver")
    
class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    start_location = Column(String)
    end_location = Column(String)
    distance = Column(Float)  # Distance in kilometers or miles
    duration = Column(Float) 
    schedules = relationship("Schedule",back_populates ="route")
    
class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)

    vehicle = relationship("Vehicle", back_populates="schedules")
    driver = relationship("Driver", back_populates="schedules")
    route = relationship("Route", back_populates="schedules")
    
    
class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    plate_number = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    
    schedules = relationship("Schedule", back_populates="vehicle")

    def __repr__(self):
        return f"<Vehicle(id={self.id}, name={self.name}, plate_number={self.plate_number}, capacity={self.capacity})>"