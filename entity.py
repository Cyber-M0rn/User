from sqlalchemy import Column, Integer, String

from core.database import Base


class Manage(Base):
    __tablename__ = 'Manage'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    path = Column(String, unique=True, index=True)
    status = Column(String, unique=True, index=True)


