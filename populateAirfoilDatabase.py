import airfoilDB
import requests
import re
import time
import csv

airFoilHeader = "http://airfoiltools.com/airfoil/details?airfoil="
polarHeader = "http://airfoiltools.com/polar/csv?polar=xf-"
coordinateHeader = "https://m-selig.ae.illinois.edu/ads/coord/"
polarRE = [50000,100000,200000,500000,1000000]

# initialize db if not already
db = airfoilDB.airfoilDatabase()

response = requests.get("http://airfoiltools.com/search/airfoils")
airfoils = re.findall("<a href=\"/airfoil/details\?airfoil=(.*?)\">",response.text)

count = 0
total = len(airfoils)*len(polarRE)
# populate database with gathered airfoils
for foil in airfoils:
    starttime = time.time()
    # get airfoil coordinates
    foilname = foil[:-3]
    print(foilname)
    coord = requests.get(coordinateHeader+foilname+".dat")
    if coord.status_code == 200:
        data = open('./AirfoilCoordinates/'+foilname+'.dat', 'w')
        data.write(coord.text)
        data.close()
    else:
        print(coordinateHeader+foilname+".dat: "+str(coord.status_code))
            
    for RE in polarRE:
        time.sleep(1)
        count+=1
        
        # get polar csv
        polar =requests.get(polarHeader+foil+"-"+str(RE))
        if polar.status_code == 200:
            reader = csv.reader(polar.text.split('\n'))
            f = open('./AirfoilPolars/'+str(RE)+'/xf-'+foil+'-'+str(RE)+'.csv', 'w', newline='')
            writer = csv.writer(f)
            writer.writerows(reader)
            #print(str(count)+"/"+str(total))
            f.close()
        else:
            print(polarHeader+foil+"-"+str(RE)+": "+str(polar.status_code))
    endtime = time.time()
    remaining = total-count
    timeremaining = remaining*(endtime-starttime)/3600
    print("Time Remaining (min): "+str(timeremaining))
    
"""
db.sendCommand("select * from airfoils")
for row in db.c:
    print(row)
"""
