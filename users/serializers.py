from django.contrib.auth.models import User
from maintdx.workorders.serializers import WorkOrderSerializer
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        depth = 1
