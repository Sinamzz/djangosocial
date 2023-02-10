from django.db import models
from django.contrib.auth.models import User


class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(null=True, blank=True)


class IpAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.user} with ip : {self.ip_address}'


class IpLog(models.Model):
    ip_address = models.GenericIPAddressField()
    route = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ip_address} with route: {self.route} on : {self.created}'


class BlockListIp(models.Model):
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.ip
