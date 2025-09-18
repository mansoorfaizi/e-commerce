from rest_framework import viewsets
from api.models.support_chat import supportChat, conversation
from api.serializers.support_chat import supportchatserializer, conversationSerializer

class SupportChatHandler(viewsets.ModelViewSet):
    queryset = supportChat.objects.all()
    serializer_class = supportchatserializer




class ConversationHandler(viewsets.ModelViewSet):
    queryset = conversation.objects.all()
    serializer_class = conversationSerializer