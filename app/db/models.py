from sqlalchemy import Column, Integer, String, Text ,DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    report = Column(Text, nullable=False)
    sources = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

