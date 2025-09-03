from rest_framework import serializers
from ..models.support_chat import SupportChat , Conversation

class ConversationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class SupportChatSerializer(serializers.ModelSerializer):
    conversation = ConversationSerilizer(read_only = True)
<<<<<<< HEAD
    sender = serializers.SerializerMethodField(read_only = True)
=======
    sender = serializers.StringRelatedField(read_only = True)
>>>>>>> 68aa4c1bce64bde07099c7310e054789150ee9cf
    class Meta:
        model = SupportChat
        fields = '__all__'