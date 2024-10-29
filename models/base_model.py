#!/usr/bin/python3
"""Creates Base class with common methods/attributes for other classess"""
import uuid
from datetime import datetime as datetime


class BaseModel:
    def __init__(self):
        """Initializes public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """Prints a string rep of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with current datetime"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Returns dict with all key/values of __dict__ of the instance"""
        instance_dict = self.__dict__
        modified_dict = instance_dict.copy()
        modified_dict["__class__"] = self.__class__.__name__
        modified_dict = {
                "created_at.isoformat()": instance_dict["created_at"],
                "updated_at.isoformat()": instance_dict["updated_at"]
                }
        return modified_dict
