import requests
import json
from datetime import date, datetime
from bs4 import BeautifulSoup
import subprocess
import pyperclip
"""from profanity_filter import ProfanityFilter"""
import re

WEB = ''

def search(search_val, WEB):
    r = requests.get(url='https://'+WEB+'.wtf/busqueda?q=' + search_val.replace(' ', '+'))
    # print(r.text)
    soup = BeautifulSoup(r.text, "html5lib")
    # print(soup)
    table = soup.find('div', attrs={'class': "w-11/12 mx-auto"})
    link_dict = {}
    for div in table.find_all('div'):
        try:
            link = div.find('a')['href']
            name = div.find('p').text
            page = requests.get(url=link)
            soup_link = BeautifulSoup(page.text, "html5lib")
            div_torrent = soup_link.find('div', attrs={'class': "flex items-center just"})
            try:
                link_torrent = div_torrent.find('a')['href']
                link_dict[name] = link_torrent
            except:
                link_dict[name] = ''
        except:
            link_dict = {}
    return link_dict

WEB = input('Introduce web: ')
user = input('User: ')
while True:
    search_val = str(input('Introduce the search: '))
    result = search(search_val, WEB)
    counter = 1
    if result != {}:
        for entry in result.keys():
            print(str(counter) + ' - ' + entry + ': ' + result[entry])
            counter += 1
        selection = str(input('Select number: '))
        if selection != '0':
            pyperclip.copy(result[list(result.keys())[int(selection)-1]])
            subprocess.Popen(['C:/Users/'+user+'/AppData/Local/Programs/LNV/Stremio-4/stremio.exe', '-new-tab'])
            #subprocess.Popen(['C:/Users/'+user+'/AppData/Local/WebTorrent/WebTorrent.exe'])
