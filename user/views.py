from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView

from stackfusion import settings
from user.serializer import ProfileSerializer


class SignUp(APIView):
    def post(self, request):
        user = request.data.get("user")
        serializer = ProfileSerializer(data=user)
        recipient_list = []
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            subject = 'confirmation mail'
            message = 'your details have been submitted successfully'
            email_from = settings.EMAIL_HOST_USER
            recipient_list.append(user.email)
            send_mail(subject, message, email_from, recipient_list)
            return Response({"success": "user '{}' created successfully".format(user_saved.name)})
