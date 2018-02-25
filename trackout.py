#!/usr/bin/python

import os
import urllib2
import json
import colorama
colorama.init(autoreset=True)

os.system("clear");
print colorama.Fore.CYAN + """
  _____                _      ___       _   
 /__   \_ __ __ _  ___| | __ /___\_   _| |_ 
   / /\/ '__/ _` |/ __| |/ ///  // | | | __|
  / /  | | | (_| | (__|   </ \_//| |_| | |_ 
  \/   |_|  \__,_|\___|_|\_\___/  \__,_|\__|                                           
  Python IP Tracker - Abay | abaykan.com
"""
print "\r"
while True:
		ip = raw_input("What Your Target IP : ")
		url = "https://api.ipdata.co/"
		response = urllib2.urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print("------------------------------------")
		print "\r"
		print(" IP           :  " + values['ip'])
		print(" City         :  " + values['city'])
		print(" Region       :  " + values['region'])
		print(" Country      :  " + values['country_name'])
		print(" Continent    :  " + values['continent_name'])
		print(" Time Zone    :  " + values['time_zone'])
		print(" Currency     :  " + values['currency'])
		print(" Calling Code :  " + "+" + values['calling_code'])
		print(" Organisation :  " + values['organisation'])
		print(" ASN          :  " + values['asn'])
		print "\r"
		break