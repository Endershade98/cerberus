# infrastructure/logging.py

import logging
from logging.handlers import RotatingFileHandler
import sys
from django.conf import settings

class Logger:
    _loggers = {}

    @classmethod
    def get_logger(cls, name: str):
        """
        Restituisce un logger singleton per ogni nome.
        """
        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)

        # Evita duplicazioni se il logger è già configurato
        if not logger.hasHandlers():
            # Livello dinamico da settings
            level_name = getattr(settings, "LOG_LEVEL", "INFO")
            logger.setLevel(getattr(logging, level_name.upper(), logging.INFO))

            # Console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(getattr(logging, level_name.upper(), logging.INFO))
            console_formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

            # File handler con rotazione
            file_handler = RotatingFileHandler(
                getattr(settings, "LOG_FILE", "cerberus.log"),
                maxBytes=5*1024*1024,  # 5 MB
                backupCount=3
            )
            file_handler.setLevel(getattr(logging, level_name.upper(), logging.INFO))
            file_formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            # Evita propagazione ai logger root
            logger.propagate = False

        cls._loggers[name] = logger
        return logger