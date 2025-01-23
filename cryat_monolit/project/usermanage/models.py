import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def get_by_natural_key(self, nickname):
        return self.get(nickname=nickname)
    
    def create_user(self, nickname, password, **extra_fields):
        if not nickname:
            raise ValueError('The given nickname must be set')
        user = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password, **extra_fields):
        extra_fields.setdefault('role', 'superuser')
        return self.create_user(nickname, password, **extra_fields)

class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('superuser', 'superuser'),
        ('admin', 'admin'),
        ('user', 'user'),
    )

    nickname = models.CharField(max_length=63, unique=True, null=False)
    favorite_word = models.CharField(max_length=63, null=False)
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='user', null=False)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['favorite_word', 'role']

    objects = UserManager()

    def natural_key(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        return self.role in ['superuser', 'admin']

    def has_module_perms(self, app_label):
        return self.role in ['superuser', 'admin']

    @property
    def is_staff(self):
        return self.role in ['superuser', 'admin']

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.nickname