from django.db import models

class tbl_user(models.Model):
    Name=models.CharField(max_length=20)
    User_name=models.CharField(max_length=20)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=25)
    Password=models.CharField(max_length=40)
    Address=models.CharField(max_length=40)
    Department=models.CharField(max_length=40)
    class Meta:
        db_table="tbl_user"
class tbl_didnt(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=50)
    regDte=models.DateField(auto_now_add=True)
    class Meta:
        db_table="tbl_didnt"

# Create your models here.
