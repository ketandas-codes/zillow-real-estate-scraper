
import pandas as pd 

row_data = pd.read_csv("zillow_properties_data_clean.csv")
df = row_data.copy()

df = df.drop_duplicates().apply(lambda col: col.str.strip().str.lower()if col.dtype == "object" else col)

"""Cleaning name"""

# split address into parts
addr_split = df["address"].str.split(",", expand=True)
# street & city

df["street"] = addr_split[0].str.strip()
df["city"] = addr_split[1].str.strip()
# state & zip

state_zip = addr_split[2].str.strip().str.split(" ", expand=True)
df["state"] = state_zip[0]
df["zip_code"] = state_zip[1]

# street number & street name
df["street_number"] = df["street"].str.split(" ").str[0]
df["street_name"] = df["street"].str.split(" ").str[1:].str.join(" ")
df["street_number"] = pd.to_numeric(df["street_number"], errors="coerce").astype("Int64")
df["zip_code"] = pd.to_numeric(df["zip_code"], errors="coerce").astype("Int64")


"""Cleaning price"""
df["price_dollar"] =df["price_dollar"].str.replace("$","",regex=False).str.strip()
df["price_dollar"] =df["price_dollar"].str.replace(",","",regex=False).str.strip()
df ["price_dollar"] =pd.to_numeric(df["price_dollar"],errors="coerce")

"""Cleaning beds"""
df["beds"] =pd.to_numeric(df["beds"],errors="coerce")


"""Cleaning bath"""
df["baths"] =pd.to_numeric(df["baths"],errors="coerce")

"""Cleaning sqft"""
df["sqft"] = df["sqft"].str.replace(",","", regex=True)
df["sqft"] =pd.to_numeric(df["sqft"],errors="coerce")



clean_Data = [
    "address",
    "street_number",
    "street_name",
    "city",
    "state",
    "zip_code",
    "price_dollar",
    "beds",
    "baths",
    "sqft"

]

df[clean_Data].to_csv("zillow_properties_clean.csv",index=False)










