from django.db import models
from django.urls import reverse
from django import forms



class Image(models.Model):
    name = models.FileField(upload_to='images1/', help_text='выберите файл')
    author = models.ForeignKey('User', on_delete=models.CASCADE)



    #def __str__(self):
    #    return self.author

    def get_absolute_url(self):
        return reverse('name', args=[str(self.id)])



class User(models.Model):
    nickname = models.CharField(max_length=30, help_text='nickname')


    def __str__(self):
        return self.nickname


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)


class Images(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['author', 'name']