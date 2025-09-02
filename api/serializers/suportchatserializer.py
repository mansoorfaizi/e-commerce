from rest_framework import serializers
from ..models.support_chat import SupportChat , Conversation

class ConversationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class SupportChatSerializer(serializers.ModelSerializer):
    conversation = ConversationSerilizer(read_only = True)
    sender = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = SupportChat
        fields = '__all__'