# YT: https://www.youtube.com/@user-om8sm3ty3g/

import smtplib, random, os, json, time
from colorama import Fore, init
from email.message import EmailMessage
init()

def main():
        print(f'''{Fore.RED}YT: https://www.youtube.com/@user-om8sm3ty3g/\n░██████╗░███╗░░░███╗░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝░████╗░████║██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
██║░░██╗░██╔████╔██║╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██║░░╚██╗██║╚██╔╝██║░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
╚██████╔╝██║░╚═╝░██║██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝''')
        with open(os.path.join(os.getcwd(), 'accounts.json'), 'r') as f:
            json1 = json.loads(f.read())
            allaccounts=0
            for i in range(len(json1)):
                allaccounts+=1
        choice = int(input(f'GMAIL SPAMMER (Доступно {allaccounts} аккаунтов)\n\n[1] Добавить спам аккаунт Microsoft\n[2] Вывести все доступные аккаунты Microsoft в JSON формате\n[3] Начать спам на почту\nВведите ваше действие:  '))
        if choice == 1:

            login = input('\nВведите логин от аккаунта Microsoft:     ')
            password = input('Введите пароль от аккаунта Microsoft:     ')

            with open(os.path.join(os.getcwd(), 'accounts.json'), 'r') as f:
                json1 = json.loads(f.read())

            allaccs = f'acc{len(json1)}'
            json1[allaccs] = {'login': login, 'password': password}

            with open(os.path.join(os.getcwd(), 'accounts.json'), 'w') as json_file:
                json.dump(json1, json_file, ensure_ascii=False, indent=4)

        if choice == 2:

            with open(os.path.join(os.getcwd(), 'accounts.json'), 'r') as f:
                input(f'\nВсе доступные аккаунты Microsoft в JSON формате: {f.read()}\nНажмите ENTER для продолжения!')

        if choice == 3:

            target = input('\nВведите почту на которую обрушится спам:     ').replace('\n', '').replace('\r', '')
            circles = int(input('Введите количество кругов:     '))
            msg = input('Введите сообщение которое будет отправляться:     ').replace('\n', '').replace('\r', '')
            print('\nСпам был успешно начат!')
            for i in range(circles):
                print(f'\nКруг {i} был начат!\n')

                with open(os.path.join(os.getcwd(), 'accounts.json'), 'r') as f:
                    json1 = json.load(f)

                for i in range(len(json1)):
                    login = json1[f'acc{i}']['login']
                    password = json1[f'acc{i}']['password'] 
                    subject = f"{msg}{random.randint(100,999999)}".replace('\n', '').replace('\r', '')
                    body = f"{msg}{random.randint(100,999999)}".replace('\n', '').replace('\r', '')
                    msg = EmailMessage()
                    msg.set_content(body)
                    msg["Subject"] = subject
                    msg["From"] = login
                    msg["To"] = target
                    try:
                        server = smtplib.SMTP("smtp.office365.com", 587)
                        server.starttls()
                        server.login(login, password)
                        server.send_message(msg)
                        server.quit()
                        print(f"{Fore.GREEN}Письмо успешно отправлено!(Заголовок: {subject}, Текст: {body})")
                    except Exception as e:
                        print(f"{Fore.RED}Ошибка при отправке письма: {e}")
                    time.sleep(1)
    
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
