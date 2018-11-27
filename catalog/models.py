from django.db import models

class Product(models.Model):
    id_product = models.IntegerField("ИД",max_length=512, blank=True, null=True, db_index=True)
    name = models.CharField("Название",max_length=1024, blank=True, null=True, db_index=True)
    price = models.FloatField("Цена",max_length=512, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name