# Note: For proper working of this Script Good and Uninterepted Internet Connection is Required
# Or else increase the time duration between commands


# Import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math
import json

# Declare global variables
global gpmembers
global sems
global semester,curent_year
global flag

current_year=17
semester="even"
btech_range=list(range(100,899))
dual_range=list(range(401,600))


sems=[]
roll_range=[]
sgpi=[]
cgpi=[]
flag=[0]

database={}
branch={
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
#add the location of chrome driver 
#use if firefox is used
#driver = webdriver.Firefox()# Enter the path of driver in bracket as string 
driver = webdriver.Chrome("/Enter/the/path/of/driver")# Enter the path of chrome driver in bracket as string

def mainfun():
    
    #launch the site
    driver.get("http://academic.nith.ac.in/result.htm")
    #driver wait's for 10 and 5 sec
    wait = WebDriverWait(driver, 10)
    wait5 = WebDriverWait(driver, 5)

    # Add odd or even sems in  sem list
    if(semester=="odd"):
        sems=[]
        for i in range(4):
            sems.append(2*i+1) #1,3,5,7
    elif(semester=="even"):
        sems=[]
        for i in range(4):
            sems.append(2*i+2) #2,4,6,8 
    print(sems)

    # Extract results for each sem in list of sem
    for target in sems:
        #calculate year using present sem
        year=((target-1)//2)+1
        
        #click on particular sem link
        driver.find_element_by_xpath("//span[@class='auto-style21' and contains(text(),\'"+ str(target) +"\')]").click()
    # BTECH DEGREE

        # Create a empty dictionary with year as a key
        database[str(year)]={}
        #add all roll nos to roll range
        roll_range=[]
        for j in btech_range:
            roll_range.append(str(current_year-year+1)+str(j))#"current_year-year+1" calculates the initial format of roll no i.e for "17101" it calculates the 17 part 
        print(roll_range)
        
        rolls=roll_range[0]#extract first element of roll range 
        ranges=roll_range[-1]#extract last element of roll range
        print(ranges)
        time.sleep(0.05)
        #find the input box
        inp_xpath="//*[@id='table2']/tbody/tr[2]/td/form/p[4]/input"
        input_box=wait.until(EC.presence_of_element_located((By.XPATH,inp_xpath)))#wait if box not found

        #Create empty dict inside of previous year dict with branches as key 
        for f in range(1,9):
            database[str(year)][branch[str(f)]]={}
        database[str(year)][branch["MI4"]]={}
        database[str(year)][branch["MI5"]]={}
        
        #Iterate through all roll nos to extract their result
        while(int(rolls)<=int(ranges)):
            input_box.send_keys((rolls)+Keys.ENTER)
            time.sleep(0.05)
            
            # convert in json format i.e. dictionary
            jsonConvert(rolls,year)
            
            # if roll nos of a branch ends then it jumps to next branch
            if(flag[0]==1):

                rolls=roundup(int(rolls))#calls round up function
                flag[0]=0
            #go to previous page
            driver.execute_script("window.history.go(-1)")
            time.sleep(0.05)
            #find the input box
            input_box=wait.until(EC.presence_of_element_located((By.XPATH,inp_xpath)))
            #clean the input box
            input_box.clear()
            time.sleep(0.05)

            #increment the rolls
            rolls=int(rolls)+1
            rolls=str(rolls)

    #DUAL DEGREE
        #add all roll nos to roll range
        roll_range=[]
        for j in dual_range:
            roll_range.append(str((current_year-year+1))+"MI"+str(j))
        print(roll_range)

        time.sleep(0.05)
        #search for input box
        inp_xpath="//*[@id='table2']/tbody/tr[2]/td/form/p[4]/input"
        input_box=wait.until(EC.presence_of_element_located((By.XPATH,inp_xpath)))#wait if box not found
        
        #Iterate through all roll nos to extract their result
        for rolls in roll_range:
            input_box.send_keys((rolls)+Keys.ENTER)
            time.sleep(0.05)
            #convert in json format
            jsonConvert(rolls,year)
            #return to previous page
            driver.execute_script("window.history.go(-1)")
            time.sleep(0.05)
            #Find the input box and clear it
            input_box=wait.until(EC.presence_of_element_located((By.XPATH,inp_xpath)))
            input_box.clear()
            time.sleep(0.05)
        # return to previous page
        driver.execute_script("window.history.go(-1)")
  
    time.sleep(3)

#Function to add resuts to dictionary(almost json form)    
def jsonConvert(rolls,year):
    
    #Find the branch name using roll no 
    if(rolls[-4]=='I'):
        brnch=branch[rolls[-5:-2]]
    else:
        brnch=branch[rolls[-3]]    

    sgpi=[]
    cgpi=[]

    try:#checks for errors
        #Extract the name of the student 
        name_x_path="/html/body/div[1]/table/tbody/tr[1]/td[2]/div"
        name_text = driver.find_element_by_xpath(name_x_path).text
        
        #Extract the sem wise sgpi and cgpi and append it to the sgpi and cgpi list 
        for sem in range (year*2):
            sgpi_x_path="/html/body/div["+str(((sem+1)*2+1))+"]/table/tbody/tr[2]/td[1]"
            cgpi_x_path="/html/body/div["+str(((sem+1)*2+1))+"]/table/tbody/tr[2]/td[3]"
            sgpi_text = driver.find_element_by_xpath(sgpi_x_path).text
            sgpi.append(sgpi_text);
            cgpi_text = driver.find_element_by_xpath(cgpi_x_path).text
            cgpi.append(cgpi_text);
        #Add name, sgpi and cgpi to previous dict with rolls as keys
        database[str(year)][brnch][(rolls)]={
            "name":name_text,
            "sgpi":sgpi,
            "cgpi":cgpi
        }
    except:#do this if error occurs
        try:#checks if roll no of a branch ends
            error_x_path="/html/body/table/tbody/tr[1]/td/div/h2"
            error_text = driver.find_element_by_xpath(error_x_path).text
            if("Kindly Check" in error_text):#Message printed when a roll no does not exist
                # raises the flag
                flag[0]=1
            # adds empty dict to database
            database[str(year)][brnch][(rolls)]={}
            # pops the empty dict
            database[str(year)][brnch].pop((rolls))
        except:
            # adds and pops empty dict to database
            database[str(year)][brnch][(rolls)]={}
            database[str(year)][brnch].pop((rolls))
    return 

#round ups to nearest hundred
def roundup(x):
    return int(math.ceil(x / 100.0)) * 100

# run the main function
mainfun()

for i in (database):
    print("YEAR:", i)
    for j in database[i]:
        print("\tBRANCH:",j)
        for k in database[i][j]:
            print("\t\tROLLNO:",k)
            print("\t\t\tNAME:",database[i][j][k]["name"])
            print("\t\t\tSGPI:",database[i][j][k]["sgpi"])
            print("\t\t\tCGPI:",database[i][j][k]["cgpi"])
#create a new file and write database into it
with open('dataBase1.txt', 'a') as the_file:
    the_file.write(json.dumps(database));
