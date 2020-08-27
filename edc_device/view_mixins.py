

from django.apps import apps as django_apps


class EdcDeviceViewMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_config = django_apps.get_app_config('edc_device')
        context.update({
            'device_id': app_config.device_id,
            'device_role': app_config.device_role,
            'ip_address': self.ip_address,
        })
        return context

    @property
    def ip_address(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
