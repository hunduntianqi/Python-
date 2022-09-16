"""
    http/https协议特性:无状态
    cookie:
        用来让服务器端记录客户端的相关状态
        处理cookie:
            1. 手动处理: 通过抓包工具获取cookie值, 将cookie封装到headers中
            2. 自动处理:
                cookie来源:模拟登录后, 由服务器端创建
                session会话对象:
                    创建session对象: session = requests.Session()
                    1. 可以进行请求的发送, 与requests模块一致
                    2. 在请求过程中产生的cookie, 会被自动存储在session对象中并携带
"""