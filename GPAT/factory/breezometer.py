import json
import urllib
import sys
import random
def breezometer1(db,lat,lon): #Breezometer API
	api="6134c1cf8c9044b2a799417ff940d511"
	url="https://api.breezometer.com/baqi/?lat="+str(lat)+"&lon="+str(lon)+"&key="+api
	print(url)
	result=json.load(urllib.request.urlopen(url))
	if (result["data_valid"]=="False"):
		print("Inappropriate Location")
		return (1)
	else:
		breezometer_aqi=result["breezometer_aqi"]
		pollutant=result['dominant_pollutant_canonical_name']
		p=result['pollutants']
		CO=(p['co']['concentration'])
		NH3=(p['nh3']['concentration'])
		NO2=(p['no2']['concentration'])
		O3=(p['o3']['concentration'])
		PM10=(p['pm10']['concentration'])
		PM25=(p['pm25']['concentration'])
		SO2=(p['so2']['concentration'])
		data={"AQI":breezometer_aqi,"Pollutant":pollutant,"CO":CO,"NH3":NH3,"NO2":NO2,"PM10":PM10,"O3":O3,"PM25":PM25,"SO2":SO2}
		print(data)
		return(data)
'''lat=db.child("users/91kLs02HLpTP7aktpRXp7WWmfzG2/Factory/56874/Sensor/Latitude").get()
lat=lat.val()
lon=db.child("users/91kLs02HLpTP7aktpRXp7WWmfzG2/Factory/56874/Sensor/Longitude").get()
lon=lon.val()
breezometer1(db,lat,lon)'''