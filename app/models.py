from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
    

# Create your models here.
class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    isim = models.CharField(max_length=30)
    soyisim = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True)
    telefon = models.CharField(max_length=30, blank=True, default='00') 
    # telefon = PhoneNumberField(blank=True, )
    cinsiyet = models.CharField(max_length=50, default="erkek", blank=True, choices=(
        ('erkek','Erkek'),
        ('kadın','Kadın'),
    ))
    bilgi = models.CharField(max_length=30, blank=True)    
    ekl_tarih = models.DateField(auto_now_add=True) 
    foto = models.ImageField(upload_to='resimler/', blank=True, help_text='jpg,png,bmp resim yükleyebilirsiniz')
    etiket = models.CharField(max_length=30, default=' ', blank=True, choices=(
        ('is','İş'),
        ('okul','Okul'),
        ('arkadas','Arkadaş'),
        ('aile','Aile'),
        ('diger','Diğer'),
    ))

    def __str__(self):
        return self.isim + ' '+ self.soyisim    
    
    class Meta:
        ordering = ['id']