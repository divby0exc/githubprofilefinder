import requests
import urllib.request
#webUrl = urllib.request.urlopen(base_url+user) doesnt work
import webbrowser

base_url = "https://github.com/"

user = input("Enter a GitHub user: ")

res = requests.get(base_url+user).status_code

def res_code(code):
    match code:
        case 200:
            return True
        case 404:
            return "No user found"
        case _:
            return code
        
def goto_user(ans):
    match ans:
        case 'y' | 'Y':
            webbrowser.open_new_tab(base_url+user)
        case 'n' | 'N':
            print("Perhaps another time.")

def tie_the_knot():
    
    if res_code(res):
        print("User exists.")
        goto_user(input("Would you like to goto that github acc: Y/N: "))

tie_the_knot()