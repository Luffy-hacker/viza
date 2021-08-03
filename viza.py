import requests
import os
import random
from bs4 import BeautifulSoup as bs
import termcolor

os.system('clear')

lite = """

                                    
$$\    $$\ $$$$$$\ $$$$$$$$\  $$$$$$\  
$$ |   $$ |\_$$  _| \____$$ |$$  __$$\ 
$$ |   $$ |  $$ |      $$  / $$ /  $$ |
\$$\  $$  |  $$ |     $$  /  $$$$$$$$ |
 \$$\$$  /   $$ |    $$  /   $$  __$$ |
  \$$$  /    $$ |   $$  /    $$ |  $$ |
   \$  /   $$$$$$\ $$$$$$$$\ $$ |  $$ |
    \_/    \______|\________|\__|  \__|                                  

"""
contact = """
    [+]Cards Genrator[+]
    [+]instagram : https://instagram/mostafa_xi 
"""

print(termcolor.colored(lite, color="green"))
print(termcolor.colored(contact, color="red"))

print(termcolor.colored("__"*25, color="blue"))
print(" ")

try:
    much = int(input(termcolor.colored("How Many Crads? : ", color="blue")))
    print(" ")
except:
    print(" ")
    print(termcolor.colored("please enter valid number", color="yellow"))
    print(" ")
    exit()

def genrator():
    try:    
        v = 0
        cards = []
        while v < much:
            x = random.randint(1234567891234567,9999999999999999)
            v += 1
            cards.append(x)

        for card in cards:
            cookies = {
                '_gid': 'GA1.2.62077506.1627949991',
                '__asc': '44f4c06a17b09e06ff8f6961aea',
                '__utmb': '32078186',
                '_gat_gtag_UA_535004_1': '1',
                '__utmc': '32078186',
                '__auc': 'd3c3063317b0961086009cc3e11',
                '__gads': 'ID=f85d4c0efa9d6b40-22a254e389c900c2:T=1627949953:RT=1627949953:S=ALNI_MZEBVrCBWRoId1LpuvwORjAkIcuxg',
                '__utma': '32078186.221416814.1627949953.1627949953.1627958307.2',
                '__utmz': '32078186.1627958307.2.2.utmccn=(referral)|utmcsr=courseshome.com|utmcct=|utmcmd=referral',
                '_ga': 'GA1.2.221416814.1627949953',
            }

            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Host': 'www.elfqrin.com',
                'Accept-Language': 'en-us',
                'Accept-Encoding': 'br, gzip, deflate',
                'Origin': 'https://www.elfqrin.com',
                'Referer': 'https://www.elfqrin.com/credit_card_bin_generator.php',
                'Connection': 'keep-alive',
                'Content-Length': '20',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
                'X-Requested-With': 'XMLHttpRequest',
            }

            data = {
            'cci': card
            }

            response = requests.post('https://www.elfqrin.com/discard_bin_q1.php', headers=headers, cookies=cookies, data=data).text
            
            soup = bs(response, 'html.parser')
            
            if "UNKNOWN" in response or "Discover" in response:
                print(termcolor.colored(f"[-] DEAD ===> {card}", color="red"))
                print(" ")

            elif "American Express" in response or "Visa" in response or "MasterCard" in response:
                print(termcolor.colored(f"[+] LIVE ===> {card}", color="green"))
                print(" ")
                
                for i in soup.findAll("table"):
                    result = str(i.td).replace('<td valign="top">'," ").replace("<br/></td>"," ").replace("</a><br/>", " ").replace("<br/>", " ").replace('<a href="//www.elfqrin.com/discard_credit_card_generator.php?mode=generate&amp;qccbin=', " ")
                    print(termcolor.colored("DATA ===> " + result, color="yellow"))
                    print(" ")

                
                dat = open("DATA.txt", "a")
                dat.write(result + '\n')
                
                live = open("LIVE.txt","a")
                live.write(str(card) + '\n')

            else:
                print(response)

    except Exception as e:
        print(e)

genrator()
