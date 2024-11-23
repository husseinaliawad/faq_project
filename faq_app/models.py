from django.db import models

class FAQ(models.Model):
    question = models.TextField()  # The question
    answer = models.TextField()    # The answer
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.question
