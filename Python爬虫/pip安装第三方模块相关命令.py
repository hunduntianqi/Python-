"""
pip--是一个通用的包管理工具,提供了对python包的查找,下载,安装,卸载等功能
pip命令：
更新pip：python -m pip install --upgrade pip
安装包：pip install 模块名
卸载包：pip uninstall 模块名
更新包：pip install -U 模块名
安装特定版本的模块：pip install 模块名==版本信息
查看已安装模块信息：pip show 模块名
列出所有安装的模块：pip list/pip freeze
列出所有未更新的模块：pip list -o
生成requirements.txt文件：pip freeze > requirements.txt
从requirements.txt文件安装所有依赖项：pip install -r requirements.txt（pip会忽略以前已经安装的所有模块）
验证安装的模块是否具有兼容的依赖关系：pip check
升级所有包的快捷方式:
 1.生成一个requirements.txt文件,安装命令：pip freeze > requirements.txt
 2.打开requirements.txt文件,将所有的 == 替换为 >=
 3.从requirements.txt安装依赖项：pip install -r requirements.txt --upgrade
pip 下载太慢解决方法
 1. 更改pip数据源
      豆瓣：http://pypi.douban.com/simple/
      清华：https://pypi.tuna.tsinghua.edu.cn/simple
      安装命名为 pip install -i 网址 所需要安装的库名
      例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
 2. 设置配置文件
    windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
        [global]
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple
"""