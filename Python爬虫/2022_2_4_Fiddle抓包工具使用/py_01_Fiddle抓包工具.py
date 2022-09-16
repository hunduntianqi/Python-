"""
    Fiddle抓包工具:
        和浏览器F12抓包功能一致, 记录并检查所有电脑和互联网之间的http通讯
        1.配置fiddler:
              Tools→Options→Https:选中Capture HTTPS Connects、Decrypt Https traffic、
            Ignore server certifcate errors(unsafe)
            配置完毕后,关闭软件重启
        2.抓包
            <>：HTML内容
            {json}:json数据,很有可能就是一个接口
            {2022-1-14-CSS}:CSS文件
            {js}:js文件
        3.停止抓取-F12
        4.Inspectors
            raw:请求和响应的详细信息
            webforms:请求所带的参数
            5.左下角黑色输入框可输入指令:
            5.1.clear:清除所有请求
            5.2.select json:快速选则所有json请求
            5.3.select image:选择图片请求
            5.4.select 2022-1-12-html:选择html请求
            5.5.？+搜索字符:搜索包含指定字符内容的请求
"""