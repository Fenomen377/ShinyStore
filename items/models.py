from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=255, verbose_name='Размер')

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Размер'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    is_sold = models.BooleanField(default=False)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Предмет'

    def __str__(self):
        return self.name


