from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from selenium import webdriver
from time import sleep
import csv


from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

url="https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"
driver.get(url)

# Applying filters using selenium

driver.find_elements_by_id('navbarDropdownMenuLink')[2].click()
driver.find_elements_by_class_name('property-type.room-no.pull-right')[0].find_elements_by_tag_name('span')[2].click()
driver.find_elements_by_class_name('property-type.room-no.pull-right')[0].find_elements_by_tag_name('span')[3].click()



#  Scrolling to get all the data which only shows up on scrolling to the bottom

SCROLL_PAUSE_TIME = 1
sleep(SCROLL_PAUSE_TIME)  # Wait to load page
last_height = driver.execute_script("return document.body.scrollHeight")       # Get scroll height

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # Scroll down to bottom

    sleep(SCROLL_PAUSE_TIME)  # Wait to load page

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    if(new_height == last_height):    # Applying the end condition for stoping the scroll
        break
    else:
        last_height = new_height

#######################################################################################

#  Getting properties container from the web page

page_soup = soup(driver.page_source, 'html.parser')
containers = page_soup.findAll("div", {"class":"filter-property-list detailurl"} )

driver.quit()

# print("Successfully executed ....\n",len(containers))



# ......  Backend code for scrapping and expoting to excel file  ...........

temp=1
alldata=[]

for i in containers:
    # Getting Heading
    heading = str(i.findAll("h1",{"class":"filter-pro-heading"})[0])
    start=heading.find("<span>")
    heading  = heading[31:start]

    #Getting Location
    location = i.findAll("a",{"class":"fullscreen"})[0].text

    # Getting Prize
    price = i.findAll("span",{"class":"price"})[0].text
    price_per_unit =  i.findAll("span",{"class":"price-per-unit"})[0].text
    price_per_unit = price_per_unit[1:len(price_per_unit)]

    # Getting Total Area
    area = i.findAll("div",{"class":"row filter-pro-details"})[0].findAll("div")[0].text
    area = area[4:len(area)]

    # Getting Facing side
    facing = i.findAll("div",{"class":"row filter-pro-details"})[0].findAll("div")[1].text
    facing = facing[6:len(facing)]

    # Getting Status
    status = i.findAll("div",{"class":"row filter-pro-details"})[0].findAll("div")[2].text
    status = status[6:len(status)]

    # Getting Property Features
    feature1 = i.findAll("ul",{"class":"pro-list"})[0].findAll("li")[0].text
    feature2 = i.findAll("ul",{"class":"pro-list"})[0].findAll("li")[1].text
    feature3 = i.findAll("ul",{"class":"pro-list"})[0].findAll("li")[2].text
    feature4 = i.findAll("ul",{"class":"pro-list"})[0].findAll("li")[3].text

    #Getting Owner/Agent Name
    name = i.findAll("span",{"class":"owner-name"})[0].text

    # Getting date posted
    posted = i.findAll("span",{"class":"owner-post"})[0].text.strip()
    posted = posted[8:len(posted)]

    # print("\n",temp,") \n")
    # print("Heading: ",heading,"\n")
    # print("Location: ",location,"\n")
    # print("price: ₹",price," (",price_per_unit,")\n")
    # print("Total Area: ",area,"\n")
    # print("Facing Side: ",facing,"\n")
    # print("Status: ",status,"\n")
    # print("Features: 1.",feature1,"    2.",feature2,"    3.",feature3,"    4.",feature4,"\n")
    # print("Owner/Agent Name: ",name,"\n")
    # print("Posted: ",posted,"\n")
    # print("\n######################################################\n")

    property_data = [temp,heading,location,price,area,facing, status,feature1,feature2,feature3,feature4,name,posted]
    alldata.append(property_data)   # adding each property data object in alldata
    temp+=1                     # increasing the serial number


# Creating the CSV File (EXCEL)

with open('afterFilters.csv', 'w') as csvfile:

    add = csv.writer(csvfile)
    add.writerow([""])
    add.writerow(["","Website: https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"])
    add.writerow(["","Filters: 2BHK, 3BHK and 4BHK"])
    add.writerow(["","Total Properties: "+str(len(containers))])
    add.writerow([""])
    headers = ["Sr. No.","Heading","Location","Price",
               "Total Area","Facing side","Status","Feature 1","Feature 2",
               "Feature 3","Feature 4","Owner/Agent Name","Posted"]

    add.writerow(headers)    # adding headers in the properties.csv file
    add.writerow("")

    # adding all the property rows
    for i in alldata:
        add.writerow(i)

    add.writerow([""])
    add.writerow(["","","","","","","","","","Coded By: Ayush Jain"])
    add.writerow(["","","","","","","","","","Github: https://github.com/ayushjaink8/webScrapping"])

print("\n########## Code Executed Successfully ###############\n ")

