from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView

from stackfusion import settings
from user.models import Profile
from user.serializer import ProfileSerializer


class SignUp(APIView):
    def post(self, request):
        user = request.data
        serializer = ProfileSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            subject = 'confirmation mail'
            message = 'your details have been submitted successfully'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [request.data['email'], ], fail_silently=False)
            return Response({"success": "user '{}' created successfully".format(user_saved.name)})


class ShowUsers(APIView):
    def get(self, request):
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response({"users": serializer.data})
