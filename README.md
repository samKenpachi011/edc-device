[![Build Status](https://travis-ci.org/botswana-harvard/edc-device.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-device)
[![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-device/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-device?branch=develop)

# edc-device

The Edc supports multiple off-line data collection clients. In such an environment a unique device ID is used to seed unique subject and sample identifiers created when offline. The group of clients should be configured each to have a unique ID, the `DEVICE_ID`, before deployment.

Other functions also ask `Device` for the role of the device. For example, is it a server (central or community), a "middleman" machine, or a client. Knowing this is useful, for example, if a server is not allowed to allocate new subject_identifiers.

By default, `Device` is configured through `settings.py` attributes where a unique `DEVICE_ID` is allocated to each machine.

A client might look like this:

	DEVICE_ID = 18
	CENTRAL_SERVER_ID = 99  # if other than 99
	SERVER_DEVICE_ID_LIST = [97, 98, 99]
	MIDDLEMAN_DEVICE_ID_LIST = [95, 96]

	>>> from edc_device import Device
	>>> device = Device()
	>>> str(device)
	'18'
	>>> device.is_client
	True

A community server might look like this:

	DEVICE_ID = 98
	CENTRAL_SERVER_ID = 99  # if other than 99
	SERVER_DEVICE_ID_LIST = [97, 98, 99]
	MIDDLEMAN_DEVICE_ID_LIST = [95, 96]

	>>> from edc_device import Device
    >>> device = Device()
	>>> str(device)
	'98'
	>>> device.is_community_server
	True


A middleman server might look like this:

	DEVICE_ID = 95
	CENTRAL_SERVER_ID = 99  # if other than 99
	SERVER_DEVICE_ID_LIST = [97, 98, 99]
	MIDDLEMAN_DEVICE_ID_LIST = [95, 96]

	>>> from edc_device import Device
    >>> device = Device()
	>>> str(device)
	'95'
	>>> device.is_middleman
	True

The central server might look like this:

	DEVICE_ID = 99
	CENTRAL_SERVER_ID = 99  # if other than 99
	SERVER_DEVICE_ID_LIST = [97, 98, 99]
	MIDDLEMAN_DEVICE_ID_LIST = [95, 96]

	>>> from edc_device import Device
    >>> device = Device()
	>>> str(device)
	'99'
	>>> device.is_central_server
	True

See also `edc_sync`.
