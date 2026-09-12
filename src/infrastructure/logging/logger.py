# infrastructure/logging/logger.py

import logging
import sys
from logging.handlers import RotatingFileHandler
from django.conf import settings


class Logger:
    _loggers = {}

    @classmethod
    def get_logger(cls, name: str):

        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)

        if not logger.hasHandlers():

            level = getattr(settings, "LOG_LEVEL", "INFO").upper()

            logger.setLevel(getattr(logging, level, logging.INFO))

            console = logging.StreamHandler(sys.stdout)
            console.setLevel(getattr(logging, level))
            console.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

            file = RotatingFileHandler(
                getattr(settings, "LOG_FILE", "cerberus.log"),
                maxBytes=5 * 1024 * 1024,
                backupCount=3,
            )
            file.setLevel(getattr(logging, level))
            file.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

            logger.addHandler(console)
            logger.addHandler(file)
            logger.propagate = False

        cls._loggers[name] = logger
        return logger