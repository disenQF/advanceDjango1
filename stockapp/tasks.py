#!/usr/bin/python3
# coding: utf-8
import time
from celery import shared_task


@shared_task
def qbuy(goods_id, user_id):
    print('qbuying....')
    time.sleep(5)
    print('%s Qbuying %s' % (goods_id, user_id))

    return '%s OK %s' % (goods_id, user_id)
