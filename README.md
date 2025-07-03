# FastAPI Excel Processor 

This project is a FastAPI-based application designed to process and expose data from an Excel file (`capbudg.xls`) via RESTful API endpoints.

## Features

- Parse and read Excel sheets
- List available tables (sheets)
- Fetch row names from a specified table
- Download JSON response (via Streamlit UI)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/excel-fastapi-processor.git
cd excel-fastapi-processor
```

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Start FastAPI server
uvicorn main:app --reload --port 9090

### 4. Start Streamlit UI 
streamlit run streamlit_app.py

API Endpoints
GET /list_tables
Description: Returns the names of all sheets in the Excel file.

Response:
    {"tables":["CapBudgWS"]}

b. GET /get_table_details
Parameters:
table_name: str (Query parameter specifying the name of the table)
Functionality: This endpoint should return the names of the rows for the selected table. These row names are typically the values found in the first column of that table.
Example: If the user selects the "Initial Investment" table, the API should list the first column values like so:

{"table_name":"CapBudgWS","row_names":["Equity Analysis of a Project","INITIAL INVESTMENT","Initial Investment=","Opportunity cost (if any)=","Lifetime of the investment","Salvage Value at end of project=","Deprec. method(1:St.line;2:DDB)=","Tax Credit (if any )=","Other invest.(non-depreciable)=","WORKING CAPITAL","Initial Investment in Work. Cap=","Working Capital as % of Rev=","Salvageable fraction at end=","GROWTH RATES","Revenues","Fixed Expenses","Default: The fixed expense growth rate is set equal to the growth rate in revenues by default.","INITIAL INVESTMENT","Investment"," - Tax Credit","Net Investment"," + Working Cap"," + Opp. Cost"," + Other invest.","Initial Investment","SALVAGE VALUE","Equipment","Working Capital","OPERATING CASHFLOWS","Lifetime Index","Revenues"," -Var. Expenses"," - Fixed Expenses","EBITDA"," - Depreciation","EBIT"," -Tax","EBIT(1-t)"," + Depreciation"," - ∂ Work. Cap","NATCF","Discount Factor","Discounted CF","Book Value (beginning)","Depreciation","BV(ending)"]}

c. GET /row_sum
Parameters:
table_name: str (Query parameter specifying the name of the table)
row_name: str (Query parameter specifying the name of the row, which must be one of the names returned by /get_table_details)
Functionality: This endpoint should calculate and return the sum of all numerical data points in the specified row of the specified table.
Example: If the row_name is "Tax Credit (if any )=" for a table where this row contains the value 10 (or 10%), the output should be:

{"table_name":"CapBudgWS","row_name":"Initial Investment","sum":62484.0}


#Testing with Postman
Base URL: http://localhost:9090
Use the provided Postman collection: FastAPI-Excel-Postman-Collection.json
Import into Postman and run each request

##Potential Improvements
   - Enable handling multiple Excel files at once 
   - In the Streamlit UI, allow users to filter rows/columns by value range or string match before download.
   - Add a new endpoint for column-wise summary (sum, mean, std) — not just rows.
   - Auto-suggest possible row_name or table_name values to avoid typos (autocomplete).
   - Allow users to download output as CSV, YAML, Excel — not just JSON.
   - Provide a Mini dashbord to track
   - Also can generate and give graphs to the user

##Missed Edge Cases
   - Excel sheets may contain hidden data not visible to users but still parsed — needs detection.
   - Some Excel files may be in non-standard encodings, causing parsing failures.
   - Memory overflows or performance bottlenecks when parsing very large Excel files example more than 50 plus MBs
   - Excel sometimes stores dates as floats — can lead to incorrect parsing.
   - User may upload multiple Excel files with sheets of the same name, causing confusion in the table listing.

