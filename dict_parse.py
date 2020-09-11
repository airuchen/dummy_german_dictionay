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

        # The word
        vocabulary = soup.find(class_="word")
        if (vocabulary != None):
            print(vocabulary.text)
            print("-"*10)

        # Gender of the word
        cara = soup.find_all(class_="cara")
        if (cara != None):
            for i in range(len(cara)):
                if (cara[i].text[0] != ""): 
                    print(cara[i].text)
            print("-"*10)

        # variation of the Verb
        verb_variation = soup.find(class_="syno")
        if (verb_variation != None):
            print(verb_variation.text)
            print("-"*10)
        
        # Chinese to German translation
        ch_2_ge = soup.find(class_="cd_explain")
        if(ch_2_ge != None):
            print(ch_2_ge.text.replace(')', ')\n'))
            print("-"*10)

        else:
            # German to Chinese translation
            s = soup.find(class_="expDiv").find_all(class_="exp")
            for i in range(len(s)):
                translation = s[i].get_text()
                application = s[i].next_sibling.next_sibling.next_sibling.next_sibling
                # print('1')
                print(translation.strip().replace('; ', '\n'))
                # print('2')
                # print(application)
                if (application != None and application.name!=None and application != "exp" and application.name != "br") :
                    # print('haha')
                    print("  ", application.text)
                    # print("  ", application.next_sibling.next_sibling.next_sibling.next_sibling.text)
            print("-"*10)


        # 3 example sentense 
        ex = soup.find_all("p", class_="line")
        ex_tr = soup.find_all("p", class_="exp")
        if ( (ex != None) or (ex_tr != None)):
            for i in range(min(3, len(ex))):
                example = ex[i].get_text()
                example_translation = ex[i].next_sibling.get_text()
                print("*", example.strip())
                print(" ", example_translation.strip())
        else:
            print("There's no example.")
            print('\n')
    
    except Exception:
        print("Sorry, there is a error! \n")
    
    finally:
        word = input("\n Enter a word (enter 'q' to exit): ")
