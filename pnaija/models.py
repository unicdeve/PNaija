from django.db import models
from datetime import datetime

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(
        'auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    meterid = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    is_officer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Feedback(models.Model):
  TITLE_TYPES = (
    (1, "Enquires"),
    (2, "Report Critical Situation"),
    (3, "Give Us Your Suggestions")
  )
  title = models.IntegerField(choices=TITLE_TYPES, default=1)
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length = 100)
  content = models.TextField()
  createdAt = models.DateTimeField(auto_now_add=True)
  location = models.CharField(max_length=100, default = "null")

  def __str__(self):
    return self.get_title_display()

  class Meta:
    ordering = ['-createdAt',]
