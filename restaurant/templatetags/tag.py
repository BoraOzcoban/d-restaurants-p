from django import template
import numpy as np
import pandas as pd
from numpy.random import randint
register = template.Library()

df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
df = df.fillna(value="No Info")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 0)

@register.simple_tag(name="random")
def random():
    x = randint(0, 125433)
    result = df.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_a")
def city_sort_a():
    result = df[df["City"].str.contains("Amsterdam")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_at")
def city_sort_at():
    result = df[df["City"].str.contains("Athens")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_b")
def city_sort_b():
    result = df[df["City"].str.contains("Barcelona")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_be")
def city_sort_be():
    result = df[df["City"].str.contains("Berlin")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_br")
def city_sort_br():
    result = df[df["City"].str.contains("Bratislava")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_bru")
def city_sort_bru():
    result = df[df["City"].str.contains("Brussels")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_bu")
def city_sort_bu():
    result = df[df["City"].str.contains("Budapest")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_cp")
def city_sort_cp():
    result = df[df["City"].str.contains("Copenhagen")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_du")
def city_sort_du():
    result = df[df["City"].str.contains("Dublin")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_ed")
def city_sort_ed():
    result = df[df["City"].str.contains("Edinburgh")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_ge")
def city_sort_ge():
    result = df[df["City"].str.contains("Geneva")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_ha")
def city_sort_ha():
    result = df[df["City"].str.contains("Hamburg")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_he")
def city_sort_he():
    result = df[df["City"].str.contains("Helsinki")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_kr")
def city_sort_kr():
    result = df[df["City"].str.contains("Krakow")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_li")
def city_sort_li():
    result = df[df["City"].str.contains("Lisbon")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_lj")
def city_sort_lj():
    result = df[df["City"].str.contains("Ljubljana")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_lo")
def city_sort_lo():
    result = df[df["City"].str.contains("London")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_lu")
def city_sort_lu():
    result = df[df["City"].str.contains("Luxembourg")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_ly")
def city_sort_ly():
    result = df[df["City"].str.contains("Lyon")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_ma")
def city_sort_ma():
    result = df[df["City"].str.contains("Madrid")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_mi")
def city_sort_mi():
    result = df[df["City"].str.contains("Milan")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_mu")
def city_sort_mu():
    result = df[df["City"].str.contains("Munich")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_op")
def city_sort_op():
    result = df[df["City"].str.contains("Oporto")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_os")
def city_sort_os():
    result = df[df["City"].str.contains("Oslo")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_pa")
def city_sort_pa():
    result = df[df["City"].str.contains("Paris")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_pr")
def city_sort_pr():
    result = df[df["City"].str.contains("Prague")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_ro")
def city_sort_ro():
    result = df[df["City"].str.contains("Rome")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_st")
def city_sort_st():
    result = df[df["City"].str.contains("Stockholm")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_vi")
def city_sort_vi():
    result = df[df["City"].str.contains("Vienna")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_wr")
def city_sort_wr():
    result = df[df["City"].str.contains("Warsaw")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="city_sort_zr")
def city_sort_zr():
    result = df[df["City"].str.contains("Zurich")]
    y = len(result)
    x = randint(1, y)
    result = result.iloc[x]
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3
@register.simple_tag(name="cuisine_am")
def cuisine_am():
    df2 = df[df["Cuisine Style"].str.contains("American")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_as")
def cuisine_as():
    df2 = df[df["Cuisine Style"].str.contains("Asian" or "Chinese" or "Japanese" or "Thai")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_fr")
def cuisine_fr():
    df2 = df[df["Cuisine Style"].str.contains("French")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_gr")
def cuisine_gr():
    df2 = df[df["Cuisine Style"].str.contains("Greek")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_ind")
def cuisine_ind():
    df2 = df[df["Cuisine Style"].str.contains("Indian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_ita")
def cuisine_ita():
    df2 = df[df["Cuisine Style"].str.contains("Italian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_med")
def cuisine_med():
    df2 = df[df["Cuisine Style"].str.contains("Mediterranean")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_mex")
def cuisine_mex():
    df2 = df[df["Cuisine Style"].str.contains("Mexican")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_mid")
def cuisine_mid():
    df2 = df[df["Cuisine Style"].str.contains("Middle Eastern")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
@register.simple_tag(name="cuisine_tur")
def cuisine_tur():
    df2 = df[df["Cuisine Style"].str.contains("Turkish")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res