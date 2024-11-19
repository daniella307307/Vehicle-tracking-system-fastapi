from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()
class RoleChoicesEnum(str,PyEnum):
    ADMIN = "admin"
    DRIVER = "driver"
    SCHEDULER = "scheduler"
    VIEWER = "viewer",
    PASSENGER = "passenger"


class CustomUser(Base):
    __tablename__ = "custom_user"  
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(RoleChoicesEnum, values_callable=lambda obj: [e.value for e in obj]),default=RoleChoicesEnum.VIEWER, nullable=False)
    profile = relationship("Profile", back_populates="user", uselist=False)

    def __repr__(self):
        return f"<CustomUser(id={self.id}, username={self.username}, email={self.email}, role={self.role})>"

class Profile(Base):
    __tablename__ = "profile" 
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("custom_user.id"))
    
    # Define relationship with CustomUser
    user = relationship("CustomUser", back_populates="profile")

    def __repr__(self):
        return f"<Profile(id={self.id}, user_id={self.user_id})>"
