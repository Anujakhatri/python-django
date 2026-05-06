from datetime import datetime

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(f"[{datetime.now()}] Request URL: {request.path}")

    def process_response(self, request, response):
        print(f"[{datetime.now()}] Response Status Code: {response.status_code}]")
        return response

class BlockIPMiddleware(MiddlewareMixin):
        BlOCKED_IPS=['127.0.0.1'] #example of blocked ip

        def process_request(self, request):
            ip = request.META.get('REMOTE_ADDR')
            if ip in self.BlOCKED_IPS:
                return HttpResponse("You have been blocked.")