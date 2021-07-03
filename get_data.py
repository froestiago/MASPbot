from bs4 import BeautifulSoup
import requests as req
import logging
import pickle

logging.basicConfig(level=0)

data = []
             
html = req.get('https://masp.org.br/acervo/busca?author=')     # this link returns the entire archive
soup = BeautifulSoup(html.text, 'lxml')
soup = soup.find('section', class_='container margin-top row') # gets only the part of the page where the art is

artists = soup.find_all('h2', class_='title') # h2 = where the name of the artist is

for artist in artists:    
    work        = artist.find_next('div', class_='col-xs-12 col-md-12 no-padding') # gets the block where the images are
    artist_name = artist.text.rstrip()
    figures     = work.find_all('figure')
    for figure in figures:
        data.append({
        'artist'       : artist_name,
        'website url'  : figure.a.get('href'),
        'image url'    : figure.img.get('src'),
        'title & year' : figure.p.text
        })
    logging.info(f"completed: {artist_name}")

with open("data.pickle","wb") as file:
    pickle.dump(data, file)
    logging.debug("Data saved")