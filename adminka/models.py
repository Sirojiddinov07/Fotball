from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=23232)
    date_birth = models.DateField()
    description = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=23232)
    played_minutes = models.IntegerField()
    sub_off = models.IntegerField()
    games = models.IntegerField()
    number = models.IntegerField()
    TYPE = (
        (1, 'attacker'),     #нападающий
        (2, 'midfielder'),   #полузащитник
        (3, 'defender'),     #защитник
        (4, 'goalkeeper'),   #вратарь
        (6, 'substitute'),    #замена
    )
    status = models.SmallIntegerField(default=6,choices=TYPE)
    captain = models.BooleanField(default=False)


class Club(models.Model):
    players = models.ManyToManyField(Player)
    name = models.CharField(max_length=2323232)
    photo = models.ImageField()
    scored = models.IntegerField()
    missed = models.IntegerField()
    game = models.IntegerField()
    scores = models.IntegerField()


class Turnir(models.Model):
    date = models.DateTimeField()
    club = models.ManyToManyField(Club)
    name = models.CharField(max_length=23232)


class Match(models.Model):
    date = models.DateTimeField()
    turnir = models.ForeignKey(Turnir, on_delete=models.CASCADE)
    club1 = models.ForeignKey(Club, related_name='ffffff', on_delete=models.CASCADE)
    club2 = models.ForeignKey(Club, related_name='sdsdsds', on_delete=models.CASCADE)
    club_1_result = models.IntegerField()
    club_2_result = models.IntegerField()


class Trending(models.Model):
    video = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=2323)
    photo = models.ImageField()
    description = models.CharField(max_length=65676876)


class Sponsor(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=344343)


class Product(models.Model):
    name = models.CharField(max_length=23232)
    photo = models.ImageField(max_length=23232)
    price = models.IntegerField()
    description = models.CharField(max_length=23232)


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Card(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SocialMedia(models.Model):
    inst = models.URLField()
    yt = models.URLField()
    tt = models.URLField()
    twitter = models.URLField()
    facebook = models.URLField()





# Create your models here.


