from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, name, user_level, password, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                name = name, user_level=user_level,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, name, user_level, password, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                name = name, user_level=user_level, password=password
            )
        user.staff =  True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, user_level, password, **extra_fields):
        user = self.create_user(email=email, name=name, user_level=user_level,password=password)
        user.staff=True
        user.admin=True
        user.save(using=self._db)
        return user
    
