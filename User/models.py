from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from datetime import datetime
# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, TeamID, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not TeamID:
            raise ValueError('The given email must be set')
        #email = self.normalize_email(email)
        user = self.model(TeamID=TeamID, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, TeamID, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(TeamID, password, **extra_fields)

    def create_superuser(self, TeamID, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(TeamID, password, **extra_fields)


class User(AbstractUser):
    
    TeamID = models.CharField(max_length=10,null=False,blank=False,unique=True)
    is_FirstLogin = models.BooleanField(default=True)
    FirstLogin = models.DateTimeField(default=datetime.now,blank=True)
    questions_attempted=models.CharField(max_length=200,default='',blank=True)
    language_selected = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'TeamID'
    objects = UserManager()
    