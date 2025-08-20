from django.db import models
from .conversation import Conversation

class SupportChat(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='support_chats')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

     
    def __str__(self):
        return f"SupportChat #{self.id} (Conversation #{self.conversation.id}) - {self.message[:40]}"