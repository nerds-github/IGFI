"""
Author: new92
Github: @new92
InstaFollowV1: Script for increasing the followers of an Instagram account



*********IMPORTANT*********
User's login credentials (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the user's Instagram account
***************************
"""
try:
    import sys
    import platform
    from os import system
    from time import sleep
    import instagrapi
    import os
    from instagrapi import *
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

banner="""
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗░░███╗░░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║░████║░░
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝██╔██║░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░╚═╝██║░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
"""
print(banner)
print("\n")
print("[+] Program for increasing followers on Instagram")
print("\n")
print("[+] Author: new92")
print("[+] Github: @new92")
print("\n")
print("[1] Increase Followers")
print("[2] Exit")
print("\n")
option=int(input("[::] Please enter a number (from the above ones): "))
while option < 1 or option > 2 or option == None:
    print("[!] Invalid number !")
    sleep(1)
    option=int(input("[::] Please enter again the number: "))
if option == 1:
    sleep(1)
    print("[+] The login credentials will not be stored or saved")
    sleep(2)
    print("-"*20+"login".upper()+"-"*20)
    username=str(input("[::] Please enter your username: "))
    while username == None or len(username) > 30:
        print("[!] Invalid username !")
        sleep(1)
        username=str(input("[::] Please enter again your username: "))
    username=username.lower()
    username=username.strip()
    sleep(1)
    password=input("[::] Please enter your password: ")
    while password == None:
        print("[!] Invalid password !")
        sleep(1)
        password=input("[::] Please enter again your password: ")
    password=password.strip()
    sleep(1)
    clnt=instagrapi.Client()
    try:
        login = clnt.login(username,password)
        if login:
            print("[!] Login successful !")
            sleep(1)
            print("[+] Please wait while the program is increasing your followers...")
            sleep(2)
        else:
            print("[!] Login unsuccessful !")
            sleep(1)
            print("[+] Please check the username and/or the password !")
            sleep(2)
            print("[+] Exiting...")
            quit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        quit(0)
    sleep(2)
    print("[+] To end the process enter Ctrl + C")
    sleep(2)
    temp = True
    print("[!] NOTE: Use this program every 2 days in order for your account not to get blocked")
    while temp:
        try:
            clnt.user_follow(173560420)
            print("[+] Following 173560420...")
            sleep(2)
            clnt.user_follow(1436859892)
            print("[+] Following 1436859892...")
            sleep(2)
            clnt.user_follow(18428658)
            print("[+] Following 18428658...")
            sleep(2)
            clnt.user_follow(7719696)
            print("[+] Following 7719696...")
            sleep(2)
            clnt.user_follow(451573056)
            print("[+] Following 451573056...")
            sleep(2)
            clnt.user_follow(247944034)
            print("[+] Following 247944034...")
            sleep(2)
            clnt.user_follow(407964088)
            print("[+] Following 407964088...")
            sleep(2)
            clnt.user_follow(460563723)
            print("[+] Following 460563723...")
            sleep(2)
            clnt.user_follow(6860189)
            print("[+] Following 6860189...")
            sleep(2)
            clnt.user_follow(427553890)
            print("[+] Following 427553890...")
            sleep(2)
            clnt.user_follow(26669533)
            print("[+] Following 26669533...")
            sleep(2)
            clnt.user_follow(4213518589)
            print("[+] Following 4213518589...")
            sleep(2)
            clnt.user_follow(12331195)
            print("[+] Following 12331195...")
            sleep(2)
            clnt.user_follow(28527810)
            print("[+] Following 28527810...")
            sleep(2)
            clnt.user_follow(12281817)
            print("[+] Following 12281817...")
            sleep(2)
            clnt.user_follow(208560325)
            print("[+] Following 208560325...")
            sleep(2)
            clnt.user_follow(145821237)
            print("[+] Following 145821237...")
            sleep(2)
            clnt.user_follow(305701719)
            print("[+] Following 305701719...")
            sleep(2)
            clnt.user_follow(217867189)
            print("[+] Following 217867189...")
            sleep(2)
            clnt.user_follow(20824486)
            print("[+] Following 20824486...")
            sleep(2)
            clnt.user_follow(25025320)
            print("[+] Following 25025320...")
            sleep(2)
            clnt.user_follow(787132)
            print("[+] Following 787132...")
            sleep(2)
            clnt.user_follow(260375673)
            print("[+] Following 260375673...")
            sleep(2)
            clnt.user_follow(290023231)
            print("[+] Following 290023231...")
            sleep(2)
            clnt.user_follow(1269788896)
            print("[+] Following 1269788896...")
            sleep(2)
            clnt.user_follow(29394004)
            print("[+] Following 29394004...")
            sleep(2)
            clnt.user_follow(11830955)
            print("[+] Following 11830955...")
            sleep(2)
            clnt.user_follow(6380930)
            print("[+] Following 6380930...")
            sleep(2)
            clnt.user_follow(2094200507)
            print("[+] Following 2094200507...")
            sleep(2)
            clnt.user_follow(9777455)
            print("[+] Following 9777455...")
            sleep(2)
            clnt.user_follow(204633036)
            print("[+] Following 204633036...")
            sleep(2)
            clnt.user_follow(176618189)
            print("[+] Following 176618189...")
            sleep(2)
            clnt.user_follow(1418652011)
            print("[+] Following 1418652011...")
            sleep(2)
            clnt.user_follow(3439002676)
            print("[+] Following 3439002676...")
            sleep(2)
            clnt.user_unfollow(173560420)
            print("[+] Unfollowing 173560420...")
            sleep(2)
            clnt.user_unfollow(1436859892)
            print("[+] Unfollowing 1436859892...")
            sleep(2)
            clnt.user_unfollow(18428658)
            print("[+] Unfollowing 18428658...")
            sleep(2)
            clnt.user_unfollow(7719696)
            print("[+] Unfollowing 7719696...")
            sleep(2)
            clnt.user_unfollow(451573056)
            print("[+] Unfollowing 451573056...")
            sleep(2)
            clnt.user_unfollow(247944034)
            print("[+] Unfollowing 247944034...")
            sleep(2)
            clnt.user_unfollow(407964088)
            print("[+] Unfollowing 407964088...")
            sleep(2)
            clnt.user_unfollow(460563723)
            print("[+] Unfollowing 460563723...")
            sleep(2)
            clnt.user_unfollow(6860189)
            print("[+] Unfollowing 6860189...")
            sleep(2)
            clnt.user_unfollow(427553890)
            print("[+] Unfollowing 427553890...")
            sleep(2)
            clnt.user_unfollow(26669533)
            print("[+] Unfollowing 26669533...")
            sleep(2)
            clnt.user_unfollow(4213518589)
            print("[+] Unfollowing 4213518589...")
            sleep(2)
            clnt.user_unfollow(12331195)
            print("[+] Unfollowing 12331195...")
            sleep(2)
            clnt.user_unfollow(28527810)
            print("[+] Unfollowing 28527810...")
            sleep(2)
            clnt.user_unfollow(12281817)
            print("[+] Unfollowing 12281817...")
            sleep(2)
            clnt.user_unfollow(208560325)
            print("[+] Unfollowing 208560325...")
            sleep(2)
            clnt.user_unfollow(145821237)
            print("[+] Unfollowing 145821237...")
            sleep(2)
            clnt.user_unfollow(305701719)
            print("[+] Unfollowing 305701719...")
            sleep(2)
            clnt.user_unfollow(217867189)
            print("[+] Unfollowing 217867189...")
            sleep(2)
            clnt.user_unfollow(20824486)
            print("[+] Unfollowing 20824486...")
            sleep(2)
            clnt.user_unfollow(25025320)
            print("[+] Unfollowing 25025320...")
            sleep(2)
            clnt.user_unfollow(787132)
            print("[+] Unfollowing 787132...")
            sleep(2)
            clnt.user_unfollow(260375673)
            print("[+] Unfollowing 260375673...")
            sleep(2)
            clnt.user_unfollow(290023231)
            print("[+] Unfollowing 290023231...")
            sleep(2)
            clnt.user_unfollow(1269788896)
            print("[+] Unfollowing 1269788896...")
            sleep(2)
            clnt.user_unfollow(29394004)
            print("[+] Unfollowing 29394004...")
            sleep(2)
            clnt.user_unfollow(11830955)
            print("[+] Unfollowing 11830955...")
            sleep(2)
            clnt.user_unfollow(6380930)
            print("[+] Unfollowing 6380930...")
            sleep(2)
            clnt.user_unfollow(2094200507)
            print("[+] Unfollowing 2094200507...")
            sleep(2)
            clnt.user_unfollow(9777455)
            print("[+] Unfollowing 9777455...")
            sleep(2)
            clnt.user_unfollow(204633036)
            print("[+] Unfollowing 204633036...")
            sleep(2)
            clnt.user_unfollow(176618189)
            print("[+] Unfollowing 176618189...")
            sleep(2)
            clnt.user_unfollow(1418652011)
            print("[+] Unfollowing 1418652011...")
            sleep(2)
            clnt.user_unfollow(3439002676)
            print("[+] Unfollowing 3439002676...")
            sleep(2)
        except KeyboardInterrupt as key:
            print("[!] Program interrupted by user !")
            sleep(1)
            print("[+] Exiting...")
            quit(0)
else:
    print("[+] Exiting...")
    quit(0)
