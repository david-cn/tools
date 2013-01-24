#coding:utf-8

import logging
import logging.handlers
import datetime

class CLogger(object):

    s_logger = None

    @staticmethod
    def instance():
        if not CLogger.s_logger:
            CLogger.s_logger = CLogger()
        return CLogger.s_logger

    def __init__(self):
        self.m_logger = logging.getLogger()
        handler = logging.handlers.TimedRotatingFileHandler('GameDataSpy.log', 'D')
        self.m_logger.addHandler(handler)
        import sys
        handler = logging.StreamHandler(sys.stdout)
        self.m_logger.addHandler(handler)
        self.m_logger.setLevel(logging.NOTSET)

    def debug(self, s):
        now = datetime.datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.m_logger.debug('[%s DEBUG] %s' % (time_string, s))

    def error(self, s):
        now = datetime.datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.m_logger.error('[%s ERROR] %s' % (time_string, s))

    def info(self, s):
        now = datetime.datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.m_logger.info('[%s INFO] %s' % (time_string, s))

    def critical(self, s):
        now = datetime.datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.m_logger.critical('[%s CRT] %s' % (time_string, s))
