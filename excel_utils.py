import pandas as pd

class ExcelProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.sheets = pd.read_excel(filepath, sheet_name=None, header=None)
    
    def list_tables(self):
        return list(self.sheets.keys())
    
    def get_table_row_names(self, table_name):
        df = self.sheets.get(table_name)
        if df is not None:
            return df.iloc[:, 0].dropna().astype(str).tolist()
        else:
            raise ValueError(f"Table '{table_name}' not found")
        
    def calculate_row_sum(self, table_name, row_name):
        df = self.sheets.get(table_name)
        if df is None:
            raise ValueError(f"Table '{table_name}' not found")
        
        row_idx = df[df.iloc[:, 0].astype(str) == row_name].index
        if not row_idx.empty:
            row_values = df.iloc[row_idx[0], 1:]
            numeric_values = pd.to_numeric(row_values, errors='coerce')
            return numeric_values.sum(skipna=True)
        else:
            raise ValueError(f"Row '{row_name}' not found in table '{table_name}'")
        
        