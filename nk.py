import os
import re
import sys
import requests
import threading
from src import UI
from time import sleep
from sys import stdout
from clipboard import copy
from bs4 import BeautifulSoup
from selenium import webdriver
from colorama import Fore, Style, init

init(convert=True)

lock = threading.Lock()

def free_print(arg):
    lock.acquire()
    stdout.flush()
    print(arg)
    lock.release()   


def menu():
    os.system('cls')
    os.system('title Nuclear Codez ^| coded by Coffee#7443 ')
    UI.banner()
    UI.start_menu()

    try:
        user_input = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
        print('\n\n')
    except ValueError:
        user_input = 0

    if user_input == 1:
        os.system('cls')
        UI.banner()
        UI.menu2()


        try:
            user_input = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
            print('\n\n')
        except ValueError:
            user_input = 0

        if user_input == 1:
            return 5

        elif user_input == 2:
            return 4

        elif user_input == 3:
            return 3

        elif user_input == 4:
            return 2

        elif user_input == 5:
            return 1
        else:
            return None

if __name__ == '__main__':
    continue_program = True

    m = menu()

    if m == 5:
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

        print(f'{Fore.LIGHTMAGENTA_EX}{pll}{Style.RESET_ALL}')
        sleep(500)

        '''
        for link in soup.find_all('a'):
            ps = link.get('href')
            print(ps)
        '''
    elif m == 4:
        user_input = 0
        while user_input<5:
            os.system('cls')
            UI.banner()
            UI.menu3()

            try:
                user_input = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
                print('\n\n')
            except ValueError:
                user_input = 0

            if user_input == 1:
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

                # Eliminar Número de Página
                plw = pll[0:-1]
                print(plw)

                g = 0
                while 0 == g:
                    os.system('cls')
                    UI.banner()
                    UI.menu4()

                    free_print(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} {plw}')

                    try:
                        free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} {pds}')
                    except:
                        pass

                    ert = int(input(f"{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))

                    if ert == 1:
                        copy(plw)
                    elif ert == 2:
                        try:
                            copy(pds)
                        except:
                            r = requests.get(f'https://nhentai.net/g/{plw}/1')
                            soup = BeautifulSoup(r.content, 'html.parser')
                            elements = soup.find_all('img', {'src': True})
                            pdd = [element['src'] for element in elements]
                            pds = pdd[1]
                            copy(pds)
                            free_print(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} {pds}')
                    elif ert == 3:
                        g = 1
            if user_input == 2:
                g = 0
                while 0 == g:
                    os.system('cls')
                    UI.banner()
                    UI.menu5()

                    try:
                        free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} {pds}')
                    except:
                        pass

                    ert = int(input(f"{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))

                    if ert > 2:
                        try:
                            copy(pds)
                        except:
                            free_print(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Ingresa Nuke:')
                            nfg = int(input(f"{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
                            r = requests.get(f'https://nhentai.net/g/{nfg}/1')
                            soup = BeautifulSoup(r.content, 'html.parser')
                            elements = soup.find_all('img', {'src': True})
                            pdd = [element['src'] for element in elements]
                            pds = pdd[1]
                            free_print(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} {pds}')
                            copy(pds)

                    elif ert == 2:
                        g = 1
            if user_input == 3:
                os.system('cls')
                UI.banner()
                UI.menu7()

                eee = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
                if eee == 1:
                    print(f"{Fore.LIGHTMAGENTA_EX}[WARNING]{Style.RESET_ALL} No pongas muchos números, puede crashear o tardara demasiado. 20 es decente. :3")
                    x = int(input(f"{Fore.LIGHTMAGENTA_EX}[>]{Style.RESET_ALL} Ingresa una cantidad [eg. 3] > "))
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

                        if x % 2 == 0:
                            free_print(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} {plw}')
                        else:
                            free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} {plw}')
                        x -= 1
                        lock.acquire()
                        with open('output/codez.txt', 'a', encoding='UTF-8') as codez:
                            codez.write(plw + '\n')      
                        lock.release()
                    else:
                        pass


    elif m == 3:
        x = 1

        while 0 < x:
            os.system('cls')
            UI.banner()
            UI.menu8()

            try:
                free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} {nuclear}')
            except:
                pass

            efe = int(input(f"\t\t{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))

            if efe > 3:
                try:
                    free_print(f'{Fore.LIGHTMAGENTA_EX}[!]{Style.RESET_ALL} Ingresa Nuke:')
                    nuke = int(input(f"{Fore.LIGHTMAGENTA_EX}[?]{Style.RESET_ALL} > "))
                except:
                    nuke = 0

                if nuke > 0:
                    driver = webdriver.Chrome('C:/Users/ccruz/PycharmProjects/pythontests/pr2/Selenium_py/chromedriver.exe')
                    driver.get(f'https://nhentai.net/g/{nuke}/')

            elif efe == 2:
                driver = webdriver.Chrome('C:/Users/ccruz/PycharmProjects/pythontests/pr2/Selenium_py/chromedriver.exe')
                driver.get('https://nhentai.net/random/')
                url = driver.current_url
                nnnn = url.split('/')
                hhhh = nnnn[4]
                nuclear = f'/g/{hhhh}/'
                copy(hhhh)
                free_print(f'{Fore.LIGHTMAGENTA_EX}[*]{Style.RESET_ALL} {nuclear}')

            elif efe == 3:
                x = 0

    elif m == 2:
        pass

    elif m == 1:
        sys.exit()
    else:
        continue_program = False

