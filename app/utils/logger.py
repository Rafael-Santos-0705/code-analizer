import logging
import json
import time
from typing import Optional, List
from datetime import datetime, timezone
#

class ExecutionTime:
    def __init__(self, message: str ="Execution time", logger: Optional[logging.Logger] = None):
        self.message = message
        self.logger = logger if logger else logging.getLogger()

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        execution_time = end_time - self.start_time
        self.logger.warning(f"{self.message}: {execution_time:.5f}s")

class DeduplicationFilter(logging.Filter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.last_log = None

    def filter(self, record):
        current_log = (record.levelno, record.name, record.getMessage())

        if current_log == self.last_log:
            return False

        self.last_log = current_log

        return True

class LoggerFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'name': record.name,
            'level': record.levelname,
            'message': record.getMessage(),
        }

        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)

        return json.dumps(log_record)

class ApplicationLogger(logging.Logger):

    def runtime(self, message: Optional[str] = None):
        return ExecutionTime(message, logger=self)

    @staticmethod
    def configure(names: List[str] = [], level: Optional[str] = None) -> logging.Handler:
        handler = logging.StreamHandler()

        handler.setFormatter(LoggerFormatter())
        handler.addFilter(DeduplicationFilter())
        logging.basicConfig(level=level, handlers=[handler])

        for name in names:
            _logger = logging.getLogger(name)

            if _logger.hasHandlers():
                _logger.handlers.clear()

            _logger.addHandler(handler)

        return handler

logging.setLoggerClass(ApplicationLogger)
