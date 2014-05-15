#import sensortag
import sqlite3
import datetime
import time
from random import randint

def main():
	conn = sqlite3.connect("thermawatch.db")
	try:
		conn.execute("CREATE TABLE history (time, temp, humi)")
		conn.execute("CREATE TABLE current (now, temp, humi)")
		conn.execute("INSERT INTO current VALUES (1, 0, 0")
	except:
		pass
	print("Starting measurements...")
	while True:
		temp = randint(15,30)#sensortag.getAmbTemp()
		humi = randint(30,80)#sensortag.getHumid()
		systime = datetime.datetime.now()
		conn.execute("INSERT INTO history VALUES (?, ?, ?)", (systime, temp, humi))
		print("\nStored history readings:\nTime:", systime,\
			"\nTemperature:", temp, "\nHumidity:", humi)
		for x in range(1,30):
			temp1 = randint(15,30)#sensortag.getAmbTemp()
			humi1 = randint(30,80)#sensortag.getHumid()
			conn.execute("""UPDATE current SET temp = ?, humi = ?  WHERE now = 1""", (temp1, humi1))
			print("\nStored current readings:\nTemperature:", temp1, "\nHumidity:", humi1)
			#time.sleep(60)
			time.sleep(5)

main()
