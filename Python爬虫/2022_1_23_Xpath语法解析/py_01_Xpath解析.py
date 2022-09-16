"""
Xpath:在XML文档中搜索内容的一门语言,类似正则表达式,但简单的多！！
html是XML的一个子集,
Xpath解析需要安装lxml模块！！！
解析步骤：
1.通过xml数据和etree.XML()方法创建etree对象
2./表示层级关系,xml数据中的第一个/是根节点
3.通过etree对象.xpath('/根节点/节点1/节点2/text()')可以拿到节点2中的文本数据
4.通过etree对象.xpath('/根节点/节点1//节点2/text()')可以拿到节点1所包含节点2的全部文本数据,无视层级关系
5.*代表任意节点,可以拿出不同节点下相同节点的数据,例如:etree对象.xpath('/book/author/*/nick/text()')
   可以拿出*代表的同级不同名节点下的相同节点nick的文本数据
6.通过/标签[@属性=‘值’]的方式可以拿出对应标签的数据,例如：etree对象.xpath('/2022-1-12-html/body/ol/li/a[@href='dapao']/
    text()'),可以拿出a标签中属性href值为dapao的数据
7.‘./’表示当前节点
8.拿到属性值:@属性
"""
from lxml import etree

xml = """
    <book>
        <id>1</id>
        <name>野花遍地香</name>
        <price>1.23</price>
        <nick>臭豆腐</nick>
        <author>
            <nick id="10086">周大强</nick>
            <nick id="10010">周芷若</nick>
            <nick class="joy">周杰伦</nick>
            <nick class="jolin">蔡依林</nick>
            <div>
                <nick>热了1</nick>
            </div>
            <span>
                <nick>热了2</nick>
            </span>
        </author>
    
        <partner>
            <nick id="ppc">胖胖陈</nick>
            <nick id="ppbc">胖胖不陈</nick>
        </partner>
    </book>
"""

tree = etree.XML(xml)  # 通过xml数据和etree.XML()方法创建etree对象
# result = tree.xpath('/book')  #/表示层级关系,xml数据中的第一个/是根节点
# result = tree.xpath('/book/name/text()')  # text()方法拿出文本数据
# result = tree.xpath('/book/author//nick/text()') # //可以拿出此节点下指定节点的所有数据,无视层级限制
# result = tree.xpath('/book/author/*/nick/text()')  # *代表任意节点,可以拿出不同节点下相同节点的数据
result = tree.xpath('/book//nick/text()')
print(result)
