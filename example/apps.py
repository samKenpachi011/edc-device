from django.apps import AppConfig as DjangoAppConfig

from edc_device.apps import AppConfig as EdcDeviceAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'example'


class EdcDeviceAppConfig(EdcDeviceAppConfigParent):
    device_id = '22'
