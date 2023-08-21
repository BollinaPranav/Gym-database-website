from django.db import models


class Trainers(models.Model):
    name = models.CharField('trainer name', max_length=120)
    address = models.CharField(max_length=300)
    phonenumber = models.CharField('trainer phone', max_length=25)
    email = models.EmailField('trainer email')

    def __str__(self):
        return str(self.name)


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Client name', max_length=120)
    dateofjoining = models.DateTimeField('Client doj')
    phonenumber = models.CharField(max_length=120)
    Amountdue = models.CharField(max_length=120)
    trainer = models.ForeignKey(Trainers, blank=True, null=True, on_delete=models.CASCADE)
    clientimage = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.name)


