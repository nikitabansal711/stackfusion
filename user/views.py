"""
Views contain logic for Signup and GetUsers View
"""
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView

from stackfusion import settings
from user.models import Profile
from user.serializer import ProfileSerializer


class SignUp(APIView):
    """
    To signup form data
    """
    def post(self, request):
        """
        Post form data
        :param request: django request
        :return: Sucess response
        """
        user = request.data
        serializer = ProfileSerializer(data=user)
        # Checking validity for Serializer
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            subject = 'confirmation mail'
            message = 'your details have been submitted successfully'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [request.data['email'], ], fail_silently=False)
            return Response({"success": "user '{}' created successfully".format(user_saved.name)})


class ShowUsers(APIView):
    """
    Get all the users
    """
    def get(self, request):
        """
        Get all the users
        :param request: django request
        :return: data for all the users
        """
        # To get all the Profile
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response({"users": serializer.data})
