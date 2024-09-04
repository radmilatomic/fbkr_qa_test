# import configparser
# import os
#
# def get_property( section, property_name):
#     properties_parser = configparser.ConfigParser()
#     properties_parser.read(os.getenv('AUTOMATION_PROPERTIES'))
#     return properties_parser.get(section, property_name)


import os
from dotenv import load_dotenv

load_dotenv()

def get_property(property_name):

    property_item = os.getenv(property_name)
    return property_item
