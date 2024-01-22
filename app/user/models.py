from django.db import models
from django.contrib.auth import get_user_model

# using the default user model
User = get_user_model()


class OwnerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    license_no = models.IntegerField(blank=True, null=True)
    passport_no = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
    

class EmployeeProfile(models.Model):
    SHIFT = (
        ("MORNING", "MORNING"),
        ("EVENING", "EVENING"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    shift = models.CharField(max_length=50, choices=SHIFT, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}-{self.shift}"
