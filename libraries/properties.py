import os
from dotenv import load_dotenv

load_dotenv()


def get_property(property_name):
    property_item = os.getenv(property_name)
    return property_item
