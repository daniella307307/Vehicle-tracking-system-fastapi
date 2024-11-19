from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.models.vehicle import Location, Driver, Route, Schedule, Vehicle  # Ensure Vehicle is imported
from schemas import LocationCreate, LocationRead, DriverCreate, DriverRead, RouteCreate, RouteRead, ScheduleCreate, ScheduleRead,VehicleCreate,VehicleRead,VehicleBase,VehicleUpdate

router = APIRouter()

# Route to create a location
@router.post("/locations/add", response_model=LocationRead)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    db_location = Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# Route to get all locations
@router.get("/locations", response_model=list[LocationRead])
def get_locations(db: Session = Depends(get_db)):
    return db.query(Location).all()

@router.put("/locations/update/{location_id}", response_model=LocationRead)
def update_location(location_id: int, location: LocationCreate, db: Session = Depends(get_db)):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    db_location.start_location = location.start_location
    db_location.end_location = location.end_location
    db_location.distance = location.distance
    db_location.duration = location.duration

    db.commit()
    db.refresh(db_location)
    return db_location

@router.delete("/locations/delete/{location_id}")
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    db.delete(db_location)
    db.commit()
    return {"message": "Location deleted successfully"}



# Route to create a driver

@router.post("/drivers/add", response_model=DriverRead)
def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    new_driver = Driver(
        name=driver.name,
        license_number=driver.license_number,
        contact_number=driver.contact_number
    )
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver
# Route to get all drivers
@router.get("/drivers", response_model=list[DriverRead])
def get_drivers(db: Session = Depends(get_db)):
    return db.query(Driver).all()

@router.put("/drivers/update/{driver_id}", response_model=DriverRead)
def update_driver(driver_id: int, driver: DriverCreate, db: Session = Depends(get_db)):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")

    db_driver.name = driver.name
    db_driver.license_number = driver.license_number
    db_driver.contact_number = driver.contact_number

    db.commit()
    db.refresh(db_driver)
    return db_driver

@router.delete("/drivers/delete/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")

    db.delete(db_driver)
    db.commit()
    return {"message": "Driver deleted successfully"}

# Route to create a route
@router.post("/routes/add", response_model=RouteRead)
def create_route(route: RouteCreate, db: Session = Depends(get_db)):
    db_route = Route(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

# Route to get all routes
@router.get("/routes", response_model=list[RouteRead])
def get_routes(db: Session = Depends(get_db)):
    return db.query(Route).all()


@router.put("/routes/update/{route_id}", response_model=RouteRead)
def update_route(route_id: int, route: RouteCreate, db: Session = Depends(get_db)):
    db_route = db.query(Route).filter(Route.id == route_id).first()
    if db_route is None:
        raise HTTPException(status_code=404, detail="Route not found")

    db_route.start_location = route.start_location
    db_route.end_location = route.end_location
    db_route.distance = route.distance
    db_route.duration = route.duration

    db.commit()
    db.refresh(db_route)
    return db_route

@router.delete("/routes/delete/{route_id}")
def delete_route(route_id: int, db: Session = Depends(get_db)):
    db_route = db.query(Route).filter(Route.id == route_id).first()
    if db_route is None:
        raise HTTPException(status_code=404, detail="Route not found")

    db.delete(db_route)
    db.commit()
    return {"message": "Route deleted successfully"}
# Route to create a schedule
@router.post("/schedules/add", response_model=ScheduleRead)
def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule


@router.get("/schedules", response_model=list[ScheduleRead])
def get_schedules(db: Session = Depends(get_db)):
    return db.query(Schedule).all()

@router.put("/schedules/update/{schedule_id}", response_model=ScheduleRead)
def update_schedule(schedule_id: int, schedule: ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")

    db_schedule.vehicle_id = schedule.vehicle_id
    db_schedule.driver_id = schedule.driver_id
    db_schedule.route_id = schedule.route_id
    db_schedule.departure_time = schedule.departure_time
    db_schedule.arrival_time = schedule.arrival_time

    db.commit()
    db.refresh(db_schedule)
    return db_schedule
@router.delete("/schedules/delete/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")

    db.delete(db_schedule)
    db.commit()
    return {"message": "Schedule deleted successfully"}
# Route to create a vehicle
@router.post("/vehicles/add", response_model=VehicleRead)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = Vehicle(**vehicle.dict())  # Creating the SQLAlchemy model
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle  

@router.get("/vehicles", response_model=list[VehicleRead])
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).all()
    return vehicles  # FastAPI will convert SQLAlchemy models to VehicleRead

# Route to update a vehicle
@router.put("/vehicles/update/{vehicle_id}", response_model=VehicleRead)
def update_vehicle(vehicle_id: int, vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    # Update fields
    db_vehicle.name = vehicle.name
    db_vehicle.plate_number = vehicle.plate_number
    db_vehicle.capacity = vehicle.capacity

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle  # FastAPI will convert this to VehicleRead

# Route to delete a vehicle
@router.delete("/vehicles/delete/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    db_vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    db.delete(db_vehicle)
    db.commit()
    return {"message": "Vehicle deleted successfully"}