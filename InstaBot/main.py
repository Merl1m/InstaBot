# This Tool Let's you to download posts of a public instagram user.
# This Tool is a Menu Driven Program
# Type 'help' to see the available commands
# This Tool is created by [ME]
# This Version is designed for Linux Only

# Import Section
import os
import time
import getpass

from instaloader import Instaloader, Profile

Loader = Instaloader()
mod = Instaloader()
# Variables

prompt = 'InstaBot> '
Active = False

# Functions
def user_stat():
    UserName = str(input("USERNAME: "))
    profile = Profile.from_username(Loader.context, UserName)
    print("---")
    print("USERNAME     : {0}".format(profile.username))
    print("Name         : {0}".format(profile.full_name))
    print("Profile Pic  : {0}".format(profile.profile_pic_url))
    print("Followers    : {0}".format(profile.followers))
    print("External URL : {0}".format(profile.external_url))
    print("Bio          : {0}".format(profile.biography))
    print("Public Story : {0}".format(profile.has_public_story))
    print("Private      : {0}".format(profile.is_private))
    print("Verified     : {0}".format(profile.is_verified))
    print("ID           : {0}".format(profile.userid))
    print("---")

def login():
    global Active
    UserName = str(input("Enter your Instagram username: "))
    PassWord = str(getpass.getpass("Enter your Instagram password: "))
    mod.login(UserName, PassWord)
    Active = True

def get_posts():
    profile = str(input("Enter the Target Username: "))
    Active = True
    Ask = str(input("Do you want to download all posts of user(y/n): "))
    if Ask == 'y':
        Active = False
    mod.download_profile(profile, profile_pic_only=Active)

def Login_Stat():
    if Active == False:
        print('-- Not Logged in --')
    elif Active == True:
        print('-- Logged in --')

def Help():
    Main_Dict = {"login stat":"Shows the Login Status","login":"Helps you login to your account","get posts":"Downloads the post of a target user","q":"stops the bot","clear":"clears the terminal"}
    for syntax, Info in Main_Dict.items():
        print("{0} - {1}".format(syntax, Info))

def Clear():
    os.system('clear')

def Execute_function(function):
    try:
        function()
    except Exception as Error:
        print(Error)

# Main Loop
while True:
    cmd = str(input(prompt))
    if cmd == 'q':
        break

    elif cmd == 'login':
        Execute_function(login)

    elif cmd == 'get posts':
        Execute_function(get_posts)
        time.sleep(5)

    elif cmd == 'login stat':
        Execute_function(Login_Stat)

    elif cmd == 'clear':
        Execute_function(Clear)

    elif cmd == 'help':
        Execute_function(Help)

    elif cmd == 'user stat':
        Execute_function(user_stat)

    elif cmd == '':
        pass

    else:
        print('InstaBot; --> {0} <-- Command Not Found'.format(cmd))

