"""
    F12实现移动端抓取:
        1.开启F12的手机模式, 选择一款手机型号, 刷新页面开始抓取数据包

    手机+Fiddle组合抓取移动端数据:
        1. 手机网络和电脑网络链接同一个路由器
        2. 配置流程:
            2.1 配置手机
                1) 长按无线网络标识修改网络
                2） 高级选项中, 将代理选择手动, 并设置为电脑IP
                    服务器主机名:电脑IP
                    端口号:8888(固定)
                3） 浏览器输入http://电脑IP:8888
                4) 下载Fiddle证书并安装
            2.2 配置Fiddle
                1） Fiddle-Tools-HTTPS-Decrypt HTTPS traffic-...from all process
                2) Connections-勾选Allow remote computers to connect
            2.3 打开手机app测试
"""