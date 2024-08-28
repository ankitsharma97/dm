from django.db import models

class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.bank_name

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, unique=True)  # IFSC codes are usually 11 characters
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    branch = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.branch} - {self.ifsc}"
