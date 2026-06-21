from django.db import models

from django.db import models

class Course(models.Model):
    """
    Represents the main subject/course dropdown option (ဘာသာရပ်ရွေးချယ်ရန်)
    """
    title = models.CharField(max_length=255, verbose_name="ဘာသာရပ်အမည်")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Represents the lesson form data matching image_212596.png
    """
    # 1. ဘာသာရပ်ရွေးချယ်ရန် (Course Dropdown)
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='lessons', 
        verbose_name="ဘာသာရပ်"
    )
    image = models.ImageField(upload_to='lessons/images/', blank=True, null=True, verbose_name="သင်ခန်းစာပုံ")
    
    # 2. သင်ခန်းစာခေါင်းစဉ် (Lesson Title)
    title = models.CharField(max_length=255, verbose_name="သင်ခန်းစာခေါင်းစဉ်")
    
    # 3. သင်ခန်းစာအကျဉ်းချုပ် (Lesson Summary / Textarea)
    summary = models.TextField(blank=True, null=True, verbose_name="သင်ခန်းစာအကျဉ်းချုပ်")
    
    # 4. သင်ခန်းစာအကြောင်းအရာ (Lesson Content / Rich Text Area)
    content = models.TextField(verbose_name="သင်ခန်းစာအကြောင်းအရာ")
    
    # 5. မီဒီယာတင်ရန် (Media/Video Upload Field)
    video_material = models.FileField(
        upload_to='lessons/videos/', 
        blank=True, 
        null=True, 
        verbose_name="ဗီဒီယိုမီဒီယာ"
    )
    
    # 6. ဖိုင်တွဲများ (File Attachments Field)
    attachment = models.FileField(
        upload_to='lessons/attachments/', 
        blank=True, 
        null=True, 
        verbose_name="ပူးတွဲဖိုင်တွဲများ"
    )
    
    # Metadata tracking fields
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ဖန်တီးသည့်နေ့ရက်")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        # verbose_name = "သင်ခန်းစာ"
        # verbose_name_plural = "သင်ခန်းစာများ"

    def __str__(self):
        return f"{self.course.title} - {self.title}"
