from config.logger import get_logger

logger = get_logger(__name__)

def clean_data(data):
    try:
        logger.info("Cleaning data: Removing NaN values and duplicates.")
        cleaned_data = data.dropna().drop_duplicates()
        logger.info(f"Data cleaned: {len(cleaned_data)} rows remaining.")
        return cleaned_data
    except Exception as e:
        logger.error(f"Data cleaning failed: {e}")
        raise
