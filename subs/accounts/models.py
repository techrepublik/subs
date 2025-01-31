from django.db import models
import random
import os
import datetime
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Invalid email address.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
    
def subs_picture_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    new_filename = f"{instance.id_no}{extension}"

    return f"profile/subscribers/{new_filename}"

def emp_picture_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    new_filename = f"{instance.emp_no}{extension}"

    return f"profile/employees/{new_filename}"
    
class User(AbstractBaseUser, PermissionsMixin):
    sub_no = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    ext_name = models.CharField(max_length=10, choices=[("jr", "Jr."), ("sr","Sr.")], default="",  blank=True, null=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=[("client","Client"),("employee","Employee")], default="", blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return f"{self.email}"
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    emp_no = models.CharField(max_length=100, unique=True, editable=False)
    marital_status = models.CharField(max_length=10, choices=[("single","Single"), ("merried","Married"), ("widow","Widow"), ("annulled","Annulled"), ("separated","Separated")], default="single", blank=True, null=True)
    gender = models.CharField(max_length=2, choices=[("M", "Male"), ("F", "Female")], default="M")
    contact_no = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    is_good = models.BooleanField(default=True)
    level = models.CharField(max_length=50, choices=[("admin","Admin"), ("cashier","Cashier"), ("collector","Collector"), ("marketing","Marketing"), ("technical","Technical")], default="", blank=True, null=True)
    picture = models.ImageField(upload_to=emp_picture_path, default="default.jpg", null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.emp_no:
            self.emp_no = self.generate_employee_number()
        super().save(*args, **kwargs)

        if self.picture:
            picture_path = self.picture.path
            img = Image.open(picture_path)

            img = img.convert("RGB")
            img = img.resize((200, 200), Image.Resampling.LANCZOS)

            img.save(picture_path, format='JPEG', quality=90)

    def generate_employee_number(self):
        emp_no = ''.join([str(random.randint(0,10) for _ in range(10))])

        while Employee.objects.filter(emp_no=emp_no).exists():
            emp_no = ''.join([str(random.randint(0,9) for _ in range(10))])

        return emp_no
    

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    id_no = models.CharField(max_length=50, unique=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    ext_name = models.CharField(max_length=10, choices=[("jr", "Jr."), ("sr","Sr.")], default="",  blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=[("single","Single"), ("merried","Married"), ("widow","Widow"), ("annulled","Annulled"), ("separated","Separated")], default="single", blank=True, null=True)
    gender = models.CharField(max_length=2, choices=[("M", "Male"), ("F", "Female")], default="M")
    contact_no = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    is_good = models.BooleanField(default=True)
    picture = models.ImageField(upload_to=subs_picture_path, default="default.jpg", null=True, blank=True)
    added_by = models.ForeignKey(User, related_name="user_employee", on_delete=models.SET_NULL, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id_no:
            self.id_no = self.generate_subscriber_number()
        super().save(*args, **kwargs)

        if self.picture:
            picture_path = self.picture.path
            img = Image.open(picture_path)

            img = img.convert("RGB")
            img = img.resize((200, 200), Image.Resampling.LANCZOS)

            img.save(picture_path, format='JPEG', quality=90)


    def generate_subscriber_number(self):
        # Corrected code: using parentheses to generate a list
        id_no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        # Ensure id_no is unique
        while Subscriber.objects.filter(id_no=id_no).exists():
            id_no = ''.join(str(random.randint(0, 9)) for _ in range(10))


        year = datetime.datetime.now().year
        month = datetime.datetime.now().month

        return F'{id_no}{year}{month}' 

    

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
