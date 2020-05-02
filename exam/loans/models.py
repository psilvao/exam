from django.db import models
from django.core.validators import  MinValueValidator

# Create your models here.

class Lender(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=15)
    Money = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.First_Name

    def get_FirstName(self):
        return self.First_Name
    def get_LastName(self):
        return self.Last_Name
    def get_Email(self):
        return self.Email
    def get_Money(self):
        return self.Money


class Borrow(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=15)
    Money_Need = models.PositiveIntegerField(default=1, validators=[ MinValueValidator(1) ])
    Subject = models.TextField(max_length=100)
    Description = models.TextField(max_length=400)
    Transactions = models.ManyToManyField(Lender,through='Loans')

    def __str__(self):
        return self.First_Name

    def get_FirstName(self):
        return self.First_Name

    def get_LastName(self):
        return self.Last_Name

    def get_Email(self):
        return self.Email

    def get_Money(self):
        return self.Money_Need
    
    def get_Subject(self):
        return self.Subject

    def get_Description(self):
        return self.Description


class Loans(models.Model):
    Loans_Lender = models.ForeignKey(Lender,on_delete=models.CASCADE)
    Loans_Borrow = models.ForeignKey(Borrow,on_delete=models.CASCADE)
    Loans_Money = models.PositiveIntegerField()
    Loans_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Loans_Date
    
    def get_LoansMoney(self):
        return self.Loans_Money






