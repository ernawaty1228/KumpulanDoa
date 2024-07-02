from django.db import models
from kategori.models import Kategori

class Doa(models.Model):
    judul = models.CharField(max_length=200)
    arab = models.TextField()  
    arti = models.TextField() 
    kategori = models.ForeignKey(Kategori, related_name='doa', on_delete=models.CASCADE)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
