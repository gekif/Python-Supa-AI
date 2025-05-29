from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)  # Judul tugas
    description = models.TextField(blank=True)  # Deskripsi tugas (opsional)
    completed = models.BooleanField(default=False)  # Status selesai atau belum
    created_at = models.DateTimeField(auto_now_add=True)  # Waktu dibuat

    def __str__(self):
        return self.title
