import pymysql
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

pymysql.install_as_MySQLdb()


def model_delete_pre(sender, **kwargs):
    from user.models import Order
    # sender 表示 哪一个Model的对象将要被删除， 信号的发送者
    # kwargs 表示 信息的基本信息， 信号发送时，传递一些信息
    print(sender)  # models.Model的子类
    # print(kwargs)  # key: signal, instance, using
    info = 'Prepare Delete %s 类的 id=%s, title=%s'
    # print(issubclass(sender, Order))  # True
    # print(isinstance(sender, Order))  # False
    # print(sender is Order)  # True
    # print(sender == Order)  # True
    if sender == Order:
        print(info % ('订单模型',
                      kwargs.get('instance').id,
                      kwargs.get('instance').title))


@receiver(post_delete)
def delete_model_post(sender, **kwargs):
    print(sender, '删除成功', kwargs)

pre_delete.connect(model_delete_pre)