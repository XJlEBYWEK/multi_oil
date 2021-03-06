from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class News(models.Model):
    name = models.TextField(max_length=100, verbose_name="Название новости")
    name_url = models.CharField(max_length=100,verbose_name="URL",unique=True,default="",validators=[MinLengthValidator(3)])
    img_big = models.ImageField(verbose_name='Изображение большое (1100 х 300) ', upload_to="img", default="img/default.jpg")
    img_smole = models.ImageField(verbose_name='Изображение маленькое (300 х 200)', upload_to="img", default="img/default.jpg")
    img_alt = models.CharField(max_length=100,verbose_name="alt",default="", blank=True)
    img_title = models.CharField(max_length=100,verbose_name="title",default="", blank=True)
    body = RichTextField(verbose_name='Новость', null=True, blank=True, default="")
    data = models.TextField(max_length=100, verbose_name="Дата",default="",blank=True)
    date_add = models.DateTimeField(verbose_name="Дата создания",auto_now_add=True,)
    page_title = models.CharField(max_length=100,verbose_name="title",default="", blank=True)
    page_description = models.CharField(max_length=100,verbose_name="description",default="", blank=True)
    page_keywords= models.CharField(max_length=100,verbose_name="keywords",default="", blank=True)

    def get_absolute_url(self):
        return reverse('multi_oil:get-news', args=[str(self.name_url)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новость"

class Stocks(models.Model):
    name = models.TextField(max_length=100, verbose_name="Название акции")
    name_url = models.CharField(max_length=100,verbose_name="URL",unique=True,)
    img = models.ImageField(verbose_name='Изображение', upload_to="img", default="img/default.jpg")
    img_alt = models.CharField(max_length=100,verbose_name="alt",default="", blank=True)
    img_title = models.CharField(max_length=100,verbose_name="title",default="", blank=True)
    body = RichTextField(verbose_name='Акция', null=True, blank=True, default="")
    date_work = models.TextField(verbose_name='Время работы',max_length=100, default="" )
    date_add = models.DateTimeField(verbose_name="Дата создания",auto_now=True)
    page_title = models.CharField(max_length=100,verbose_name="title",default="", blank=True)
    page_description = models.CharField(max_length=100,verbose_name="description",default="", blank=True)
    page_keywords= models.CharField(max_length=100,verbose_name="keywords",default="", blank=True)




    def get_absolute_url(self):
        return reverse('multi_oil:get-stocks', args=[str(self.name_url)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Акции"
        verbose_name = "Акция"