from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class EMPLOYEE_LOGIN(models.Model):
    EMP_DIG_ID = models.CharField(max_length=25, primary_key=True)
    EMP_PNO = models.CharField(max_length=5)
    EMP_NAME = models.CharField(max_length=50)
    EMP_DESIGNATION = models.CharField(max_length=25)
    EMP_DEPTT = models.CharField(max_length=25)
    EMP_PASSWORD = models.CharField(max_length=128)  

    def save(self, *args, **kwargs):
        if self.EMP_PASSWORD:  
            self.EMP_PASSWORD = make_password(self.EMP_PASSWORD)  
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.EMP_NAME

class EMP_ATTENDANCE_REC(models.Model):
    EMP_DIG_ID = models.ForeignKey(EMPLOYEE_LOGIN, on_delete=models.CASCADE)
    EMP_CHECKIN_DATETIME = models.DateTimeField()
    EMP_CHECKOUT_DATETIME = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        string = self.EMP_DIG_ID.EMP_NAME + "," + str(self.EMP_CHECKIN_DATETIME) + "," + str(self.EMP_CHECKOUT_DATETIME)
        return string