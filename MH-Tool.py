import datetime , time , os
os.system("clear")
c1 = "\033[0;31m" #red
c2 = "\033[0;32m" #green
c3 = "\033[0;33m" #yellow
c4 = "\033[0;36m" #cyan
print(c2+">>>>>>>>>>>>>>>>>>>>>>>>>>>welcome My Bro<<<<<<<<<<<<<<<<<<<<<<<<")
time.sleep(1)
print(c2+"▄▄▄  ▄▄▄  ▄▄    ▄▄            ▄▄    ▄▄     ▄▄        ▄▄▄▄   ▄▄   ▄▄▄")  
print(c2+"███  ███  ██    ██            ██    ██    ████     ██▀▀▀▀█  ██  ██▀") 
print(c2+"████████  ██    ██            ██    ██    ████    ██▀       ██▄██")   
print(c2+"██ ██ ██  ████████            ████████   ██  ██   ██        █████ By=Mohamed Hesham")  
print(c2+"██ ▀▀ ██  ██    ██            ██    ██   ██████   ██▄       ██  ██▄")    
print(c2+"██    ██  ██    ██            ██    ██  ▄██  ██▄   ██▄▄▄▄█  ██   ██▄")
print(c2+"▀▀    ▀▀  ▀▀    ▀▀            ▀▀    ▀▀  ▀▀    ▀▀     ▀▀▀▀   ▀▀    ▀▀") 
print(c3+"                By=Mohamed Hesham")

password = input("please enter password..: ")
if password == "11111":
    time.sleep(1)
    print("                               ")
    print(c2+"done.....")
else:
    print("password not found....")
    exit()
#########################################################################
style_tool = """
[1]Termux-Tool                    [2]scaning

[3]info gathering                 [4]install metasploit

[5]Dos attack                     [6]about me

              [7]exit MH-Tool.py
"""
os.system("clear")
print(style_tool)
E4 = input("enter number: ")
if E4 == "7":
    exit()
