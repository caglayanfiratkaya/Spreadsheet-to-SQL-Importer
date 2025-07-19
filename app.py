import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SQL Insert Generator",  # Sets the browser tab title and icon
    page_icon="🗃️",                    # Sets the page icon
    layout="wide",                      # Uses wide layout for better display
    initial_sidebar_state="expanded"    # Sidebar is expanded by default
)

# --- CORE FUNCTION ---
def generate_inserts(df, table_name, blank_mode, insert_mode):
    """Generates INSERT statements based on DataFrame content."""
    columns = [f"[{col}]" for col in df.columns]  # Formats column names for SQL
    cols_str = ", ".join(columns)                 # Joins column names for SQL syntax

    def process_value(val):
        # Handles empty/blank values according to user selection
        if pd.isna(val) or str(val).strip() == '':
            return "NULL" if blank_mode == 'NULL' else "''"
        clean_val = str(val).replace("'", "''")   # Escapes single quotes for SQL
        return f"'{clean_val}'"

    if insert_mode == 'MULTI':
        # Generates a single multi-row INSERT statement
        value_rows = [f"({', '.join(map(process_value, row))})" for _, row in df.iterrows()]
        all_values_str = ",\n".join(value_rows)
        return f"INSERT INTO [{table_name}] ({cols_str})\nVALUES\n{all_values_str};"
    else: # SINGLE
        # Generates separate INSERT statements for each row
        inserts = [f"INSERT INTO [{table_name}] ({cols_str}) VALUES ({', '.join(map(process_value, row))});" for _, row in df.iterrows()]
        return "\n".join(inserts)

# --- SESSION STATE INIT ---
if 'df' not in st.session_state:
    st.session_state.df = None  # Stores the uploaded DataFrame
if 'generated_sql' not in st.session_state:
    st.session_state.generated_sql = None  # Stores the generated SQL code

# --- CALLBACK FUNCTION ---
def process_file_on_upload():
    """Runs only when file is uploaded or cleared."""
    st.session_state.generated_sql = None  # Resets generated SQL when file changes
    if st.session_state.get('file_uploader_key'):
        try:
            uploaded_file = st.session_state.file_uploader_key
            # Reads the uploaded file (Excel or CSV) into a DataFrame
            st.session_state.df = pd.read_excel(uploaded_file, sheet_name=0) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"File could not be read: {e}")  # Shows error if file can't be read
            st.session_state.df = None
    else:
        st.session_state.df = None

# --- UI ---
st.title("🗃️ SQL INSERT Generator")  # Main page title

# Sidebar
with st.sidebar:
    col1, col2 = st.columns([0.8, 0.2])  # Sidebar layout: control panel and help
    with col1:
        st.header("Control Panel")        # Sidebar header
    with col2:
        with st.popover("❓", use_container_width=True):
            st.markdown("""
                ### 🗃️ SQL INSERT Generator Assistant
                This tool allows you to convert your Excel and CSV files into SQL `INSERT` statements.

                **How to Use?**
                1.  **Upload a File:** Select a file in supported format (`.xlsx` or `.csv`). After selection, a data preview will appear instantly.
                2.  **Configure Options:** Set the target database type, table name, and other SQL settings.
                3.  **Generate Code:** Click the button to instantly generate your SQL statements.

                **Features:**
                - **Instant Preview:** See the first 5 rows of your uploaded data to verify correctness.
                - **SQL Dialects:** Generate compatible statements for different databases (MS SQL Server, PostgreSQL, MySQL).
                - **Excel Sheets:** For multi-sheet Excel files, a menu appears to select the desired sheet.
                - **Stateful Settings:** Your selections (dialect, insert type, etc.) are remembered until you change the file.
                """)  # Help popover with usage instructions

    uploaded_file = st.file_uploader(
        "**1. Upload Your File**",
        type=['xlsx', 'csv'],              # Accepts Excel and CSV files
        key='file_uploader_key',           # Key for session state
        on_change=process_file_on_upload   # Callback when file is uploaded
    )

    is_file_uploaded = st.session_state.df is not None  # Checks if file is uploaded
    
    # All settings form. This helps preserve state.
    with st.form("settings_form", border=False):
        st.subheader("2. SQL Options")     # Section for SQL options

        # Excel sheet selection
        sheet_name_to_process = None
        if is_file_uploaded and uploaded_file.name.endswith('.xlsx'):
            xls = pd.ExcelFile(uploaded_file)
            if len(xls.sheet_names) > 1:
                sheet_name_to_process = st.selectbox("Select Excel Sheet:", xls.sheet_names)  # Allows sheet selection

        # Other options
        dialect = st.selectbox("Target SQL Dialect:", ['MS SQL Server', 'PostgreSQL', 'MySQL'], disabled=not is_file_uploaded)  # SQL dialect selection
        default_name = os.path.splitext(uploaded_file.name)[0] if uploaded_file else ""  # Default table name from file name
        user_table_name = st.text_input("Table Name:", placeholder=f"Default: {default_name}", disabled=not is_file_uploaded)  # Table name input
        blank_mode = st.radio("Empty cells:", ('Assign as NULL', "Assign as empty string ('')"), horizontal=True, disabled=not is_file_uploaded)  # Handling empty cells
        insert_mode = st.radio("INSERT Type:", ('Separate for each row', 'Combine in one query (Multi-row)'), disabled=not is_file_uploaded)  # Insert statement type
        
        # Form submit button
        generate_button = st.form_submit_button(
            label="Generate SQL Code", 
            type="primary", 
            use_container_width=True, 
            disabled=not is_file_uploaded
        )  # Button to generate SQL code

# Main Screen
st.subheader("Data Preview")  # Section for data preview
if st.session_state.df is not None:
    st.info("The first 5 rows of your uploaded file are shown below for you to verify the content.")  # Info message
    st.dataframe(st.session_state.df.head(), use_container_width=True)  # Shows first 5 rows of uploaded data
else:
    st.info("The first 5 rows of your uploaded file will be shown here for you to verify the content.")  # Info message if no file
    

# Main logic when button is pressed
if generate_button:
    if st.session_state.df is not None:
        with st.spinner("Generating SQL..."):  # Shows spinner while generating SQL
            try:
                # If a different Excel sheet is selected, re-read the data
                df = st.session_state.df
                if sheet_name_to_process and sheet_name_to_process != df.attrs.get('sheet_name', 0):
                     df = pd.read_excel(uploaded_file, sheet_name=sheet_name_to_process)
                
                # FIX: Incorrect SQL generation issue resolved
                table_name = user_table_name.strip() or default_name  # Uses user input or default table name
                st.session_state.generated_sql = generate_inserts(df, table_name, blank_mode, insert_mode)  # Generates SQL
            
            except Exception as e:
                st.error(f"Error occurred while generating SQL: {e}")  # Shows error if SQL generation fails

# Show generated SQL code
if st.session_state.generated_sql:
    st.subheader("Generated INSERT Statements")  # Section for generated SQL
    st.info("📋 Use the button at the top right to copy the code or select all text.")  # Info message
    st.code(st.session_state.generated_sql, language='sql', line_numbers=True)  # Displays generated SQL code
    st.download_button(
        label="Download SQL File (.sql)",
        data=st.session_state.generated_sql,
        file_name=f"{user_table_name.strip() or default_name}.sql",
        mime="text/plain",
        use_container_width=True
    )  # Button to download SQL code as a file