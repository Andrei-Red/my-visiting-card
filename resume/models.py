from django.db import models


class PlaceOfWork(models.Model):
    organization = models.CharField('organization', max_length=100)
    description = models.TextField('description')

    def __str__(self):
        return self.organization


class Detail(models.Model):
    organization = models.ForeignKey(PlaceOfWork, on_delete=models.CASCADE)
    position = models.CharField('position', max_length=100)
    responsibilities = models.TextField('responsibilities')
    started_work = models.DateTimeField('started_work')
    finished_work = models.DateTimeField('finished_work')

    def __str__(self):
        return self.position


class MyContact(models.Model):
    email = models.CharField('email', max_length=100)
    phone = models.CharField('phone', max_length=100)
