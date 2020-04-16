from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import requests

# Step1: from Texas Police Department website extract links to
# each prisoner's personal page with their Last Statement
# and write them to links_to_statements.txt

LINKS_TO_STATEMENTS = 'links_to_statements.txt'
url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

tags = soup.find_all('a')
base_url = 'https://www.tdcj.texas.gov/death_row/'

with open(LINKS_TO_STATEMENTS, 'a') as file:
    for t in tags[31:-12:2]:
        t = base_url + t.attrs['href']
        if t != 'https://www.tdcj.texas.gov/death_row/dr_info/no_last_statement.html':
            file.write(t + '\n')


# Step2: function for text extraction from the tag <p> which
# contents prisoner's Last Statement

def get_text(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, features='html.parser')
    tags = soup.find_all('p')
    statement = ''
    for tag in tags[5:]:  # if statement has more than one <p>
        statement += tag.get_text(strip=True)
    return statement.strip()


# Step3: following each link from 'links_to_statements.txt'
# and using get_text() function create 'statements.txt' file
# with all Last Statements as one text

STATEMENTS_FILE_NAME = 'statements.txt'


def follow_links_get_text():
    with open(LINKS_TO_STATEMENTS, 'r') as file:
        links = file.read().splitlines()

    with open(STATEMENTS_FILE_NAME, 'a') as file:
        for link in links:
            statement = get_text(link)
            file.write(statement + '\n')


print(follow_links_get_text())

# Final: we have 'statement.txt' with Last Statements text.
# Would be nice to write some script to upload this text
# automatically to wordclouds.com, for example, to represent
# the data in graphic way
