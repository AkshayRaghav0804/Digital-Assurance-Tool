import streamlit as st
import pandas as pd

# Streamlit UI Layout
st.set_page_config(page_title='Digital Assurance Tool', layout='wide')

# Sidebar for Source Selection
st.sidebar.title("📌 Select External Regulatory Source")
selected_source = st.sidebar.radio("Choose a source:", [
    "GST", "EDPMS/IDPMS", "TRACES / Form 26A", "Income Tax", "EPF"
])

# Right Section - Title and Subheader
st.title("📊 Digital Assurance Tool")
st.subheader("Statement containing compliance of conditions of Regulation 33 of LODR Regulations, 2015")

# Table Data
data = {
    "External Regulatory Information Source": [
        "[GST Portal](https://gst-extraction.streamlit.app/)", "[TRACES Portal](https://tdsrecotool-8ev5hcapsychjewmbncbxs.streamlit.app/)", "TRACES Portal", "EDPMS/IDPMS Report", "EDPMS/IDPMS Report"
    ],
    "Description": [
        "Revenue from operations (Goods and Services)",
        "Form 26 AS (Data updated till date ___)",
        "Total Tax Deducted at source",
        "Export Receivables covered under EDPMS",
        "Import Payables covered under IDPMS"
    ],
    "Amount as per Books of Account": ["", "", "", "", ""],
    "Amount as per External Regulatory Information Source": ["", "", "", "", ""],
    "Date on which the External Regulatory Information source was noted by the auditor/independent practitioner": ["", "", "", "", ""],
    "Reconciling items (C-D)": ["", "", "", "", ""],
    "Management Explanation": ["", "", "", "", ""]
}

df = pd.DataFrame(data)

# Display Table with full width using markdown for clickable links
st.write("### Table")
def make_clickable(val):
    if val.startswith("[") and val.endswith(")"):
        return f'<a href="{val[val.find("(")+1:val.find(")")]}" target="_blank">{val[1:val.find(")")-1]}</a>'
    return val

df = df.applymap(make_clickable)
st.write(df.to_html(escape=False), unsafe_allow_html=True)
