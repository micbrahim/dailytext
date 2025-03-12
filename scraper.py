import requests
from bs4 import BeautifulSoup
import os
import sys

def wikipedia():
    URL = "https://en.wikipedia.org/wiki/Main_Page"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    for s in str(soup.b).split():
        if s.startswith('href='):
            link = 'https://en.wikipedia.org/' + s[6:-1]

    main_content = soup.find("div", {"class": "mw-body-content"})

    daily = main_content.find_all("p")[0].get_text()
    return f'Daily article: {daily}' + '\n' + f"Find more at {link}"

def send_imessage(phone_number, message_body):
    os.system('osascript msg.applescript {} "{}"'.format( phone_number, message_body ) )

def main():
    if len(sys.argv) != 2:
        print("invalid length")
        exit(1)
    number = int(sys.argv[1])
    if not (isinstance(number, int)):
        print("invalid number")
        exit(1)
    send_imessage(number, wikipedia())
    print("message sent")

if __name__ == "__main__":
    main()

