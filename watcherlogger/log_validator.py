from jsonschema import validate, ValidationError
import json
import logging


schema_data = '''{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "WatcherLogger",
    "description": "A product from logging",
    "type": "object",
     
    "properties": {
       "run_id": {
          "description": "The unique run identifier for a service",
          "type": "string"
       },
       "internal_process_name": {
          "description": "The status description",
          "type": "string"
       }, 
       "internal_process_status": {
          "description": "The status description",
          "type": "string"
       }, 
       "service_arn": {
          "description": "The unique identifier for a service",
          "type": "string"
       },
         
       "module_name": {
          "description": "Name of the module",
          "type": "string"
       },
         
       "start_time": {
            "description": "Start time of job",
            "type": "string"
       },

       "end_time": {
            "description": "End time of job",
            "type": "string"
       },

      "duration": {
            "description": "Duration of the job",
            "type": "string"
       },

       "no_of_records": {
            "description": "Number of records processed",
            "type": "number",
            "minimum": 0
        },

        "status": {
            "description": "Status of job",
            "type": "string"
            },

        "reason": {
            "description": "Reason",
            "type": "string"
        } ,
        
        "user_id": {
            "description": "User ID job trigger",
            "type": "string"
        } ,

        "src_record_count": {
            "description": "Record count in source",
            "type": "number",
            "minimum": 0
        } ,

        "target_record_count": {
            "description": "Record count in target",
            "type": "number",
            "minimum": 0
        } ,

        "src_file_size": {
            "description": "File size in source",
            "type": "number",
            "minimum": 0
        } ,

        "target_file_size": {
            "description": "File size in target",
            "type": "number",
            "minimum": 0
        } ,

        "job_type": {
            "description": "Job Type",
            "type": "string"
        } 
    },
     
    "required": ["run_id", "service_arn", "module_name", "job_type"]
 }'''

logger = logging.getLogger(__name__)
def validator(log_data):
    # with open("resources/config.json") as file:
    #     schema_data = file.read()
    #schema for log from json config under resources/config.json
    schema = json.loads(schema_data)    
    try:
        validate(log_data, schema)
        logger.info("Info: Log ok")
    except Exception as e:
        logger.error("Error: "+str(e))
        raise e
