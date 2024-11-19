from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum as PyEnum

# Role Enum
class RoleChoicesEnum(str, PyEnum):
    ADMIN = "admin"
    DRIVER = "driver"
    SCHEDULER = "scheduler"
    VIEWER = "viewer"
    PASSENGER = "passenger"

# User Models
class UserBase(BaseModel):
    username: str
    email: str
    role: RoleChoicesEnum

class UserResponse(BaseModel):
    id: int
    message: str
    username: str
    email: str
    role: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirmPassword: str
    role: str
    created_at: Optional[datetime] = datetime.now()

class UserRead(UserBase):
    id: int

class ProfileRead(BaseModel):
    user: UserRead

# Location Models
class LocationBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    location_type: str

class LocationCreate(LocationBase):
    pass

class LocationRead(LocationBase):
    id: int

    class Config:
        form_attributes = True

# Driver Models
class DriverBase(BaseModel):
    name: str
    license_number: int
    contact_number: int

class DriverCreate(DriverBase):
    pass

class DriverRead(DriverBase):
    id: int

    class Config:
        form_attributes = True

class DriverResponse(BaseModel):
    name: str
    license_number: str
    contact_number: str
    message: str

    class Config:
        form_attributes = True

# Route Models
class RouteBase(BaseModel):
    start_location: str
    end_location: str
    distance: float
    duration: float

class RouteCreate(RouteBase):
    pass

class RouteRead(RouteBase):
    id: int

    class Config:
        form_attributes = True

# Schedule Models
class ScheduleBase(BaseModel):
    vehicle_id: int
    driver_id: int
    route_id: int
    departure_time: datetime
    arrival_time: datetime

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleRead(ScheduleBase):
    id: int

    class Config:
        form_attributes = True

class ScheduleUpdate(ScheduleBase):
    pass

# Vehicle Models
class VehicleBase(BaseModel):
    name: str
    plate_number: str
    capacity: int

class VehicleCreate(VehicleBase):
    pass
    class Config:
        orm_mode = True

class VehicleRead(VehicleBase):
    id: int

    class Config:
        form_attributes = True

class VehicleUpdate(VehicleBase):
    name: Optional[str] = None
    plate_number: Optional[str] = None
    capacity: Optional[int] = None
    
    class Config:
        orm_mode = True  
