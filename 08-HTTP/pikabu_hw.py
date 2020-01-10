import bs4
import requests


def get_sorted_tags(cookies, x_csrf_token):
    url = 'https://pikabu.ru/'
    # scroll posts until we get new posts, in developers tools->console we can find get request:
    # XHR finished loading: GET "https://pikabu.ru/?twitmode=1&of=v2&page=2&_=1578650632189"
    # url gives us parameters for future scrolling (write them in params dict)
    # when we look for this request in developers tools->network, we get requests headers
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookies,
        'Referer': 'https://pikabu.ru/',
        'Sec - fetch - mode': 'cors',
        'Sec-fetch-site': 'same-origin',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 79.0.3945.117 Safari / 537.36',
        'x-csrf-token': x_csrf_token,
        'x-requested-with': 'XMLHttpRequest'
        }
    params = {'twitmode': 1, 'of': 'v2', 'page': 2, '_': '1578650632189'}

    session = requests.Session()

    # for home page we use BeautifulSoup to parse and find_all to get only tags for each post
    welcome_page = session.get(url, headers=headers).text
    parsed = bs4.BeautifulSoup(welcome_page, 'html.parser')
    story_tags = parsed.find_all('div', 'story__tags tags')

    # parse other posts
    # we use get request with params firstly(page is 2) then we add 1 to page every turn of the loop
    # we do it until we reach 100 posts
    while len(story_tags) < 100:
        new_page = session.get(url, params=params, headers=headers).json()
        params['page'] += 1
        data = new_page['data']['stories']
        for story in [x['html'] for x in data]:
            if len(story_tags) < 100:
                new_page_parsed = bs4.BeautifulSoup(story, 'html.parser')
                story_tags.append(new_page_parsed.find('div', 'story__tags tags'))

    # get tags out of story_tags list and sort them
    tags = []
    sorted_tags = []
    for item in story_tags:
        for tag in item:
            try:
                tags.append(tag.text)
            except AttributeError:
                pass
    for item in set(tags):
        sorted_tags.append((item, tags.count(item)))
    sorted_tags = sorted(sorted_tags, key=lambda x: x[1], reverse=True)
    return sorted_tags


if __name__ == '__main__':
    result = get_sorted_tags(input('Enter your cookies please: '), input('Enter your x-csrf token please: '))
    print('Most popular tags out of 100 of your posts: ')
    for tag_name, count in result[0:10]:
        print(f'{tag_name}:{count}')
