import streamlit as st
import requests
import json

API_URL = "http://localhost:9090"

st.title("📊 Excel Row Sum App")

st.info("Ensure your Excel file is already loaded in the backend.")

# Step 2: Get list of table names
response = requests.get(f"{API_URL}/list_tables")
if response.status_code == 200:
    table_names = response.json()["tables"]
    table_name = st.selectbox("Select Table (Sheet)", table_names)

    # Step 3: Get list of row names for selected sheet
    # Step 3: Get list of row names for selected sheet
if table_name:
    row_response = requests.get(f"{API_URL}/get_table_details", params={"table_name": table_name})
    if row_response.status_code == 200:
        row_names = row_response.json()["row_names"]  # ✅ Fix here
        row_name = st.selectbox("Select Row", row_names)

        if st.button("Get Row Sum"):
    # Normalize row name before sending
            cleaned_row_name = row_name.strip()

            result = requests.get(f"{API_URL}/row_sum", params={
                "table_name": table_name,
                "row_name": cleaned_row_name
            })

            if result.status_code == 200:
                data = result.json()
                st.success(f"Row Sum for **{data['row_name']}**: `{data['sum']}`")
                
                json_bytes = json.dumps(data, indent=2).encode('utf-8')
                st.download_button(
                    label = "Download JSON",
                    data = json_bytes,
                    file_name=f"{data['row_name'].replace(' ', '_')}_sum.json",
                    mime="application/json"
                )
            else:
                st.error(f"Error: {result.json()}")
else:
    st.error("Could not fetch table names from backend.")
