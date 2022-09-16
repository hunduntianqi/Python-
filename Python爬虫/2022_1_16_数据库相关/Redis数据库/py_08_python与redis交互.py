"""
    1. 安装包-redis:
        pip install redis
    2. 引入模块:
        from redis import *
        该模块中提供了StrictRedis对象, 用于连接redis服务器, 并按照不同类型提供了不同方法
        进行交互操作
        sr = StrictRedis(host='IP地址(本机为127.0.0.1或localhost)', port=6379, db=0(指定使用那个数据库(0-15), 默认为0))
    3. 各种数据类型对应方法:
        3.1 string:
            set, setex, mset, append, get, mget, keys
        3.2 keys:
            exists, type, delete, expire, getrange, ttl
        3.3 hash:
            hset, hmset, hkeys, hget, hmget, hvals, hdel
        3.4 list:
            lpush, rpush, linsert, lrange, lset, lrem
        3.5 set:
            sadd, smembers, srem
        3.6 zset:
            zadd, zrange, zrangebyscore, zscore, zrem, zremrangebyscore

"""
from redis import *

sr = StrictRedis(host='localhost', port=6379, db=0)
sr.set('name', 'gpt')
sr.append('name', ' love cxn')
print(sr.keys())
print(sr.get('name'))
# sr.sadd('name', 'cxn')
# for i in sr.keys('*'):
#     sr.delete(i)