import pandas
import pearson as p

# historical data stocks from https://www.nasdaq.com/market-activity/stocks


def get_daily_opening_lists(data: "Input in pandas format", year: int):
    """Gets the column index of the year specified data.
    The data should be in dollar and from the site in the comments above.
    Returns daily opening data for the year specified in a list format
    The Input should be pandas format and the year should be all four digits.

    If its more... Nice that you use this shill program still?^^"""
    index_list = []

    for i in range(len(data)):
        if data["Date"][i][-4:] == str(year):
            index_list.append(i)

    daily_opening_data = data.loc[index_list[0]:index_list[-1], " Open":" Open"]
    daily_opening_data_list = []

    for i in daily_opening_data[" Open"]:
        value = str(i).strip()
        value = value.replace("$", "")
        daily_opening_data_list.append(float(value))

    return daily_opening_data_list


# Read out the data of the csv files with pandas
data_apple = pandas.read_csv("HistoricalQuotesApple.csv")
data_fb = pandas.read_csv("HistoricalQuotesFB.csv")
data_db = pandas.read_csv("HistoricalQuotesDB.csv")

# Convert it into opening data of 2019
data_fb_2019_list = get_daily_opening_lists(data_fb, 2019)
data_db_2019_list = get_daily_opening_lists(data_db, 2019)
data_apple_2019_list = get_daily_opening_lists(data_apple, 2019)

print(p.correlation_mat(data_apple_2019_list, data_fb_2019_list))
print(p.pearson_coefficient(data_apple_2019_list, data_fb_2019_list))

print(p.correlation_mat(data_apple_2019_list, data_db_2019_list))
print(p.pearson_coefficient(data_apple_2019_list, data_db_2019_list))