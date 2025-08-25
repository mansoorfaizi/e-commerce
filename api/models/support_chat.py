from django.db import models
from .timestamp import TimeStampedModel
from django.conf import settings

class Conversation(TimeStampedModel):
    subject = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"Conversation: {self.subject} (User: {self.user.username})"


class SupportChat(TimeStampedModel):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='support_chats')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='support_chats')

    def __str__(self):
        return f"SupportChat #{self.id} (Conversation #{self.conversation.id}) - {self.message[:40]}"