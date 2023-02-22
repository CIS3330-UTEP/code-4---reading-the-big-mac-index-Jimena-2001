#This assignment made me cry. PS: Have a good weekend!!

import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    country_code_value = country_code.upper()
    query = (f"iso_a3 == '{country_code_value}' and date >='{year}-01-01' and date < '{year}-12-31'")
    year_of_country_df = df.query(query)
    outcome = round(year_of_country_df['dollar_price'].mean(),2)
    return outcome

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    country_code = country_code.upper()
    query = (f"iso_a3 == '{country_code}'")
    country_inf_df = df.query(query)
    outcome = round(country_inf_df['dollar_price'].mean(),2)
    return outcome

def get_the_cheapest_big_mac_price_by_year(year):
        df = pd.read_csv(big_mac_file)
        query = (f"date >='{year}-01-01' and date < '{year}-12-31'")
        year_inf_df = df.query(query)
        year_inf = round(year_inf_df['dollar_price'].min(),2)
        min_value = year_inf_df['dollar_price'].idxmin()
        idx_min_value = year_inf_df.loc[min_value]
        out_ch = f"{idx_min_value['name']}({idx_min_value['iso_a3']}): ${round(idx_min_value['dollar_price'],2)}"
        return out_ch        


def get_the_most_expensive_big_mac_price_by_year(year):
        df = pd.read_csv(big_mac_file)
        query = (f"date >='{year}-01-01' and date < '{year}-12-31'")
        year_inf_df = df.query(query)
        year_inf = round(year_inf_df['dollar_price'].max(),2)
        max_value = year_inf_df['dollar_price'].idxmax()
        idx_max_value = year_inf_df.loc[max_value]
        out_ch = f"{idx_max_value['name']}({idx_max_value['iso_a3']}): ${round(idx_max_value['dollar_price'],2)}"
        return out_ch 

if __name__ == "__main__":
    print(get_big_mac_price_by_year("2003","CHL"))
    print(get_big_mac_price_by_country("CHL"))
    print(get_the_cheapest_big_mac_price_by_year("2003"))
    print(get_the_most_expensive_big_mac_price_by_year("2003"))
