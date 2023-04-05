# from MailSenderClass import MailSender
# from time import sleep
# import datetime


# def send_mails(sender, file, subject):
#     print(f"\n  Start sending mails from {file}.txt")

#     with open(f"mails/{file}.txt") as persons:
#         for person in persons:
#             gender, mail, target = person.split(' -> ')

#             print(f"---> Send mail to {target.strip()} - {datetime.datetime.now()}")
#             body = open(f"body/{file}{gender}.txt", 'r', encoding='utf-8').read()
#             sender.send(mail.strip(), subject, body)
#             sleep(60)




# smtp_server = 'serwer2351397.home.pl'
# port = "587"

# server = MailSender(smtp_server, port)

# server.login('arkadiusz.budzicki@wiedza.info.pl', 'Homepl@123')
# send_mails(server, 'psycho', 'Zaproszenie do udziału w projekcie "Psychologia w życiu codziennym"')

# server.login('mateusz.pankowski@wiedza.info.pl', 'Homepl@123')
# send_mails(server, 'bio', 'Zaproszenie do udziału w projekcie "Biotechnologia w życiu codziennym"')

# server.login('joanna.wesolowska@wiedza.info.pl', 'Homepl@123')
# send_mails(server, 'chem', 'Zaproszenie do udziału w projekcie "Chcemia w życiu codziennym"')


