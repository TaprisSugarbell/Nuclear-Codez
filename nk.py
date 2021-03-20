import re
import requests
from bs4 import BeautifulSoup
from clipboard import copy
from selenium import webdriver

elec = 0

while elec<4:
    print('1. Nuk de PP\n2. Usa BeautifulSoup\n3. Usa Selenium\n4. Fin')
    elec = int(input('Ingresa opción - '))

    if elec == 1:
        r = requests.get('https://nhentai.net/')
        soup = BeautifulSoup(r.content, 'html.parser')

        # Consigue todos los href de la página
        elements = soup.find_all('a', {'href': True})
        ps = [element['href'] for element in elements]

        # Devuelve solo los nuke codes
        psp = ps[17:-8]

        # Convierte la lista en texto
        psl = '\n'.join(psp)

        # Quitar /g/{deja los números}/
        pll = re.sub("/|g","",psl).replace("-","")

        print(pll)

        '''
        for link in soup.find_all('a'):
            ps = link.get('href')
            print(ps)
        '''

    elif elec == 2:
        fgh = 0
        while fgh<5:
            print('Que quieres hacer?\n1. Conseguir Nuclear Code\n2. Buscar portada\n3. Random?\n4. Proximamente\n5. Nada')
            fgh = int(input('Ingresa opción - '))
            if fgh == 1:
                r = requests.get('https://nhentai.net/random/')
                soup = BeautifulSoup(r.content, 'html.parser')

                # Consigue todos los href de la página
                '''
                for href in soup.find_all('a',href=True):
                    ps = href.get('href')
                '''
                elements = soup.find_all('a', {'href': True})
                ps = [element['href'] for element in elements]
                # Devuelve solo los nuke codes
                psp = ps[17]

                # Quitar /g/{deja los números}/
                pll = re.sub("/|g","",psp).replace("-","")

                # Eliminar Númer de Página
                plw = pll[0:-1]
                print(plw)
                ert = int(input('1. Copialo\n2. Copia Portada\n3. Menú\n'))
                if ert == 1:
                    copy(plw)
                elif ert ==2:
                    r = requests.get(f'https://nhentai.net/g/{plw}/1')
                    soup = BeautifulSoup(r.content, 'html.parser')
                    elements = soup.find_all('img', {'src': True})
                    pdd = [element['src'] for element in elements]
                    pds = pdd[1]
                    print(pds)
                    copy(pds)
            elif fgh == 2:
                print('Ingresa el Nuke:')
                nfg = input()
                r = requests.get(f'https://nhentai.net/g/{nfg}/1')
                soup = BeautifulSoup(r.content, 'html.parser')
                elements = soup.find_all('img', {'src': True})
                pdd = [element['src'] for element in elements]
                pds = pdd[1]
                print(pds)
                copy(pds)
            elif fgh == 3:
                x = int(input('Cuantos quieres?\nIngresa Cifra - '))
                y = 0
                while y<x:
                    r = requests.get('https://nhentai.net/random/')
                    soup = BeautifulSoup(r.content, 'html.parser')

                    # Consigue todos los href de la página
                    '''
                    for href in soup.find_all('a',href=True):
                        ps = href.get('href')
                    '''
                    elements = soup.find_all('a', {'href': True})
                    ps = [element['href'] for element in elements]
                    # Devuelve solo los nuke codes
                    psp = ps[17]

                    # Quitar /g/{deja los números}/
                    pll = re.sub("/|g","",psp).replace("-","")

                    # Eliminar Númer de Página
                    plw = pll[0:-1]
                    print(plw)
                    x -= 1

            else:
                pass
    elif elec == 3:
        try:
            nuke = int(input('Ingresa Nuke: '))
        except:
            nuke = 0
        if nuke > 0:
            driver = webdriver.Chrome('C:/Users/ccruz/PycharmProjects/pythontests/pr2/Selenium_py/chromedriver.exe')
            driver.get(f'https://nhentai.net/g/{nuke}/')
        else:
            driver = webdriver.Chrome('C:/Users/ccruz/PycharmProjects/pythontests/pr2/Selenium_py/chromedriver.exe')
            driver.get('https://nhentai.net/random/')
            url = driver.current_url
            nnnn = url.split('/')
            hhhh = nnnn[4]
            nuclear = f'/g/{hhhh}/'
            copy(hhhh)
            print(nuclear)

