from bs4 import BeautifulSoup
import requests


def get_gender(person):
    person = person.replace('prof.', '').replace('dr', '').replace('hab.', '').replace('inż.', '').replace('mgr', '')
    if person.split()[0].endswith('a'): return 'F'
    return 'M'


def get_targets(url):
    targets = []

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser') 
    
    for target in soup.find_all('h3', class_="field-content"):
        page = target.find('a', href=True)
        page = requests.get('https://old.ug.edu.pl' + page['href'])
        
        soup = BeautifulSoup(page.content, 'html.parser')
        mail = soup.find('div', class_="e-mail")
        if mail is None: continue
        person = soup.find('div', class_="field field-name-title").text.strip()
        mail = mail.find('a').text
        
        data = [get_gender(person), mail, person]
        print(data)
        targets.append(data)

    return targets



def write_to_file(file, data):
    with open(file, 'w') as file:
        for target in data:
            file.write(' -> '.join(target) + '\n')



if __name__ == "__main__":
    url = 'basic url for scrapping'
    target = 'which grupe you want'.replace(' ', '+', -1)

    targets =  get_targets(url + target)
    write_to_file('file.txt', targets)


