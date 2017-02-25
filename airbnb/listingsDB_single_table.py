import sqlite3
import csv
import urllib.request
from webscraping import getLinks

conn = sqlite3.connect('listings_single_table.db')
conn.isolation_level = None

TABLE_NAME = "listings"

def create_table():
	query = "CREATE TABLE IF NOT EXISTS '%s' (city TEXT, lat REAL, long REAL, price REAL)" % (TABLE_NAME)
	c.execute(query)
	print(query)

def data_entry(city, latitude, longitude, price):
	query = "INSERT INTO '%s' (city, lat, long, price) VALUES (?, ?, ?, ?)" % (TABLE_NAME)
	c.execute(query, (city, latitude, longitude, price))

dataLinks = getLinks();
#print(dataLinks)
try:
	c = conn.cursor()
	#c.execute("DROP TABLE IF EXISTS Amsterdam")
	c.execute("begin")
	create_table()

	for dataObj in dataLinks:
		try:
			response = urllib.request.urlopen(dataObj['Link'])
		except:
			response = urllib.request.urlopen(urllib.parse.quote(dataObj['Link'].encode('utf-8'),':/')) 
				
		cr = csv.DictReader(response.read().decode('utf-8').splitlines())
		for row in cr:
			data_entry(dataObj['City'], row['latitude'], row['longitude'], row['price'])

	c.execute("commit")
	c.close()
	conn.close()
except:
	print("error")
	c.execute("rollback")
