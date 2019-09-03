from django.db import models

# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='标题')
    price = models.DecimalField(verbose_name='单价',
                                max_digits=10,
                                decimal_places=2)
    pay_status = models.IntegerField(choices=((0, '待支付'),
                                              (1, '已支付')),
                                     verbose_name='支付状态')
    class Meta:
        db_table = 't_order'