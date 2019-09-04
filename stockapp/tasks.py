#!/usr/bin/python3
# coding: utf-8
import logging
import time
from celery import shared_task
from advanceDjango.celery import app


@shared_task
def qbuy(goods_id, user_id):
    print('qbuying....')
    time.sleep(5)
    print('%s Qbuying %s' % (goods_id, user_id))

    return '%s OK %s' % (goods_id, user_id)


@app.task
def con_data(content):
    print('开始同步数据: %s' % content)
    logging.getLogger('').info('开始同步数据: %s' % content)
    return '同步完成'
