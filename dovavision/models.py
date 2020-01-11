from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
   
    def create_user(self, email, name, date_of_birth, password):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, last_login=now, name=name, date_of_birth=date_of_birth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, password):
        user = self.create_user(email, name, date_of_birth, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser):
    name = models.CharField(max_length=75, null=True)
    email = models.CharField(max_length=40, unique=True)
    date_of_birth = models.DateField()
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name