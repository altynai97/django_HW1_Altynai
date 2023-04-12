from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'{self.item.name} - {self.name}'
