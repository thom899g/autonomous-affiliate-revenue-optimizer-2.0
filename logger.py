import logging
from datetime import datetime

class EcosystemLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Format logs with timestamp and module name
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_operation(self, message):
        """Logs general operations."""
        self.logger.info(message)

    def log_error(self, message, exc=None):
        """Logs errors with optional exception details."""
        if exc:
            self.logger.error(message, exc_info=True)
        else:
            self.logger.error(message)

    def log_performance(self, operation, duration):
        """Logs performance metrics."""
        self.logger.info(f"Operation {operation} completed in {duration:.2f}s")