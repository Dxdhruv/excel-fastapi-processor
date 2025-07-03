from fastapi import FastAPI, HTTPException, Query
from excel_utils import ExcelProcessor
from fastapi import UploadFile, File
import pandas as pd
from fastapi import Query
from fastapi.responses import JSONResponse

app = FastAPI()

processor = ExcelProcessor('capbudg.xls')

loaded_tables = {}

@app.get("/")
def read_root():
    excel_path = 'capbudg.xls'
    try:
        loaded_tables.update(pd.read_excel(excel_path, sheet_name=None))
        print("Excel file loaded successfully.")
    except Exception as e:
        print
    return {"message": "Welcome to the Excel Processor API"}

@app.get("/list_tables")
def list_tables():
    try:
        tables = processor.list_tables()
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    try:
        rows = processor.get_table_row_names(table_name)
        return {"table_name": table_name, "row_names": rows}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    try:
        result = processor.calculate_row_sum(table_name, row_name)
        return {"table_name": table_name, "row_name": row_name, "sum": result}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
