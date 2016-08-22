[![Build Status](https://travis-ci.org/botswana-harvard/edc-device.svg?branch=develop)](https://travis-ci.org/botswana-harvard/edc-device)
[![Coverage Status](https://coveralls.io/repos/botswana-harvard/edc-device/badge.svg?branch=develop&service=github)](https://coveralls.io/github/botswana-harvard/edc-device?branch=develop)

# edc-device

The Edc supports multiple off-line data collection clients. In such an environment a unique device ID is used to seed unique subject and sample identifiers created when offline. The group of clients should be configured each to have a unique ID, the `device_id`, before deployment.

Other functions might need to know the `role` of the device. For example, is it a server (central or community), a "middleman" machine, or a client. Knowing this is useful, for example, if a server is not allowed to allocate new subject_identifiers.

Device information is set in `edc_device.apps.AppConfig`. You should subclass into your projects `apps.py` like this, for example:

    from edc_device.apps import AppConfig as EdcDeviceAppConfigParent
    
    class EdcDeviceAppConfig(EdcDeviceAppConfigParent):
        device_id = '32'

... and then in your settings:

    INSTALLED_APPS = [
        ...
        my_app.apps.EdcDeviceAppConfig,
        myapp.apps.AppConfig',
    ]

A `client` might look like this:

    class EdcDeviceAppConfig(EdcDeviceAppConfigParent):
        device_id = '18'
    	server_id_list = [97, 98, 99]
    	middleman_id_list = [95, 96]

	>>> from django.apps import apps as django_apps
	>>> app_config = django_apps.get_app_config('edc_device')
	>>> app_config.device_id
	'18'
	>>> app_config.is_client
	True
    >>> app_config.role
    'Client'

A node server server might look like this:

    class EdcDeviceAppConfig(EdcDeviceAppConfigParent):
        device_id = '98'
        server_id_list = [97, 98, 99]
        middleman_id_list = [95, 96]

    >>> from django.apps import apps as django_apps
    >>> app_config = django_apps.get_app_config('edc_device')
    >>> app_config.device_id
    '98'
    >>> app_config.is_node_server
    True
    >>> app_config.role
    'NodeServer'

A middleman server might look like this:

    class EdcDeviceAppConfig(EdcDeviceAppConfigParent):
        device_id = '95'
        server_id_list = [97, 98, 99]
        middleman_id_list = [95, 96]

    >>> from django.apps import apps as django_apps
    >>> app_config = django_apps.get_app_config('edc_device')
    >>> app_config.device_id
    '95'
    >>> app_config.is_middleman
    True
    >>> app_config.role
    'Middleman'

The central server might look like this:

    class EdcDeviceAppConfig(EdcDeviceAppConfigParent):
        device_id = '99'
        server_id_list = [97, 98, 99]
        middleman_id_list = [95, 96]

    >>> from django.apps import apps as django_apps
    >>> app_config = django_apps.get_app_config('edc_device')
    >>> app_config.device_id
    '99'
    >>> app_config.is_middleman
    True
    >>> app_config.role
    'CentralServer'


See also `edc_sync`.
