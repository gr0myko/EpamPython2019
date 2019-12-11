# 1. Rarser/dumper json


def parse_to_list(data: str):
    wine_list = []
    for wine_str in data.split('}, {'):
        wine_param = wine_str.split(', "')
        wine_dict = {}
        for param in wine_param:
            param = param.replace('"', '').replace('[{', '')
            param = param.split(': ')
            if param[1].isdigit():
                param[1] = int(param[1])
            elif param[1] == 'null':
                param[1] = None
            wine_dict[param[0]] = param[1]
        wine_list.append(wine_dict)
    return wine_list


def dumper(wine_info):
    wine_info = str(wine_info)
    wine_info = wine_info.replace('None', 'null')
    return wine_info


# 2. Общий файл winedata_full

with open('winedata_1.json') as first_file, \
     open('winedata_2.json') as second_file:
    first_data = first_file.read()
    second_data = second_file.read()
    winelist_1 = parse_to_list(first_data)
    winelist_2 = parse_to_list(second_data)

# Убрать дупликаты
winelist_1_2 = winelist_1 + winelist_2
wine_unique = set()
winedata_full = []
for wine_d in winelist_1_2:
    wine_tuple = tuple(wine_d.items())
    if wine_tuple not in wine_unique:
        wine_unique.add(wine_tuple)
        winedata_full.append(wine_d)

# Отсортировать по цене, в случае коллизий - по сорту
winedata_full = sorted(winedata_full,
                       key=lambda z: -1 * float('inf')
                       if z['price'] is None else z['price'],
                       reverse=True)


# Записать в файл winedata_full.json
with open('winedata_full.json', 'w') as full_wine:
    winedata = dumper(winedata_full)
    full_wine.write(winedata)


# 3. Статистика
'''
gewurztraminer = [d for d in winedata_full
                  if d['variety'] == 'Gew\\u00fcrztraminer'
                  and 'Gewurztraminer' in d['title']]
gewürztraminer = [d for d in winedata_full
                  if d['variety'] == 'Gew\\u00fcrztraminer'
                  and 'Gew\\u00fcrztraminer' in d['title']]
riesling = [d for d in winedata_full if d['variety'] == 'Riesling']
merlot = [d for d in winedata_full if d['variety'] == 'Merlot']
madera = [d for d in winedata_full if d['variety'] == 'Madeira Blend']
tempranillo = [d for d in winedata_full if d['variety'] == 'Tempranillo']
red_blend = [d for d in winedata_full if d['variety'] == 'Red Blend']
varieties = [gewurztraminer, gewürztraminer, riesling,
             merlot, madera, tempranillo, red_blend]
'''
varieties_dict = {'Gewurztraminer': [d for d in winedata_full
                                     if d['variety'] == 'Gew\\u00fcrztraminer'
                                     and 'Gewurztraminer' in d['title']],
                  'Gewürztraminer': [d for d in winedata_full
                                     if d['variety'] == 'Gew\\u00fcrztraminer'
                                     and 'Gew\\u00fcrztraminer' in d['title']],
                  'Riesling': [d for d in winedata_full
                               if d['variety'] == 'Riesling'],
                  'Merlot': [d for d in winedata_full
                             if d['variety'] == 'Merlot'],
                  'Madeira Blend': [d for d in winedata_full
                                    if d['variety'] == 'Madeira Blend'],
                  'Tempranillo': [d for d in winedata_full
                                  if d['variety'] == 'Tempranillo'],
                  'Red Blend': [d for d in winedata_full
                                if d['variety'] == 'Red Blend']}
varieties_stat = {}
for name, variety_list in varieties_dict.items():

    stat = {'avarege_price': sum(d['price'] for d in variety_list
                                 if d['price'] is not None)/len(variety_list),
            'min_price': min(d['price'] for d in variety_list
                             if d['price'] is not None),
            'max_price': max(d['price'] for d in variety_list
                             if d['price'] is not None)}
    regions_dict = {}
    for w in variety_list:
        for region in ('region_1', 'region_2'):
            if w[region] is not None:
                if w[region] not in regions_dict:
                    regions_dict[w[region]] = 1
                else:
                    regions_dict[w[region]] += 1
    stat['most_common_region'] = max(regions_dict, key=regions_dict.get)
    countries_dict = {}
    for w in variety_list:
        if w['country'] not in countries_dict:
            countries_dict[w['country']] = 1
        else:
            countries_dict[w['country']] += 1
    stat['most_common_country'] = max(countries_dict, key=countries_dict.get)
    stat['avarege_score'] = sum(d['points'] for d in variety_list if d['points'] is not None)/len(variety_list)
    varieties_stat[name] = stat

price_score = ['price', 'points']
most_expensive_wine = []
cheapest_wine = []
highest_score = []
lowest_score = []

for parameter in price_score:
    max_parameter = max([d[parameter] for d in winedata_full if d[parameter] is not None])
    for d in [{d['title']: d[parameter]} for d in winedata_full]:
        for title, val in d.items():
            if parameter == 'price':
                if val == max_parameter:
                    most_expensive_wine.append(title)
            else:
                if val == max_parameter:
                    highest_score.append(title)
    min_parameter = min([d[parameter] for d in winedata_full
                         if d[parameter] is not None])
    for d in [{d['title']: d[parameter]} for d in winedata_full]:
        for title, val in d.items():
            if parameter == 'price':
                if val == min_parameter:
                    cheapest_wine.append(title)
            else:
                if val == min_parameter:
                    lowest_score.append(title)

comentator_dict = {}
countries = set()
for wine in winedata_full:
    if wine['taster_name'] is not None:
        if wine['taster_name'] not in comentator_dict:
            comentator_dict[wine['taster_name']] = 1
        else:
            comentator_dict[wine['taster_name']] += 1
    if wine['taster_name'] is not None:
        if wine['country'] not in countries:
            countries.add(wine['country'])
most_active_commentator = max(comentator_dict,
                              key=lambda x: comentator_dict[x])

avg_prices = {}
avg_scores = {}
for country in countries:
    winedata_country = [d for d in winedata_full if d['country'] == country]
    avg_prices[country] = sum(d['price'] for d in winedata_country
                              if d['price'] is not None)/len(winedata_country)
    avg_scores[country] = sum(d['points'] for d in winedata_country
                              if d['points'] is not None)/len(winedata_country)
most_expensive_country = max(avg_prices, key=lambda x: avg_prices[x])
cheapest_country = min(avg_prices, key=lambda x: avg_prices[x])
most_rated_country = max(avg_scores, key=lambda x: avg_scores[x])
underrated_country = min(avg_scores, key=lambda x: avg_scores[x])

stats_total = {"wine": varieties_stat,
               "most_expensive_wine": most_expensive_wine,
               "cheapest_wine": cheapest_wine,
               "highest_score": highest_score,
               "lowest_score": lowest_score,
               "most_expensive_country": most_expensive_country,
               "cheapest_country": cheapest_country,
               "most_rated_country": most_rated_country,
               "underrated_country": underrated_country}
stats = {"statistics": stats_total}

with open('stats.json', 'w', encoding='utf-8') as stats_json:
    stats = dumper(stats)
    stats_json.write(stats)
