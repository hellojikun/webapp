__author__ = 'kun.ji'
import asyncio, logging

import aiomysql

def log(sql,args=()):
    logging.info('SQL: %s' % sql)


async def create_pool(loop,**kw):
    logging.info('craete database connect pool')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charse=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsizse', 1),
        loop=loop
    )


asyncio def select(sql, args, size=None):
    log(sql, args)
    global  __pool
    