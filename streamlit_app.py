import pandas as pd
import openpyxl
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pyodbc


def get_data():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=[10.101.3.55];"
        "DATABASE=AWIBI_DM;"
        "UID=-;"
        "PWD=-;"
        "TrustServerCertificate=yes;"
    )
    
    query = "SELECT * FROM CONTRACT_MHU_SKU_BCP_SKEMA_2023_YEARLY"
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df

st.title("Enhanced SQL Server Data Viewer")

df = get_data()
AgGrid(df)  # Interactive Grid

# import pyodbc


# # Set page title and description
# st.set_page_config(page_title="Ecommerce Dataset", page_icon="🎬")
# st.title("🎬 Ecommerce Dataset")
# st.write(
#     """
#     This app visualizes data from a SQL Server datamart interactively using a grid interface.
#     Use the widgets below to filter and customize your view!
#     """
# )

# # SQL Server connection function
# # def connect_to_sql_server():
# #     connection_string = (
# #         "DRIVER={ODBC Driver 17 for SQL Server};"
# #         "SERVER=10.101.3.55;"  # e.g., "localhost" or "192.168.1.100"
# #         "DATABASE=AWIBI_DM;"
# #         "UID=Scriptcase;"
# #         "PWD=Scriptcase;"
# #     )
# #     return pyodbc.connect(connection_string)

# # Fetch data from the SQL Server datamart
# # @st.cache_data
# # def fetch_data(query):
# #     conn = connect_to_sql_server()
# #     df = pd.read_sql(query, conn)
# #     conn.close()
# #     return df

# # # Define the query to fetch data
# # query = "SELECT TOP 1000 * FROM ecommerce"

# # # Display data in the app
# # try:
# #     df = fetch_data(query)
# #     st.write("Data from SQL Server:")
# #     st.dataframe(df)
# # except Exception as e:
# #     st.error(f"Error connecting to SQL Server: {e}")
# #     st.stop()


# @st.cache_data
# def load_data():
#     df = pd.read_excel("data/Ecommerce.xlsx")
#     return df


# df = load_data()

# # Widgets for filtering
# ecommerce_options = df["Ecommerce"].unique().tolist()
# ecommerce = st.multiselect(
#     "E-commerce Platform",
#     ecommerce_options,
#     default=["LAZADA", "SHOPEE"],
# )

# year_min, year_max = int(df["Year"].min()), int(df["Year"].max())
# Year = st.slider("Year", year_min, year_max, (year_max - 1, year_max))

# # month_min, month_max = int(df["Month"].min()), int(df["Month"].max())
# # Month = st.slider("Month", month_min, month_max, (month_max - 1, month_max))

# # Filter the data based on widget input
# df_filtered = df[(df["Ecommerce"].isin(ecommerce)) & (df["Year"].between(Year[0], Year[1])) ]

# # Widget for pivot customization
# st.write("### Customize Pivot Table")
# rows = st.multiselect("Select Rows", df_filtered.columns, default=["Year"])
# columns = st.multiselect("Select Columns", df_filtered.columns, default=["Ecommerce"])
# values = st.selectbox("Select Values", df_filtered.columns, index=list(df_filtered.columns).index("QTY"))
# aggfunc = st.selectbox("Aggregation Function", ["sum", "mean", "count", "max", "min"])

# # Create the pivot table
# if rows and columns and values:
#     pivot_table = df_filtered.pivot_table(
#         index=rows,
#         columns=columns,
#         values=values,
#         aggfunc=aggfunc,
#         fill_value=0,
#     ).reset_index()
# else:
#     pivot_table = df_filtered  # Default to filtered data if no pivot is defined

# # Display the grid using Ag-Grid
# st.write("### Interactive Pivot Table")
# grid_options_builder = GridOptionsBuilder.from_dataframe(pivot_table)
# grid_options_builder.configure_pagination(paginationAutoPageSize=True)
# grid_options_builder.configure_default_column(editable=True, groupable=True)
# grid_options = grid_options_builder.build()

# AgGrid(
#     pivot_table,
#     gridOptions=grid_options,
#     enable_enterprise_modules=True,
#     allow_unsafe_jscode=True,
#     theme="streamlit",
# )

# # Add a download button for the pivot table
# st.write("### Download Data")
# csv_data = pivot_table.to_csv(index=False)
# st.download_button(
#     label="Download as CSV",
#     data=csv_data,
#     file_name="pivot_table.csv",
#     mime="text/csv",
# )
