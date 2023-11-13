from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
# Create your models here.


class User(AbstractUser):
    profile_image = ResizedImageField(
        size = [300,300],
        crop = ('middle','center'),
        upload_to = 'profile',
    )


    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # user_set(followers) =  
    # symmetrical=False => 1번에서 2번가는 것과 2번에서 1번가는 것이 다르다는 것을 알려줌 