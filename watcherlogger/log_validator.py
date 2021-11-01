from jsonschema import validate, ValidationError
import json
import logging


logger = logging.getLogger(__name__)
def validator(log_data):
    with open("resources/config.json") as file:
        schema_data = file.read()
    #schema for log from json config under resources/config.json
    schema = json.loads(schema_data)    
    try:
        validate(log_data, schema)
        logger.info("Info: Log ok")
    except Exception as e:
        logger.error("Error: "+str(e))
        raise e