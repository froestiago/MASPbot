import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests as req

data_dict = {'artist' : [],
             'title & year' : [],
             'image url' : [],
             'website url' : [],
             'posted' : []}
             
print('Getting website')
html = req.get('https://masp.org.br/acervo/busca?author=') #this link return the entire archive
print('\t Done!')

print('Getting data')
soup = BeautifulSoup(html.text, 'lxml')
soup = soup.find('section', class_='container margin-top row')  #gets only the part of the page where the art is

for artist_block in soup.find_all('h2', class_='title'):    #h2 = where the name of the artist is
    work_block = artist_block.find_next('div', class_='col-xs-12 col-md-12 no-padding')     #gets the block where the images are
    for figure in work_block.find_all('figure'):    #gets all the images and infos of the works
        data_dict['artist'].append(artist_block.text.rstrip(' '))           #gets the artist name
        data_dict['website url'].append(figure.a.get('href').rstrip(' '))   #gets the link to the website
        data_dict['image url'].append(figure.img.get('src').rstrip(' '))    #gets the link to the image
        data_dict['title & year'].append(figure.p.text.rstrip(' '))         #works title and year

data_dict['posted'] = np.zeros(len(data_dict['artist'])) #0 = not posted; 1 = posted
print('\t Done')

print('Saving file as data.csv')
data = pd.DataFrame.from_dict(data_dict)
data.to_csv('/Users/tiagofroes/Desktop/programming/MASPbot/data.csv')
print('\tDone!')