from django.db import models


# Create your models here.
class Subscription(models.Model):
    class Plan(models.TextChoices):
        Bronze = 'Bronze','Globalnet Bronze'
        Silver = 'Silver','Globalnet Silver'
        Golde = 'Gold','Globalnet Gold'

    plan = models.CharField(max_length=100, choices=Plan.choices,blank=True,null=True)
    cost = models.FloatField()

    def __str__(self) -> str:
        return self.plan


class Company(models.Model):

    plans = models.ForeignKey(Subscription,on_delete=models.CASCADE,null=True,blank=True)
    company_name = models.CharField(max_length=100)
    company_mail = models.EmailField(max_length=50,unique=True,blank=True,null=True)
    phone_number = models.CharField(max_length=15, unique=True)


    class Meta:

        verbose_name_plural = 'companies'

    def __str__(self):
        return self.company_name