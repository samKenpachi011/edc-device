[![Build Status](https://travis-ci.org/botswana-harvard/edc-device.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-device)

# edc-device


Setup
-----
	
As a client, add to settings:

	DEVICE_ID = 18
	CENTRAL_SERVER_ID = 99
	SERVER_DEVICE_ID_LIST = [97, 98, 99]
	MIDDLEMAN_DEVICE_ID_LIST = [95, 96]
	PRODUCER_PREFIX = 'bcpp'
	
As a sentral server, add to settings:

	DEVICE_ID = 99
	CENTRAL_SERVER_ID = 99
	SERVER_DEVICE_ID_LIST = [97, 98, 99]
	MIDDLEMAN_DEVICE_ID_LIST = [95, 96]
	PRODUCER_PREFIX = 'bcpp'


Usage
-----	

	from edc_device import device
	
	>>> device
	<Client 18@mac.local>
	>>> str(device)
	'18'
	