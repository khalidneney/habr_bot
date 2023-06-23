from bs4 import BeautifulSoup
import requests


def get_orders(q: list, task: str):
    headers = {
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_session_id=eFVEc2tQb25VREYxTmtEdytVVVdCOVNrbnVSckZmYmU0eVU1TC96eksxbUVUMnE5dXMyaGI4WDdmd09PaUNYQmwxdmFIelRzKy9TMW1IbjRWdk1NamlGM3IyM1V4Z2dicFZpeUgyZGpmUjIvcmFTVlVaY2t2ZFpJNU5WSzRNY2tBbExjSm5GdnVxYzZZM2F5YWtBejRSQnBUVmJteEgvRXZmaG9OUVF5c2VZcTBnTWIrT0o3cERjSThCR1YxQWZmNVVvNFBFQUZNNnVjTm5laFlWbWNveGhLZnp3N1JXcjlzb094UUdHOE5jTXE1VUlFS0VObkd3TDIyRnlvUmorYW8rTWZMM3VxUkMzNmpwTTNLV0hhbmR6Q0pWSXYrckNaanhBQ0s0L3JQUER6RUhCMDF1VkpDL1ROQnIwUWRaN2RXbGNZbXR5aXJFRndmV29lVzZ1YzVnPT0tLTZFUG50dXNubTI1czYwOFM4V2JCZVE9PQ%3D%3D--c9e18faa12368d8c43916e478ecad6706c79193d; _ga=GA1.3.1181309917.1686054451; _gid=GA1.3.1927799692.1686054451; _ym_visorc=w; return_to=%2Ftasks%2F502515; __gads=ID=89ff7a01678453c3:T=1686054465:RT=1686056159:S=ALNI_MYJcoFTLMk8PK2x7-IOX_t13T114Q; __gpi=UID=00000c2d14c45e05:T=1686054465:RT=1686056159:S=ALNI_MaI-CE6OlL5RwV9lNw2pb2vpWGZIw; _ga=GA1.2.1181309917.1686054451; _gid=GA1.2.1927799692.1686054451; remember_user_token=BAhbCFsGaQNFVxFJIiIkMmEkMTAkeVQzRTV1R0tuQ3JtLkZ5bWxnMVlXZQY6BkVUSSIXMTY4NjA1NDc0Ni4yMDE0MjY1BjsARg%3D%3D--370ad571d8a0e15b76bf1041f74d2480d002c3c9; _ym_isad=2; habr_uuid=WkpmS1M0L1BRUU1oOXdyTzJJb3dvZHJieWpWWUV4SUlaMHFldmZQMysxajBOeU9sNUJHdEU5RVphd28zUEdHOQ%3D%3D; _ym_d=1686054451; _ym_uid=1686054451801538924',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'freelance.habr.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
        'Accept-Language': 'ru',
        'Referer': 'https://freelance.habr.com/tasks?q=telegram&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other',
        'Connection': 'keep-alive',
    }
    qs = { 
        "development" : "development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other",
        "testing" : "testing_sites,testing_mobile,testing_software",
        "admin" : "admin_servers,admin_network,admin_databases,admin_security,admin_other",
        "design" : "design_sites,design_landings,design_logos,design_illustrations,design_mobile,design_icons,design_polygraphy,design_banners,design_graphics,design_corporate_identity,design_presentations,design_modeling,design_animation,design_photo,design_other"
    }
    # getting right response based on parameters
    response = requests.models.Response()
    result_q = ""
    for i in q:
        result_q += qs[i]
        result_q += ","
    if len(task) != 0 and len(q) != 0:
        response = requests.get(f"https://freelance.habr.com/tasks?q={task}&categories={result_q}")
    elif len(task) != 0 and len(q) == 0:
        response = requests.get(f"https://freelance.habr.com/tasks?q={task}")
    elif len(q) != 0 and len(task) == 0:
        response = requests.get(f"https://freelance.habr.com/tasks?categories={result_q}")
    else:
        response = requests.get(f"https://freelance.habr.com/task?")
    
    # html code getting with soup 
    soup = BeautifulSoup(response.text, "html.parser")
    title_divs = soup.find_all('article', {"class": "task task_list"})
    print(title_divs[1].text)
    title_dict = {}
    # for i in title_divs:
    #     print(i)
        # title_dict[i.text] = i.find('span', {"class": "negotiated_price"}).text
        # if  title_dict[i.text] == None:
        #     title_dict[i.text] = i.find('span', {"class": "count"}).text

    print(title_dict)

if __name__ == '__main__':
    get_orders(['development'], "telegram")