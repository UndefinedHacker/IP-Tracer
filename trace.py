import requests
import json
import colorama
from colorama import Fore
import os
import sys

os.system("clear")
os.system("figlet IP TRACER | lolcat")
os.system('echo "Made by Undefined Hacker" | lolcat')
try:
    ip = input("Enter IP Address: ")
    os.system("clear")
    url = "http://ip-api.com/json/" + ip
    trace = requests.get(url).json()
    os.system("figlet IP TRACER | lolcat")
    print("Made by Undefined Hacker")
    print(f"\nStatus: {trace['status']}\nCountry: {trace['country']}\nISP: {trace['isp']}\nOrg: {trace['org']}\nCountry Code: {trace['countryCode']}\nRegion: {trace['region']}\nRegion Name: {trace['regionName']}\nZIP: {trace['zip']}\nLatitude: {trace['lat']}\nLongitude: {trace['lon']}\nTimezone: {trace['timezone']}\nAS: {trace['as']}")
except KeyError:
    os.system("clear")
    os.system("figlet ERROR | lolcat")
    print('The given IP Address/domain is invalid. Please check the spelling and try again.')
