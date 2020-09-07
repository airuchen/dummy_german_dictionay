import requests 
from bs4 import BeautifulSoup

import random
import ctypes

word = input("Enter a word (enter 'q' to exit): ")

while word != 'q':
    try:
        address = "https://www.godic.net/dicts/de/" + word
        r = requests.get(url=address)
        soup = BeautifulSoup(r.text, "lxml")
        
        print('\n')

        vocabulary = soup.find(class_="word")
        if (vocabulary != None):
            print(vocabulary.text)
            print("-"*10)

        cara = soup.find(class_="cara")
        if (cara != None):
            print(cara.text)
            print("-"*10)

        verb_variation = soup.find(class_="syno")
        if (verb_variation != None):
            print(verb_variation.text)
            print("-"*10)
        
        ch_2_ge = soup.find(class_="cd_explain")
        if(ch_2_ge != None):
            print(ch_2_ge.text.replace(')', ')\n'))
            print("-"*10)

        else:
            s = soup.find(class_="expDiv").find_all(class_="exp")
            for i in range(len(s)):
                translation = s[i].get_text()
                print(translation.strip().replace('; ', '\n'))
            print("-"*10)


        ex = soup.find_all("p", class_="line")
        ex_tr = soup.find_all("p", class_="exp")
        if ( (ex != None) or (ex_tr != None)):
            for i in range(min(3, len(ex))):
                example = ex[i].get_text()
                example_translation = ex[i].next_sibling.get_text()
                print(example.strip())
                print(example_translation.strip())
        else:
            print("There's no example.")
            print('\n')
    
    except Exception:
        print("Sorry, there is a error! \n")
    
    finally:
        word = input("\n Enter a word (enter 'q' to exit): ")