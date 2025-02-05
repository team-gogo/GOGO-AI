from django.http import HttpResponse

class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health-check":
            return HttpResponse("GOGO AI Service OK", content_type="text/plain")
        return self.get_response(request)
