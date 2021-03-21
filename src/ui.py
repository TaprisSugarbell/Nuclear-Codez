from colorama import Fore, Style, init

init(convert= True)

class UI:
    @classmethod
    def banner(cls):
        logo =f'''{Fore.LIGHTMAGENTA_EX} 
                             ▐ ▄ ▄• ▄▌ ▄▄· ▄▄▌  ▄▄▄ . ▄▄▄· ▄▄▄     ▄▄·       ·▄▄▄▄  ▄▄▄ .·▄▄▄▄•
                            •█▌▐██▪██▌▐█ ▌▪██•  ▀▄.▀·▐█ ▀█ ▀▄ █·  ▐█ ▌▪ ▄█▀▄ ██▪ ██ ▀▄.▀·▪▀·.█▌
                            ▐█▐▐▌█▌▐█▌██ ▄▄██▪  ▐▀▀▪▄▄█▀▀█ ▐▀▀▄   ██ ▄▄▐█▌.▐▌▐█· ▐█▌▐▀▀▪▄▄█▀▀▀•
                            ██▐█▌▐█▄█▌▐███▌▐█▌▐▌▐█▄▄▌▐█ ▪▐▌▐█•█▌  ▐███▌▐█▌.▐▌██. ██ ▐█▄▄▌█▌▪▄█▀
                            ▀▀ █▪ ▀▀▀ ·▀▀▀ .▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀  ·▀▀▀  ▀█▄▀▪▀▀▀▀▀•  ▀▀▀ ·▀▀▀ •
                                                                    by Coffee#7443{Style.RESET_ALL}
        '''
        print(logo)   

    @classmethod
    def start_menu(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                    [1] Start
                                                    [2] Exit 
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu) 

    @classmethod
    def menu2(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                [1] Página Principal
                                                [2] BeautifulSoup 
                                                [3] Selenium 'BETA'
                                                [4] Coming soon
                                                [5] Coming soon
                                                [6] Exit
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu) 

    @classmethod
    def menu3(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                [1] Nuclear Code
                                                [2] Buscar Portada 
                                                [3] Random
                                                [4] Coming soon
                                                [5] Exit
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu)

    @classmethod
    def menu4(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                  [1] Copialo
                                                  [2] Copia Portada
                                                  [3] Atrás
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu)

    @classmethod
    def menu5(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                  [>] Ingresa Nuke
                                                  [2] Atrás
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu)

    @classmethod
    def menu6(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                   [2] Atrás
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu)

    @classmethod
    def menu7(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                [1] Crea .txt
                                                [2] Atrás
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu)

    @classmethod
    def menu8(cls):
        menu =f'''{Fore.LIGHTMAGENTA_EX} 
                                         ╔══════════════════════════════╗
                                                [>] Ingresa Nuke
                                                [2] Enter = Random
                                                [3] Atrás
                                         ╚══════════════════════════════╝    {Style.RESET_ALL}
        '''
        print(menu)
