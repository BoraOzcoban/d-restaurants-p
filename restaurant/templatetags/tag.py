from django import template
import numpy as np
import pandas as pd

register = template.Library()
#@register.assignment_tag
#@register.filter(name="random")


@register.simple_tag(name="random")
def random():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    x = np.random.randint(0, 125433)
    result = df.iloc[x]
    #result1 = result[["Name","City","Ranking","Rating","Cuisine Style","Price Range","Reviews"]]
    newline = '\n'
    result1 = (f'''Name: {result["Name"]}   |City: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_a")
def city_sort_a():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Amsterdam")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_at")
def city_sort_at():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Athens")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_b")
def city_sort_b():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Barcelona")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_be")
def city_sort_be():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Berlin")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_br")
def city_sort_br():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Bratislava")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_bru")
def city_sort_bru():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Brussels")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_bu")
def city_sort_bu():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Budapest")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_cp")
def city_sort_cp():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Copenhagen")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_du")
def city_sort_du():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Dublin")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_ed")
def city_sort_ed():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Edinburgh")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_ge")
def city_sort_ge():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Geneva")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_ha")
def city_sort_ha():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Hamburg")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_he")
def city_sort_he():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Helsinki")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_kr")
def city_sort_kr():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Krakow")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_li")
def city_sort_li():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Lisbon")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_lj")
def city_sort_lj():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Ljubljana")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_lo")
def city_sort_lo():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("London")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_lu")
def city_sort_lu():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Luxembourg")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_ly")
def city_sort_ly():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Lyon")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_ma")
def city_sort_ma():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Madrid")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_mi")
def city_sort_mi():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Milan")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_mu")
def city_sort_mu():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Munich")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_op")
def city_sort_op():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Oporto")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_os")
def city_sort_os():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Oslo")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_pa")
def city_sort_pa():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Paris")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_pr")
def city_sort_pr():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Prague")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_ro")
def city_sort_ro():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Rome")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_st")
def city_sort_st():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Stockholm")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_vi")
def city_sort_vi():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Vienna")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_wr")
def city_sort_wr():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Warsaw")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="city_sort_zr")
def city_sort_zr():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    result = df[df["City"].str.contains("Zurich")]
    y = len(result)
    x = np.random.randint(1, y)
    result = result.iloc[x]
    result1 = (f'''Name: {result["Name"]}   |\nCity: {result["City"]}   |\nRanking: {result["Ranking"]}   |Cuisine Style: {result["Cuisine Style"]}   |Reviews: {result["Reviews"]}   |Price Range: {result["Price Range"]}   | ''')
    result2 = result["URL_TA"]
    result3 = f"https://www.tripadvisor.com.tr{result2}"
    return result3


@register.simple_tag(name="cuisine_a")
def cuisine_a():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("African")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_al")
def cuisine_al():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Algerian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_am")
def cuisine_am():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("American")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ar")
def cuisine_ar():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Arabic")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_arg")
def cuisine_arg():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Argentinean")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_as")
def cuisine_as():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Asian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_bar")
def cuisine_bar():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Bar")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_barb")
def cuisine_barb():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Barbecue")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_be")
def cuisine_be():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Beer restaurants")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_bra")
def cuisine_bra():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Brazilian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_brew")
def cuisine_brew():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Brew Pub")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_bri")
def cuisine_bri():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("British")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ca")
def cuisine_ca():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Cafe")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_cau")
def cuisine_cau():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Caucasian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_cea")
def cuisine_cea():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Central Asian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_cee")
def cuisine_cee():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Central European")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ch")
def cuisine_ch():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Chinese")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_con")
def cuisine_con():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Contemporary")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_da")
def cuisine_da():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Danish")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_de")
def cuisine_de():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Deli")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_di")
def cuisine_di():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Diner")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_dut")
def cuisine_dut():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Dutch")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ee")
def cuisine_ee():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Eastern European")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ff")
def cuisine_ff():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Fast Food")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_fr")
def cuisine_fr():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("French")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_fru")
def cuisine_fru():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Fruit parlour")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_fus")
def cuisine_fus():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Fusion")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ga")
def cuisine_gas():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Gastropub")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ger")
def cuisine_ger():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("German")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_gr")
def cuisine_gr():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Greek")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_gri")
def cuisine_gri():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Grill")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_hea")
def cuisine_hea():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Healthy")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_hun")
def cuisine_hun():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Hungarian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ind")
def cuisine_ind():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Indian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_indo")
def cuisine_indo():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Indonesian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_int")
def cuisine_int():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("International")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ir")
def cuisine_ir():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Irish")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_isr")
def cuisine_isr():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Israeli")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_ita")
def cuisine_ita():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Italian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_jap")
def cuisine_jap():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Japanese")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_kor")
def cuisine_kor():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Korean")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_lat")
def cuisine_lat():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Latin")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_latv")
def cuisine_latv():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Latvian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_leb")
def cuisine_leb():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Lebanese")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_med")
def cuisine_med():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Mediterranean")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_mex")
def cuisine_mex():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Mexican")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_mid")
def cuisine_mid():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Middle Eastern")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_mor")
def cuisine_mor():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Moroccan")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_pak")
def cuisine_pak():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Pakistani")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_per")
def cuisine_per():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Persian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_pol")
def cuisine_pol():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Polish")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_por")
def cuisine_por():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Portuguese")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_pub")
def cuisine_pub():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Pub")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_rom")
def cuisine_rom():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Romanian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_rus")
def cuisine_rus():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Russian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_sca")
def cuisine_sca():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Scandinavian")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_soam")
def cuisine_soam():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("South American")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_spa")
def cuisine_spa():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Spanish")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_steak")
def cuisine_steak():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Steakhouse")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_strt")
def cuisine_strt():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Street Food")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_swis")
def cuisine_swis():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Swiss")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_th")
def cuisine_th():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Thai")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_tur")
def cuisine_tur():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Turkish")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_viet")
def cuisine_viet():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Vietnamese")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_wine")
def cuisine_wine():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Wine Bar")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_hal")
def cuisine_hal():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Halal")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_kos")
def cuisine_kos():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Kosher")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res


@register.simple_tag(name="cuisine_car")
def cuisine_car():
    df = pd.read_csv("restaurant/TA_restaurants_curated.csv")
    df = df.fillna(value="No Info")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 0)
    df2 = df[df["Cuisine Style"].str.contains("Caribbean")]
    res = df2.groupby("City").count().sort_values("Name", ascending=False)
    res = res["Name"].to_string()
    return res
