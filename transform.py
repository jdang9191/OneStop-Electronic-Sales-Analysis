import pandas as pd
import numpy as np

def clean_and_transform_data(df):
    #fill nulls with Unknown instead
    for col in ['MARKETING_CHANNEL', 'ACCOUNT_CREATION_METHOD', 'COUNTRY_CODE', 'CURRENCY']:
        df[col] = df[col].fillna('Unknown')

    df['PURCHASE_TS'] = pd.to_datetime(df['PURCHASE_TS'], errors='coerce')
    df['SHIP_TS'] = pd.to_datetime(df['SHIP_TS'], errors='coerce')
    df['DELIVERY_TS'] = pd.to_datetime(df['DELIVERY_TS'], errors='coerce')
    df['REFUND_TS'] = pd.to_datetime(df['REFUND_TS'], errors='coerce')

    #fill nulls in local price based off usd price
    #can make this more efficient and reduce amt of code
    conversion_rates = {
        'KES': 0.0077, 'BOB': 0.14, 'MMK': 0.0004, 'LKR': 0.0033,
        'GHS': 0.097, 'MAD': 0.11, 'RSD': 0.0096, 'PYG': 0.00013,
        'JOD': 1.41, 'DZD': 0.0076
    }
    mask = df['USD_PRICE'].isna()
    for currency, rate in conversion_rates.items():
        df.loc[mask & (df['CURRENCY'] == currency), 'USD_PRICE'] = df['LOCAL_PRICE'] * rate

    product_name_conversion = {
    '27in"" 4k gaming monitor': '27in 4K gaming monitor'
    }
    for name, real_name in product_name_conversion.items():
        mask = df['PRODUCT_NAME'] == name
        df.loc[mask, 'PRODUCT_NAME'] = real_name


    #feature engineering new cols based on date
    df['MONTH_OF_SALE'] = df['PURCHASE_TS'].dt.month
    df['YEAR_OF_SALE'] = df['PURCHASE_TS'].dt.year

    #feature engineering new cols
    df['TIME_TO_SHIP'] = (df['SHIP_TS'] - df['PURCHASE_TS']).dt.total_seconds()
    df['TIME_TO_DELIVER'] = (df['DELIVERY_TS'] - df['SHIP_TS']).dt.total_seconds()
    df['TIME_TO_REFUND'] = (df['REFUND_TS'] - df['DELIVERY_TS']).dt.total_seconds()


    df['PURCHASE_TS'] = pd.to_datetime(df['PURCHASE_TS'], format='%Y-%m-%d', errors='coerce')
    df['SHIP_TS'] = pd.to_datetime(df['SHIP_TS'], format='%Y-%m-%d', errors='coerce')
    df['DELIVERY_TS'] = pd.to_datetime(df['DELIVERY_TS'], format='%Y-%m-%d', errors='coerce')
    df['REFUND_TS'] = pd.to_datetime(df['REFUND_TS'], format='%Y-%m-%d', errors='coerce')

    return df

def clean_location_data(df):

    df = df[~(df['COUNTRY_CODE'].isna() | (df['REGION'] == 'x'))]

    country_to_region = {
        'AG': 'LATAM', 'AI': 'LATAM','AW': 'LATAM', 'BB': 'LATAM',
        'BJ': 'EMEA', 'BM': 'North America', 'BQ': 'LATAM', 'BS': 'LATAM',
        'BZ': 'LATAM', 'CA': 'North America', 'CW': 'LATAM', 'GD': 'LATAM',
        'GL': 'North America', 'GP': 'LATAM', 'JM': 'LATAM', 'KN': 'LATAM',
        'KY': 'LATAM', 'LC': 'LATAM', 'MQ': 'LATAM', 'PR': 'LATAM',
        'SX': 'LATAM', 'TC': 'LATAM', 'TT': 'LATAM', 'VC': 'LATAM',
        'VG': 'LATAM', 'VI': 'LATAM',
    }
    mask = df['REGION'].isna()
    for country, region in country_to_region.items():
        df.loc[mask & (df['COUNTRY_CODE'] == country), 'REGION'] = region

    return df