from django.db import models


class User(models.Model):
    date_joined = models.DateTimeField(null=False)
    username = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)


class Contract(models.Model):
    start_date = models.DateTimeField(null=False)
    product_id = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class RecurrentContract(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
