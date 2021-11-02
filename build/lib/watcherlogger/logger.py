from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import watchtower
import json
import logging
import sys
import os
from datetime import datetime
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from .log_validator import validator


class watcherlogger(object):

    def __init__(self):
        self.__name__ = "watcherlogger"
        self._log_group = "/aws/watchtowerlogger"
        self._log_level = logging.ERROR
        self._stream_name = __name__ +"-"+datetime.now().strftime("%Y%m%D%H%M%S")
        self._logger = logging.getLogger()
        if self._logger.handlers:
            for handler in self._logger.handlers:
                self._logger.removeHandler(handler)
        self._logger = logging.getLogger(__name__)


    def getName(self):
        return self.__name__

    class Builder(object):
        def __init__(self):
            self._watcherlogger = watcherlogger()

        def setStreamNamePrefix(self, stream_name_prefix):
            self._watcherlogger._stream_name = stream_name_prefix+"-"+datetime.now().strftime("%Y%m%d%H%M%S")
            return self
            
        def setLogLevel(self, level):
            self._watcherlogger._log_level = level
            logging.basicConfig( level = level )
            return self

        def getOrCreate(self):
            self._watcherlogger._logger.addHandler(watchtower.CloudWatchLogHandler(log_group=self._watcherlogger._log_group,stream_name=self._watcherlogger._stream_name))
            return self._watcherlogger

    def info(self, data):
        validator(data)
        self._logger.info(data)

    def error(self, data):
        self._logger.error(data)

    def debug(self, data):
        self._logger.debug(data)    

if __name__ == "__main__":
    logger = watcherlogger().Builder().setLogLevel(logging.INFO).setStreamNamePrefix("test_log").getOrCreate()
    print(logger.getName())
    print(logger._stream_name)
    print(logger._log_group)
    
    logger.info({"service_arn":"test","module_name":"app","job_type":"test"})