if E4 == "1":
    os.system("clear")
    tools_termux = {
    "1":"git clone https://github.com/Gameye98/Lazymux.git",
    "2":"git clone ttps://github.com/p4kl0nc4t/Spammer-Grab.git",
    "3":"git clone https://github.com/inconshreveable/ngrok.git",
    "4":"git clone https://github.com/cyweb/hammer.git",
    "5":"git clone https://github.com/grafov/hulk.git",
    "6":"git clone https://github.com/derv82/wifite.git",
    "7":"git clone https://github.com/sabri-zaki/EasY_HaCk.git",
    "8":"git clone https://github.com/israelbuitron/wifi-scanner.git",
    "9":"git clone https://github.com/sqlmapproject/sqlmap.git",
    "10":"git clone https://github.com/rajkumardusad/Tool-X.git",
    "11":"git clone https://github.com/emre/fb.py.git",
    "12":"git clone https://github.com/Vairous7x/V7x-Tool.git",
    "13":"git clone https://github.com/byt3bl33d3r/MITMf",
    "14":"git clone https://github.com/No-Name-404/N404-Tool.git",
    "15":"git clone https://github.com/thelinuxchoice/saycheese.git",
    "16":"git clone https://github.com/ciku370/OSIF",
    "17":"git clone https://github.com/TheSpeedX/TBomb.git",
    "18":"git clone https://github.com/RedVirus-Dev/JokerTools.git",
    "19":"git clone https://github.com/Ledear-Hacker/LEDEAR_HACKING",
    "20":"git clone https://github.com/Bl4ckDr460n/HxWhatsApp",
    "21":"git clone https://github.com/remo7777/T-Header",
    "22":"git clone https://github.com/Y-Hak840/Y-Hack",
    "23":"git clone https://github.com/Hider5/Matermuxx",
    "24":"git clone https://github.com/threat9/routersploit",
    "25":"git clone https://github.com/kancotdiq/ipcs",
    "26":"git clone https://github.com/nasirxo/flb2.git",
    "27":"git clone https://github.com/kuburan/txtool.git",
    "28":"git clone https://github.com/nmilosev/termux-fedora.git",
    "29":"git clone https://github.com/joker25000/Devploit",
    "30":"git clone https://github.com/Manisso/fsociety.git",
    "31":"git clone https://github.com/bmegli/wifi-scan.git",
    "32":"git clone https://github.com/SilentGhostX/HT-WPS-Breaker.git",
    "33":"git clone https://github.com/4shadoww/hakkuframework",
    "34":"git clone https://github.com/wi-fi-analyzer/fluxion",
    "35":"git clone https://github.com/Neo-Oli/termux-ubuntu",
    "36":"git clone https://github.com/byt3bl33d3r/MITMf",
    "37":"git clone https://github.com/wi-fi-analyzer/3vilTwinAttacker",
    "38":"git clone https://github.com/SilentGhostX/HT-WPS-Breaker",
    "39":"git clone https://github.com/anthrax3/DarkSploit.git",
    "40":"git clone https://github.com/Ranginang67/DarkFly-Tool.git",
    "41":"git clone https://github.com/Xi4u7/A-Rat.git",
    "42":"git clone https://github.com/beefproject/beef.git",
    "43":"git clone https://github.com/adi1090x/termux-style.git",
    "44":"git clone https://github.com/thelinuxchoice/shellphish",
    "45":"git clone https://github.com/evait-security/weeman",
    "46":"git clone https://github.com/thelinuxchoice/blackeye",
    "47":"git clone https://github.com/UndeadSec/SocialFish.git",
    "48":"git clone https://github.com/DarkSecDevelopers/HiddenEye.git",
    "49":"git clone https://github.com/trustedsec/social-engineer-toolkit",
    "50":"git clone https://github.com/htr-tech/nexphisher",
    "51":"git clone https://github.com/htr-tech/zphisher"
    }


    style_termux = """
    [1]Lazymux            [2]Spammer-Grab

    [3]ngrok              [4]hammer

    [5]hulk               [6]wifite

    [7]EasY_HaCk          [8]wifi-scanner

    [9]sqlmap             [10]Tool-X

    [11]fb                [12]V7x-Tool

    [13]MITMF             [14]N404-Tool

    [15]saycheese         [16]OSIF

    [17]TBom              [18]JokerTools

    [19]LEDEAR_HACKING    [20]HxWhatsApp

    [21]T-Header          [22]Y-Hack

    [23]Matermuxx         [24]RouterSploit

    [25]ipcs              [26]Hack pubg

    [27]TxTool            [28]Termux-Fedora

    [29]Dev Ploit         [30]fsociety

    [31]Wifi-scan         [32]HT-WPS-Breaker

    [33]hakkuframework    [34]fluxion

    [35]Termux-ubuntu     [36]MITMF

    [37]3vilTwinAttacker  [38]HT-WPS-Breaker

    [39]DarkSploit        [40]DarkFly-Tool

    [41]A-Rat             [42]Beef


           [43]Termux-Style


              social fish

    [44]shellphish        [45]weeman

    [46]Black eye         [47]Social Fish

    [48]Hidden eye        [49]social-engineer-toolkit

    [50]Nexphiser         [51]Zphisher
"""

    def installer1(number):
        try:
            os.system(tools_termux[number])
        except:
            print("error not found....")
    print(style_termux)
    user = input("enter number tool: ")
    installer1(user)
    back = input("enter 99 to back: ")
    if back == "99":
        os.system("python MH-Tool.py")

