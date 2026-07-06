from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="ဘာသာရပ်အမည်")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='lessons', 
        verbose_name="ဘာသာရပ်"
    )
    image = models.ImageField(upload_to='lessons/images/', blank=True, null=True, verbose_name="သင်ခန်းစာပုံ")
    title = models.CharField(max_length=255, verbose_name="သင်ခန်းစာခေါင်းစဉ်")
    summary = models.TextField(blank=True, null=True, verbose_name="သင်ခန်းစာအကျဉ်းချုပ်")
    content = CKEditor5Field(verbose_name="သင်ခန်းစာအကြောင်းအရာ",config_name="default")
    video_material = models.FileField(
        upload_to='lessons/videos/', 
        blank=True, 
        null=True, 
        verbose_name="ဗီဒီယိုမီဒီယာ"
    )
    attachment = models.FileField(
        upload_to='lessons/attachments/', 
        blank=True, 
        null=True, 
        verbose_name="ပူးတွဲဖိုင်တွဲများ"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ဖန်တီးသည့်နေ့ရက်")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.course.title} - {self.title}"
