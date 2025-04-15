import pandas as pd

def getDataframeSize(players: pd.DataFrame):
    rows, cols = players.shape
    return [rows, cols]