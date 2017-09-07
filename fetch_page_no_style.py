import sys
import re

import requests


def fetch_page(url):
    return requests.get(url).text


def remove_style(text):
    return re.sub(r' style=[\"\'](.*?)[\"\']', '', text)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('No params.')
        sys.exit(1)
    
    link = sys.argv[1]
    page_content = fetch_page(link)
    no_style_page_content = remove_style(page_content)
    print(no_style_page_content)