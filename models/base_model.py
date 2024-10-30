#!/usr/bin/python3
"""Creates Base class with common methods/attributes for other classess"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes public instance attributes"""
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dtime_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dtime_obj)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints a string rep of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dict with all key/values of __dict__ of the instance"""
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            # Get the values of datetime object
            if isinstance(value, datetime):
                dictFormat[key] = value.isoformat()
            else:
                dictFormat[key] = value
        return dictFormat
