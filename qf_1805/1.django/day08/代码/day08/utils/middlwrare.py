
from django.utils.deprecation import MiddlewareMixin

from users.models import MyUser


class UserAuthMiddlwrare(MiddlewareMixin):

    def process_request(self, request):

        user = MyUser.objects.get(username='admin')
        request.user = user

        return None



