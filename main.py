from config.logger import get_logger
from data.data_loader import load_csv
from data.data_cleaner import clean_data
from models.trading_model import TradingModel
from strategies.trading_strategy import apply_strategy

logger = get_logger(__name__)

def main():
    logger.info("Starting AI agent...")
    data = load_csv("data/datasets/example_dataset.csv")
    data = clean_data(data)
    model = TradingModel()
    model.train(data)
    for index, row in data.iterrows():
        apply_strategy(model, row)

if __name__ == "__main__":
    main()
