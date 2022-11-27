from bs4 import BeautifulSoup
import requests
from time import sleep

def nome_filme(soup):
   achar = soup.find('h1').text
   print('\033[31m'+achar.center(150)+'\033[m')

def info_filme(soup):
   achar = soup.find('p', attrs={'slot':'info','class':'scoreboard__info'}).text
   print('\033[35m'+achar.center(150)+'\033[m')

def diretor(soup):
    achar_diretor = soup.find('span', attrs={'data-qa': 'movie-info-director'})
    if achar_diretor == None:
        achar_diretor_link = soup.find('a', attrs={'data-qa': 'movie-info-director'})
        print('\033[97m\n'+achar_diretor_link.text.center(150)+'\n\033[m')
    else:
        print('\033[97m\n'+achar_diretor.text.center(150)+'\n\033[m')

def sinopse(soup):
    achar_content = soup.find('div', attrs={'data-qa': 'movie-info-synopsis'}).text
    print('\033[36m'+achar_content+'\033[m')

def criticos_audiencia(soup):
    achar_critico = soup.find('a', attrs={'data-qa':'critic-reviews-top-filter'})
    achar_audiencia = soup.find('a', attrs={'data-qa':'critic-reviews-all-filter'})
    if achar_critico != None:
        print('\033[39m'+ 'criticos'.upper() + '\033[m: ' + 'https://www.rottentomatoes.com' + achar_critico.get('href'))
    else:
        print('\033[31m'+ 'não tem critica dos criticos!'.upper() + '\033[m')
    if achar_audiencia != None:
        print('\033[39m' + 'audiencia'.upper() + '\033[m: ' + 'https://www.rottentomatoes.com' + achar_audiencia.get('href'))
    else:
        print('\033[31m'+ 'não tem critica da audiencia!'.upper() + '\033[m')

if __name__ == '__main__':
   base_url = 'https://www.rottentomatoes.com/'

   data = [
       {  'filme' : 'terrifier'
       }, {'filme': 'drishyam_2_2022'
       }, {'filme': 'black_panther_wakanda_forever'
       }, {'filme': 'bad_axe'
       }, {'filme': 'taurus'
       }, {'filme': 'smile_2022'
       }, {'filme': 'all_quiet_on_the_western_front_2022'
       }, {'filme': 'the_great_basin'
       }, {'filme': 'the_godfather'
       }, {'filme': 'the_last_manhunt'
       }, {'filme': 'she_said'
       }, {'filme': 'the_menu'
       }, {'filme': 'the_conjuring'
       }, {'filme': 'one_piece_film_red'
       }, {'filme': 'terrifier_2'
       }, {'filme': 'minions_the_rise_of_gru'
       }, {'filme': 'the_bad_guys_2022'
       }, {'filme': 'neptune_frost'
       }, {'filme': 'paradise_city_2022'
       }, {'filme': 'interstellar_2014'
       }, {'filme': 'star_wars_episode_vii_the_force_awakens'
       }, {'filme': 'mission_impossible_rogue_nation'
       }, {'filme': 'city_of_god'
       }
   ]

   # iteração sobre as páginas do site
   for filme in data:
        url = base_url +'m/' + filme['filme']
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')
        print('\033[96m\n' + 'Pegando informações do filme...\n'+'\033[m'.upper())
        nome_filme(soup)
        info_filme(soup)
        diretor(soup)
        sinopse(soup)
        criticos_audiencia(soup)
        sleep(10)

