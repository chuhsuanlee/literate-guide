from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Event(Base):
    __tablename__ = 'event'

    uuid = Column(String(36), primary_key=True)
    event_type = Column(Integer, nullable=False)
    event_time = Column(DateTime, nullable=False)
    user_email = Column(String(32))
    phone_number = Column(String(32))
    processing_date = Column(Date, nullable=False)


class EventStage(Base):
    __tablename__ = 'event_stage'

    uuid = Column(String(36), primary_key=True)
    event_type = Column(Integer, nullable=False)
    event_time = Column(DateTime, nullable=False)
    user_email = Column(String(32))
    phone_number = Column(String(32))
    processing_date = Column(Date, nullable=False)


json_schema = {
    "title": "event",
    "type": "object",
    "properties": {
        "event_type": {
            "type": "integer"
        },
        "event_time": {
            "type": "string",
            "format": "date-time"
        },
        "data": {
            "type": "object",
            "properties": {
                "user_email": {
                    "type": "string",
                    "format": "email"
                },
                "phone_number": {
                    "type": "string"
                }
            }
        },
        "processing_date": {
            "type": "string",
            "format": "date"
        }
    }
}
