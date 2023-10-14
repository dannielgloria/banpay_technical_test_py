from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from config.settings import Settings

settings = Settings()
database_url = settings.database_url

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    api_access = relationship("APIAccess", back_populates="user")

class APIAccess(Base):
    __tablename__ = "api_access"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    api_url = Column(String)
    read_access = Column(Boolean, default=False)
    write_access = Column(Boolean, default=False)

    # Relación con el usuario
    user = relationship("User", back_populates="api_access")

# Crear las tablas en la base de datos
def create_tables():
    Base.metadata.create_all(bind=engine)
