# I wrote this script to make absolutely sure that the Wiki's links are working properly.

import os

def check_link(link: str, filename: str, folder: str):
    # Checks if the link exists
    link = link.replace(f'{folder}/', '')

    if os.path.isfile(link) or '://' in link or not link or '[' in link or ']' in link:
        return True
    else:
        print(f'DEADLINK "{link}" in "{filename}"') 

def list_links(filename: str):
    # Returns list of all links in a file
    links = []

    for link in open(filename).read().split(']('):
        links.append(link.split(')')[0].split('#')[0])

    return links

def check_file(filename: str, folder: str):
    # Checks if all links in a markdown file are working properly
    for link in list_links(filename):
        check_link(link, filename, folder)

    print(f'Checked {filename}')

def check_folder(folder: str):
    # Checks if all links in all markdown files in a folder are working properly
    old_cwd = os.getcwd()
    os.chdir(folder)

    for filename in [f for f in os.listdir() if f.endswith('.md')]:
        check_file(filename, folder)
    os.chdir(old_cwd)

if __name__ == '__main__':
    print('=== GERMAN ===')
    check_folder('de-de')
    print('=== ENGLISH ===')
    check_folder('en-us')