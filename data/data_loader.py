import pandas as pd
from config.logger import get_logger

logger = get_logger(__name__)

def load_csv(file_path):
    try:
        logger.info(f"Loading CSV file from {file_path}...")
        data = pd.read_csv(file_path)
        logger.info(f"Successfully loaded {len(data)} rows.")
        return data
    except Exception as e:
        logger.error(f"Failed to load CSV file: {e}")
        raise

def save_csv(dataframe, file_path):
    try:
        logger.info(f"Saving DataFrame to {file_path}...")
        dataframe.to_csv(file_path, index=False)
        logger.info("File saved successfully.")
    except Exception as e:
        logger.error(f"Failed to save CSV file: {e}")
        raise
