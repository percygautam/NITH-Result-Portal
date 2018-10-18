# IMPORT data processing and data visualisationn libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import json
from operator import itemgetter 
global s,brnch,year
global brnch2,year2

global gpmembers
global gpname
gpmembers=[]
gpname=[]
# Create the main function to draw bar graph
def mainfunc(x,y,plot_type):
	# Load the database as a dictionary from database1.txt file (created database)
	with open('dataBase1.txt', 'r') as f:
	    s = f.read()
	database = json.loads(s) 
	
	rollno = []
	rollno.append(x[0].upper())
	rollno2 = []
	if(len(y)==1):
		rollno2.append(y[0].upper())
	branch={   # branches as specified in the dataextractor file
	    '1':"CIVIL",
	    '2':"ELECTRICAL",
	    '3':"MECHANICAL",
	    '4':"ECE",
	    '5':"CSE",
	    '6':"ARCHI",
	    '7':"Chemical",
	    '8':"MATERIAL",
	    "MI4":"ECE DUAl",
	    "MI5":"CSE DUAL"
	}
	try:
		try: # Selecting year and branch on basis of rollno.
			year = 8-int(rollno[0][1])
			az = rollno[0][2:-2]
			for i in branch.keys():
				if az == i:
					brnch = branch[i]
		except:
			print("Please enter a valid rollno.")
		if(len(rollno2)==1):
			try:
				year2 = 8-int(rollno2[0][1])
				az2 = rollno2[0][2:-2]
				for i in branch.keys():
					if az2 == i:
						brnch2 = branch[i]
			except:
				print("Please enter a valid rollno.")
		
		# For SGPI data representation
		if("SGPI" in plot_type):
			semester = ['1st', '2nd', '3rd', '4th','5th', '6th', '7th', '8th'] # semesters list
			x = database[str(year)][brnch][rollno[0]]["sgpi"]
			y=[]
			for i in x:
			    m = ((i.split("=")[1]))
			    y.append(float(m))
			#Creating dataframe of student having sgpi
			db = pd.DataFrame(y,columns=['SGPI'])
			db['Semester']=semester[:year*2]
			db["Name"] = list((database[str(year)][brnch][rollno[0]]["name"]) for i in range(year*2))

			if(len(rollno2)==1):
				q = database[str(year2)][brnch2][rollno2[0]]["sgpi"]
				y2=[]
				for i in q:
				    m2 = ((i.split("=")[1]))
				    y2.append(float(m2))
				db2 = pd.DataFrame(y2,columns=['SGPI'])
				db2['Semester']=semester[:year2*2]
				db2["Name"] = list((database[str(year2)][brnch2][rollno2[0]]["name"]) for i in range(year*2))
				db = pd.concat([db,db2])
			# Plotting the bar graph
			sns.set(style="whitegrid")
			pl = sns.barplot(x="Semester", y="SGPI", data=db, hue='Name')#plotting barplot & setting parameters
			plt.ylim(1,12.5)
			plt.title("SGPI VS Semester")
			ax = plt.gca()
			totals=[]
			for i in ax.patches:
			    totals.append(i.get_height())

			# set individual bar lables using above list
			total = sum(totals)
			# Setting the place of bar labels
			for i in ax.patches:
			    # get_x pulls left or right; get_height pushes up or down
			    z1=i.get_height()
			    z1 = "%0.2f" % float(z1)
			    ax.text(i.get_x()+(i.get_width()/2), i.get_height()/2, \
			            z1, fontsize=(20-(year*2)),
			                color='black', ha= 'center')
			plt.show() #Shows the plot
		# For CGPI data representation 
		if("CGPI" in plot_type):
			semester = ['1st', '2nd', '3rd', '4th','5th', '6th', '7th', '8th']
			x = database[str(year)][brnch][rollno[0]]["cgpi"] #getting cgpi data of student
			y=[]
			for i in x:
			    m = ((i.split("=")[1]))
			    y.append(float(m))
			#Creating the dataframe of the student having CGPI
			db = pd.DataFrame(y,columns=['CGPI'])
			db['Semester']=semester[:year*2]
			db["Name"] = list((database[str(year)][brnch][rollno[0]]["name"]) for i in range(year*2))

			if(len(rollno2)==1):
				q = database[str(year2)][brnch2][rollno2[0]]["cgpi"]
				y2=[]
				for i in q:
				    m2 = ((i.split("=")[1]))
				    y2.append(float(m2))
				db2 = pd.DataFrame(y2,columns=['CGPI'])
				db2['Semester']=semester[:year2*2]
				db2["Name"] = list((database[str(year2)][brnch2][rollno2[0]]["name"]) for i in range(year*2))
				db = pd.concat([db,db2])
			#For class rank finding
			# make a sorted list of the class of student 
			srt=[]
			for z in database[str(year)][brnch]:
			    z1 = database[str(year)][brnch][z]['cgpi'][-1]
			    z1 = (float(z1.split("=")[1]))
			    info = {
			              "name": database[str(year)][brnch][z]['name'],
			              "cgpi": z1 
			              }
			    srt.append(info)
			srt = sorted(srt, key=itemgetter('cgpi', 'name'),reverse = True) #Creting sorted list of students
			#Plotting the bar graph for CGPI
			sns.set(style="whitegrid")
			pl = sns.barplot(x="Semester", y="CGPI", data=db, hue='Name') # Plotting & Setting parameters
			plt.ylim(1,12.5)
			plt.title("CGPI VS Semester")
			ax = plt.gca()
			totals=[]
			# Setting individual bar labels position
			for i in ax.patches:
			    totals.append(i.get_height())
			# set individual bar lables using above list
			total = sum(totals)
			for i in ax.patches:
			    # get_x pulls left or right; get_height pushes up or down
			    z1=i.get_height()
			    z1 = "%0.2f" % float(z1)
			    ax.text(i.get_x()+(i.get_width()/2), i.get_height()/2, \
			            z1, fontsize=(20-(year*2)),
			                color='black', ha= 'center')
			if(len(rollno2)!=1):
				z2 = database[str(year)][brnch][rollno[0]]['cgpi'][-1]
				z2 = (float(z2.split("=")[1]))
				dct = {"name" : database[str(year)][brnch][rollno[0]]["name"], 
						"cgpi" : z2
						}
				indx = srt.index(dct) # Finding class rank of student
				rank = "Class Rank : " + str(indx + 1)
				line, = ax.plot(0, label=rank)
				plt.legend()
			plt.show()#plotting the bar chart with CGPI and rank
	except: # Exception handler
		print("Please, enter a valid roll no.")