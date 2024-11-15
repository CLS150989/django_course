from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    description = models.TextField(max_length=300, verbose_name='decripción')
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name = 'precio')
    available = models.BooleanField(default=True, verbose_name='disponible') 
    photo = models.ImageField(upload_to='logos', blank=True, null=True, verbose_name='imagen')

    def __str__(self) -> str:
        return self.name
