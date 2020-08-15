from xml.etree import ElementTree

class ParseXML:
    def __init__(self, xmlPath):
        self.xmlPath = xmlPath

    def getRoot(self):
        tree = ElementTree.parse(self.xmlPath)
        return tree.getroot()

    def fineNodeByName(self, parentNode, nodeName):
        nodes = parentNode.findall(nodeName)
        return nodes

    def getNodeOfChildText(self, node):
        childrenTextDict = {i.tag:i.text for i in list(node.iter())[1:]}
        '''
        等价：
        childrenTextDict = {}
        for i in list(node.iter())[1;]:
            childrenTextDict[i.tag] = i.text
        '''
        return childrenTextDict

    def getDataFromXml(self):
        root = self.getRoot()
        books = self.fineNodeByName(root, 'book')
        dataList = []
        # 遍历获取所有的book的节点对象
        for book in books:
            childrenText = self.getNodeOfChildText(book)
            dataList.append(childrenText)
        return dataList

if __name__ == '__main__':
    xml = ParseXML(r'./TestData')
    datas = xml.getDataFromXml()
    for i in datas:
        print(i['name'], i['author'])
