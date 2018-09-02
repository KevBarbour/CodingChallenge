# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 20:18:56 2018

@author: kevin
"""

import random
import csv

while True: #Age question, nullifies user input errors
   try:       
       n = int(input("Please enter age: "))     
   except ValueError:
       print("Age does not compute, please enter a integer i > 1")  
       pass
   else:       
       if 2 <= n <= 3:
           whatAge = "2 to 3"
           break
       elif 4 <= n <= 8:
           whatAge = "4 to 8"
           break
       elif 9 <= n <= 13:
           whatAge = "9 to 13"
           break
       elif 14 <= n <= 18:
           whatAge = "14 to 18"
           break   
       elif 19 <= n <= 30:
           whatAge = "19 to 30"
           break   
       elif 31 <= n <= 50:
           whatAge = "31 to 50"
           break
       elif 51 <= n <= 70:
           whatAge = "51 to 70"
           break   
       elif 71 <= n :
           whatAge = "71+"
           break   
       else:
           print("Age does not compute, please enter a integer i > 1")
      
while True: #Gender question, nullifies user input errors
   m = input("Please enter gender (m/f)? ")
   if m == "m": 
      whatGender = "Male"
      break
   elif m == "f":
      whatGender = "Female"
      break
   else:
      print("Please input only m or f")
      
print("\n","Catagory:",whatGender,", ages",whatAge)

with open("foodgroups-en_ONPP.csv",  "rt") as f0:    #assigns names to groups
    reader0 = csv.reader(f0, delimiter=",")
    for row0 in reader0:
        if row0[0] == "vf":
            t0 = row0[1]
        elif row0[0] == "gr":
            t1 = row0[1]
        elif row0[0] == "mi":
            t2 = row0[1] 
        elif row0[0] == "me":
            t3 = row0[1] 

csv_dict = {} 
with open("fg_directional_satements-en_ONPP.csv", "rt") as f1: #assigns healthy tip
    reader1 = csv.reader(f1)
    header = next(reader1)
    for row1 in reader1:
        if row1[0] in csv_dict:
            csv_dict[row1[0]].extend(row1)
        else:
            csv_dict[row1[0]] = row1
            if row1[0] == "vf":
                d0=row1[1]
            elif row1[0] == "gr":
                d1=row1[1]
            elif row1[0] == "mi":
                d2=row1[1]
            elif row1[0] == "me":
                d3=row1[1]
     
choice = "y"     
while choice == "y":    #main loop
    with open("servings_per_day-en_ONPP.csv",  "rt") as f2:
        reader2 = csv.reader(f2, delimiter=",")
        for row2 in reader2:
            if row2[3] == "1 to 2":     #converts invalid literal into an int 
                row2[3] = int(2)
            elif row2[3] == "3 to 4":
                row2[3] = int(4)
            elif row2[3] == "6 to 7":
                row2[3] = int(7)
            elif row2[3] == "7 to 8":
                row2[3] = int(8)
            elif row2[3] == "8 to 10":
                row2[3] = int(9)  
            if row2[1] == whatGender and row2[2] == whatAge:
                if row2[0] == "vf":
                    row2[0] = t0
                    foodType = "vf"
                    foodInfo = d0
                elif row2[0] == "gr":
                    row2[0] = t1  
                    foodType = "gr"
                    foodInfo = d1
                elif row2[0] == "mi":
                    row2[0] = t2 
                    foodType = "mi"
                    foodInfo = d2
                elif row2[0] == "me":
                    row2[0] = t3
                    foodType = "me"
                    foodInfo = d3
                x = int(row2[3])
                
                print("\n", row2[0]," - ",row2[3], "servings - ","Healthy Tip: ", foodInfo) 
    
                lines = open("foods-en_ONPP_rev.csv").readlines()   #randomizes food selection
                random.shuffle(lines)
                open("foods-en_ONPP_rev.csv", "w").writelines(lines)
                
                lines = open("fg_directional_satements-en_ONPP.csv").readlines()   #randomizes healthy tips
                random.shuffle(lines)
                open("fg_directional_satements-en_ONPP.csv", "w").writelines(lines)                
                
                with open("foods-en_ONPP_rev.csv",  "rt") as f3:    #draws specific foods
                    reader3 = csv.reader(f3, delimiter=",")
                    for row3 in reader3:
                        if row3[0] == foodType:
                            
                            fgcat_id = row3[1] 
                            with open("foodgroups-en_ONPP.csv",  "rt") as f4:    #assigns sub catagories
                                reader4 = csv.reader(f4, delimiter=",")
                                for row4 in reader4: 
                                    if row4[2] == fgcat_id:
                                         fgcat = row4[3]
                                         break

                            print("-", row3[3],":","(",row3[2], ") - ",fgcat)
                            x = x - 1            
                            if x == 0:                           
                                break   

    answer = input("Would you like to randomize the selection (y/n): ")
    if answer == "n": 
        choice = "n" 
        print("Thank you for using this program created by Kevin Barbour for Dr. Steve Liang.")
    elif answer == "y": 
        choice = "y" 
    else:
        print("Please answer with y or n .")
        break  

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            