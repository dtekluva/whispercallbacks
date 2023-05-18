from rest_framework import serializers

from callbacks.models import MessageStatus


# Create your Serializer(s) here.
class MessageStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageStatus
        fields = "__all__"
