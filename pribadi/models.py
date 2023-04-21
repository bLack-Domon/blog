from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Profil(models.Model):
 nama = models.CharField(max_length=250, null=True, blank=True)
 tentang_diri = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
 foto = models.ImageField(max_length=250, null=True, blank=True)
 hp = models.CharField(max_length=250, null=True, blank=True)
 fb = models.CharField(max_length=250, null=True, blank=True)
 ig = models.CharField(max_length=250, null=True, blank=True)

 def __str__(self):
     return self.nama
 
 class Meta:
  verbose_name_plural = "Profil Diri"


class Artikel(models.Model):
 judul = models.CharField(max_length=250, null=True, blank=True)
 isi_artikel = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
 foto_artikel = models.ImageField(max_length=250, null=True, blank=True)
 penulis = models.CharField(max_length=250, null=True, blank=True)
 tanggal = models.DateField(auto_now_add=False, null=True)

 def __str__(self):
     return self.judul
 
 class Meta:
  verbose_name_plural = "Artikel"


class Khutbah(models.Model):
 penulis = models.CharField(max_length=250, null=True, blank=True)
 judul = models.CharField(max_length=250, null=True, blank=True)
 isi_khutbah = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
 foto_khutbah = models.ImageField(max_length=250, null=True, blank=True)
 tanggal = models.DateField(auto_now_add=False, null=True)

 def __str__(self):
     return self.judul
 
 class Meta:
  verbose_name_plural = "Khutbah"


class Album(models.Model):
 judul_foto = models.CharField(max_length=250, null=True, blank=True)
 foto = models.ImageField(max_length=250, null=True, blank=True)
 judul_album = models.CharField(max_length=250, null=True, blank=True)
 tanggal = models.DateField(auto_now_add=False, null=True)

 def __str__(self):
     return self.judul_foto
 
 class Meta:
  verbose_name_plural = "Album Foto"