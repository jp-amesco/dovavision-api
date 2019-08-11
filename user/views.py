from rest_auth.views import LoginView


class UserViewSet(LoginView):

    def get_response(self):
        original_response = super().get_response()
        return original_response
