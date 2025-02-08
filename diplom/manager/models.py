from django.db import models


class Executors(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class Bank(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
