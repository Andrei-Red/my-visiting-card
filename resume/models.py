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


class MyInformation(models.Model):
    name = models.CharField('name', max_length=100)
    photo = models.ImageField('photo', upload_to='resume/')
    salutation = models.CharField('salutation', max_length=200)
    description = models.TextField('description')
    email = models.CharField('email', max_length=100)
    phone = models.CharField('phone', max_length=100)

    def __str__(self):
        return self.name


class Reward(models.Model):
    reward_img = models.ImageField('reward', upload_to='resume/')
    description = models.TextField('description', blank=True)
    person = models.ForeignKey(MyInformation, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField('name', max_length=100)
    picture = models.ImageField('picture', upload_to='project/')
    description = models.TextField('description', blank=True)
    url = models.CharField('url', unique=True, max_length=100)

    def __str__(self):
        return self.name