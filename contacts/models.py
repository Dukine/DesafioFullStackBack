from django.db import models
import uuid

class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127)
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    phone = models.CharField(max_length=10)
    registered_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name= 'contacts')
