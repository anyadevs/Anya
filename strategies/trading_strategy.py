def apply_strategy(model, market_data):
    try:
        print("Applying trading strategy...")
        action = model.predict(market_data)
        print(f"Action decided: {action}")
        return action
    except Exception as e:
        print(f"Strategy application failed: {e}")
