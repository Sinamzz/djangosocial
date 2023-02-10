from account.models import IpLog, BlockListIp
from utils import get_ip_address
from django.http import HttpResponseForbidden



class ListenerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = get_ip_address(request)
        path = request.get_full_path()
        blacklist = BlockListIp.objects.all()

        if not request.user.is_superuser:
            for item in blacklist:
                ip_blocked = item.ip
                if ip == ip_blocked:
                    return HttpResponseForbidden()
        request.user.ip_address = ip
        response = self.get_response(request)

        if (not '/media/' in path) and (not 'favicon.ico' in path) and (not 'admin' in path):
            IpLog.objects.create(ip_address=ip, route=path)

        return response



