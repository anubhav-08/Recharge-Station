from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, primary_key=True)

    class Meta:
        verbose_name_plural = "Companies"
    def __str__(self):
        return self.name

class Plan(models.Model):
    price = models.IntegerField(blank=False)
    validity = models.IntegerField(blank=False)
    description = models.CharField(max_length=512)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.price) + " valid for " + str(self.validity)