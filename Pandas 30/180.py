import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev1'] = logs['num'].shift(1)
    logs['prev2'] = logs['num'].shift(2)

    # Check for 3 consecutive same values
    consecutive = logs[
        (logs['num'] == logs['prev1']) & 
        (logs['num'] == logs['prev2'])
    ]

    # Select distinct numbers that appear 3 times consecutively
    result = consecutive[['num']].drop_duplicates()
    result.columns = ['ConsecutiveNums']

    return result