from django.db import models
from google.genai import Client

class NUser(models.Model):
    session_id = models.CharField(max_length=255, db_index=True)

    def get_history(self):
        return [
                {"role": m.role, "parts": [{"text": m.text}]} 
                for m in self.messages.all()
            ]

    def __str__(self):
        return self.session_id

class ChatMessage(models.Model):
    user = models.ForeignKey(NUser, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=10)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']