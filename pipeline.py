from scripts.extract import load_file
from scripts.load import upload_to_postgres
from scripts.transform import clean_and_transform_data, clean_location_data
import pandas as pd

df_raw = load_file("data/OneStopElectronics_raw_data.csv")
df_region_data = load_file('data/OneStopElectronics_country_data.csv')
df_region_data_clean = clean_location_data(df_region_data)
df_clean = clean_and_transform_data(df_raw)
merged_df = df_clean.merge(df_region_data_clean, on='COUNTRY_CODE', how='left')
upload_to_postgres(merged_df, 'entire_sales_data_cleaned')

print("Data uploaded successfully")