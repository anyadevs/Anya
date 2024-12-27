import sqlite3
from config.logger import get_logger

logger = get_logger(__name__)

class Storage:
    def __init__(self, db_url):
        try:
            logger.info(f"Connecting to database at {db_url}...")
            self.connection = sqlite3.connect(db_url)
            logger.info("Database connection successful.")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise

    def execute_query(self, query, params=()):
        try:
            with self.connection:
                logger.info(f"Executing query: {query}")
                result = self.connection.execute(query, params)
                logger.info("Query executed successfully.")
                return result
        except Exception as e:
            logger.error(f"Query execution failed: {e}")
            raise

    def close(self):
        logger.info("Closing database connection.")
        self.connection.close()
