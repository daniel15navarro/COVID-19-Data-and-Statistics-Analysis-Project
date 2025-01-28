'''
.py
  Authors: Daniel Navarro DeGiorgio (1167827), Jonas Matulis (1194815)
  Project: Milestone III (March 29, 2022)
  python reading_script.py Ethno-Racial_monthly_%.csv white black sea saic amewa la ea > plot.csv
'''

import sys
import os
import csv
import datetime


def main(argv):
    #gather arguments

    if len(argv) < 3:
        print(
            "Usage: reading_script.py <csv file> <first ethno-racial group> <second ethno-racial group>...<seventh ethno-racial group>"
        )
        sys.exit(1)

    raceArray = []
    #initialize variables from command line
    csv_file = argv[1]
    race1 = argv[2]
    raceArray.append(race1)
    race2 = argv[3]
    raceArray.append(race2)
    if(len(argv) > 4):
      race3 = argv[4]
      raceArray.append(race3)
    if(len(argv) > 5):
      race4 = argv[5]
      raceArray.append(race4)
    if(len(argv) > 6):
      race5 = argv[6]
      raceArray.append(race5)
    if(len(argv) > 7):
      race6 = argv[7]
      raceArray.append(race6)
    if(len(argv) > 8):
      race7 = argv[8]
      raceArray.append(race7)

    for raceElement in raceArray:
      if(not(raceElement.lower() == "amewa" or raceElement.lower() == "ea" or raceElement.lower() == "la" or raceElement.lower() == "saic" or raceElement.lower() == "sea" or raceElement.lower() == "black" or raceElement.lower() == "white")):
        print(f"Error: invalid ethno-racial group:{raceElement}" )

    for raceElement, x in zip(raceArray,range(len(raceArray))):
      #Arab, Middle Eastern or West Asian is amewa
        if(raceElement.lower() == "amewa"):
          raceArray[x] = 'Arab or Middle Eastern or West Asian'
        
        #East Asian is ea    
        elif(raceElement.lower() == "ea"):
          raceArray[x] = 'East Asian'
    
        #Latin American is la
        elif(raceElement.lower() == "la"):
          raceArray[x] = 'Latin American'
          
        #South Asian or Indo-Caribbean is saic
        elif(raceElement.lower() == "saic"):
          raceArray[x] = 'South Asian or Indo-Caribbean'
    
        #Southeast Asian is sea
        elif(raceElement.lower() == "sea"): 
          raceArray[x] = 'Southeast Asian'
    
        #Black is black
        elif(raceElement.lower() == "black"):
          raceArray[x] = 'Black'
    
        #White is white
        elif(raceElement.lower() == "white"):
          raceArray[x] = 'White'

    #try opening the csv file
    try:
      opened_csv_file = open(csv_file, "r")
    except IOError as err:
      print("Unable to open desired file '{}' : {}".format(csv_file, err), file=sys.stderr)
      sys.exit(1)

    opened_csv_file_reader = csv.reader(opened_csv_file)
    next(opened_csv_file_reader)

    print('date,race,Share of Covid Cases%,raceCovidCount,Representation of Toronto Population %,Difference Between Share of Covid and Share of Population')
    for line in opened_csv_file_reader:
      race = line[0]
      month = line[1]
      share_cases = line[2]
      count_cases = line[3]
      torontoPopRep = line[4]
      cur_date = datetime.date.fromisoformat(month)
      for raceElement in raceArray:
        if(raceElement.lower() == race.lower()):
          print(f'{cur_date},{race},{share_cases[:-1]},{count_cases},{torontoPopRep[:-1]},{round(float(share_cases[:-1])-float(torontoPopRep[:-1]),2)}')


main(sys.argv)
