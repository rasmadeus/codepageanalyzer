# -*- coding: utf-8 -*-

def _getStrFrom(path, code): 
    try:
        return open(path).read().decode(code)
    except (IOError, UnicodeDecodeError)  as ex: 
        print(ex)
        return ''
    
def _buildMessList(messStr, word, newWord):
    import re
    pattern = u'\$MESS\[[\'"].+[\'"]\] *= *[\'"].*{word}.*[\'"]'.format(word=word)
    return [re.sub(word, newWord, mess) for mess in re.compile(pattern).findall(messStr)]   

def parse(absPathToDir, word, newWord, code):
    import os
    res = []
    for pathToDir, _, files in os.walk(absPathToDir):
        for fileName in files:
            absPathToFile = os.path.join(pathToDir, fileName)
            messList = _buildMessList(_getStrFrom(absPathToFile, code), word, newWord)
            if (len(messList) != 0):
                res.append((absPathToFile, messList))
    return res

def toFile(path, data, code):
    import codecs
    try:
        codecs.open(path, 'w', code).write(data)     
    except IOError as ex:
        print(ex)
        
def buildHtml(messList, header):
    import re
    res = \
        u'<html>' \
            u'<meta charset="UTF-8" />' \
            u'<head>'\
                u'<title>{header}</title>'\
                u'<style>{style}</style>'\
            u'</head>'\
            u'<body>'\
                u'<h1>{header}</h1>'\
                u'<table>'\
                    u'{table}'\
                u'</table>'\
            u'</body>'\
        u'</html>'
        
        
    style = u'table, th, td {border: 1px solid gray;} table {border-collapse: collapse;}'
        
    table = u''
    for messPart in messList:
        path = messPart[0]
        for messValue in messPart[1]:
            messValueParts = re.split('["\']', messValue)
            key = messValueParts[1]
            value = messValueParts[3]
            table += u'<tr><td><a href="file://{path}">{path}</a></td><td>{key}</td><td>{value}</td></tr>'.format(path=path, key=key, value=value)
        
    return res.format(header=header, style=style, table=table)