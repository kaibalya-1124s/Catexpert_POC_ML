import pandas as pd

def load_sales_data(file_path: str) -> pd.DataFrame:
    """Load sales CSV and convert date column."""
    try:
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'])
        df.columns = df.columns.str.lower().str.strip()
        return df
    except Exception as e:
        raise Exception(f"Error loading sales data: {e}")


def load_weather_data(file_path: str) -> pd.DataFrame:
    """Load weather CSV and convert date column."""
    try:
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'])
        df.columns = df.columns.str.lower().str.strip()
        return df
    except Exception as e:
        raise Exception(f"Error loading weather data: {e}")


def load_macro_data(file_path: str) -> pd.DataFrame:
    """Load macro CSV and convert date column."""
    try:
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'])
        df.columns = df.columns.str.lower().str.strip()
        return df
    except Exception as e:
        raise Exception(f"Error loading macro data: {e}")


def merge_datasets(sales_df: pd.DataFrame, weather_df: pd.DataFrame, macro_df: pd.DataFrame, merge_on: list = ['date']) -> pd.DataFrame:
    """
    Merge sales, weather, and macro datasets.
    By default, merges on 'date'. You can also merge on ['date', 'region'].
    """
    try:
        merged = sales_df.merge(weather_df, on=merge_on, how='left')
        merged = merged.merge(macro_df, on=merge_on, how='left')
        print(f"[INFO] Merged dataset shape: {merged.shape}")
        return merged
    except KeyError as e:
        raise KeyError(f"Merge failed — check merge keys: {e}")
