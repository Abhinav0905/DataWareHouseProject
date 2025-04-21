import pandas as pd
from sqlalchemy import create_engine

# 1. Read CSV as UTF-8
df = pd.read_csv(
    "/Users/kumarabhinav/Desktop/Data Warehouse Porfolio projects/sql-data-warehouse-project 2/datasets/source_erp/PX_CAT_G1V2.csv",
    encoding="utf-8"      # or the correct source encoding
)

# 2. Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:password@localhost:3306/DataWarehouse"
    "?charset=utf8mb4"
)

# 3. Append to your bronze table
df.to_sql(
    "bronze_erp_px_cat_g1v2",
    con=engine,
    if_exists="append",
    index=False
)
