# middlewares.py
from django.utils.deprecation import MiddlewareMixin

class DisableCSRFForSpecificViewsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in ['/introduction/followupquestion/', '/another/view/path/']:
            setattr(request, '_dont_enforce_csrf_checks', True)
