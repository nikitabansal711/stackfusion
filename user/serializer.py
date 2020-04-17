from rest_framework import serializers

from user.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'mobile', 'email', 'date_of_birth')
