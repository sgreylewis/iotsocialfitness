import RPi.GPIO as GPIO
import time
import uuid
import requests
import json 
from collections import OrderedDict

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print ("Distance Measurement in Progress; press CTRL+C to exit")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance():
	GPIO.output(TRIG, False)
	print ("Waiting For Sensor to Settle")
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	return float(distance)

if __name__ == '__main__':
	
	my_api = 'http://52.55.75.56:2001/api/v1/sensor/data'
	headers = {'Content-type': 'application/json'}
	user = "SarahLewis"
	device_status = None
	device_id = str(uuid.uuid1())
	device_depth = 19.5
	type = 'coffee_cup'
	
	try:
		while True:
			dist = distance()						
			#data = {'user': user, 'device_status': device_status, 'device_id': device_id, 'type': type}
			if (dist > (device_depth/2)) and (dist <= device_depth): #will not send them url
				data = None
				device_status = 'not empty'
			elif dist > device_depth: #want to let them know when it's empty so send url
				device_status = 'empty'
				data = {'user': user, 'device_status': device_status, 'device_id': device_id, 'type': type}
				jsondata = json.dumps(data)
				response = requests.post(my_api, data = jsondata, headers = headers)
			else: #send them url because it's full
				device_status = 'full' 
				data = {'user': user, 'device_status': device_status, 'device_id': device_id, 'type': type}
				jsondata = json.dumps(data)
				response = requests.post(my_api, data = jsondata, headers = headers)
			print (data)
			time.sleep(3)

	# Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()

	

