import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ru/okrug_balashiha/cars/cadillac/all/'
HEADER = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", 'accept': 'text/html,application/xhtml+xml,'
                                                                                                                                                         'application/xml;q=0.9,image/avif,'
                                                                                                                                                         'image/webp,image/apng,*/*;q=0.8,'
                                                                                                                                                         'application/signed-exchange;v=b3;q=0.9'}
