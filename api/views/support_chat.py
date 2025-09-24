from rest_framework import viewsets
from api.models.support_chat import SupportChat, Conversation
from api.serializers.suport_chat import SupportChatSerializer, ConversationSerilizer

# Conversation viewset
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerilizer 

# SupportChat viewset nested under Conversation
class SupportChatViewSet(viewsets.ModelViewSet):
    serializer_class = SupportChatSerializer

    def get_queryset(self):
        conversation_id = self.kwargs.get("conversation_pk")
        return SupportChat.objects.filter(conversation_id=conversation_id)

    def perform_create(self, serializer):
        conversation_id = self.kwargs.get("conversation_pk")
        conversation = Conversation.objects.get(id=conversation_id)
        serializer.save(conversation=conversation)  