###############################################################################
if E4 == "2":
    os.system("clear")
    tools_scan = {
    "1":"git clone https://github.com/nmap/nmap.git",
    "2":"git clone https://github.com/threat9/routersploit.git",
    "3":"git clone https://github.com/sqlmapproject/sqlmap.git",
    "4":"git clone https://github.com/Dionach/CMSmap.git",
    "5":"git clone https://github.com/Gameye98/OWScan",
    "6":"git clone https://github.com/Dionach/CMSmap.git",
    "7":"git clone https://github.com/D4Vinci/Clickjacking-Tester",
    "8":"git clone https://github.com/TechnicalMujeeb/TM-scanner",
    "9":"git clone https://github.com/AndroBugs/AndroBugs_Framework",
    "10":"git clone https://github.com/commixproject/commix",
    "11":"git clone https://github.com/sullo/nikto",
    "12":"git clone https://github.com/thelinuxchoice/sqliscan"
    }
    style_scan = """
    [1]Nmap scan

    [2]RouterSploit scan

    [3]Sqlmap scan

    [4]Cmsmap scan

    [5]OWScan

    [6]CMSmap

    [7]Clickjacking-Tester

    [8]TM-scanner

    [9]AndroBugs_Framework

    [10]commix

    [11]Nikto

    [12]sqliscan

    """
    def installer2(number_scan):
        try:
            os.system(tools_scan[number_scan])
        except:
            print("error not found....")
    print(style_scan)
    user1 = input("enter number tool: ")
    installer2(user1)
    back1 = input("enter 99 to back: ")
    if back1 == "99":
        os.system("python MH-Tool.py")
############################################################################
if E4 == "3":
    os.system("clear")
    tools_info = {
    "1":"git clone https://github.com/Richienb/iplocation.git",
    "2":"git clone https://github.com/UndeadSec/EvilURL.git",
    "3":"git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git",
    "4":"git clone https://github.com/thelinuxchoice/thechoice.git",
    "5":"git clone https://github.com/maldevel/IPGeoLocation",
    "6":"git clone https://github.com/Tuhinshubhra/RED_HAWK",
    "7":"git clone https://github.com/cr4shcod3/pureblood",
    "8":"git clone https://github.com/thelinuxchoice/userrecon",
    "9":"git clone https://github.com/UltimateHackers/ReconDog",
    "10":"git clone https://github.com/m4ll0k/Infoga",
    "11":"git clone https://github.com/Manisso/Crips",
    "12":"git clone https://github.com/maldevel/IPGeoLocation"


    }
    style_info = """
    [1]ip location             [2]Evil URL

    [3]D-TECT                  [4]The CHOICE

    [5]IPGeoLocation           [6]RED_HAWK

    [7]pureblood               [8]userrecon

    [9]ReconDog                [10]Infoga

    [11]Crips                  [12]IPGeoLocation
    """
    def installer3(number_info):
        try:
            os.system(tools_info[number_info])
        except:
            print("error not found....")
    print(style_info)
    user2 = input("enter number tool: ")
    installer3(user2)
    back2 = input("enter 99 to back: ")
    if back2 == "99":
        os.system("python MH-Tool.py")
############################################################################
if E4 == "4":
    os.system("clear")
    tool_meta = {
    "1":"git clone https://github.com/rapid7/metasploit-framework.git"
    }
    style_meta = """
    [1]metasploit
    """
    def installer4(number_meta):
        try:
            os.system(tool_meta[number_meta])
        except:
            print("error not found....")
    print(style_meta)
    user3 = input("enter number tool: ")
    installer4(user3)
    back3 = input("enter 99 to back : ")
    if back3 == "99":
        os.system("python MH-Tool.py")
############################################################################
if E4 == "5":
    os.system("clear")
    tool_dos = {
    "1":"git clone https://github.com/cyweb/hammer.git",
    "2":"git clone https://github.com/grafov/hulk.git",
    "3":"git clone https://github.com/XCHADXFAQ77X/XERXES.git",
    "4":"git clone https://github.com/jseidl/GoldenEye.git"
    }
    style_dos = """
    [1]H.A.M.M.E.R            [2]H.U.L.K

    [3]X.E.R.X.E.S            [4]Golden E.Y.E
    """
    def installer5(number_dos):
        try:
            os.system(tool_dos[number_dos])
        except:
            print("error not found....")
    print(style_dos)
    user4 = input("enter number tool: ")
    installer5(user4)
    back4 = input("enter 99 to back: ")
    if back4 == "99":
        os.system("python MH-Tool.py")
###########################################################################
if E4 == "6":
    print("""
    my name : Mohamed Hesham Elsayed
    city : Mansoura
    age : 17 
    my channal in youtube : https://www.youtube.com/channel/UCSDUPq4uEPb_y_TN3BgKD-Q
    """) 
    back5 = input("enter 99 to back:")
    if back5 == "99":
        os.system("python MH-Tool.py")

#############################################################################

