import logging
from logger import watcherlogger

if __name__ == "__main__":
    logger = watcherlogger().Builder().setLogLevel(logging.INFO).setStreamNamePrefix("test_log").getOrCreate()
   
    logger.info({"service_arn":"test","module_name":"app","job_type":"test","src_record_count":100})
