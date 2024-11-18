from django.db import models

# Create your models here.
class Signup(models.Model):
    firstName = models.CharField(max_length=200)  # First name with a maximum of 200 characters
    lastName = models.CharField(max_length=10)  # Last name with a maximum of 10 characters
    email = models.EmailField(default="example@example.com")  # Email field with a default value
    phoneNumber = models.TextField(default="0000000000")  # Phone number as a text field (ensure proper validation elsewhere)

    def __str__(self):
        return (
            f"First name: {self.firstName}, "
            f"email: {self.email}, "
            f"Phone number: {self.phoneNumber}"
        )
