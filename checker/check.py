# -*- coding: utf-8 -*-

def _decode(value):
    import chardet
    try:
        encoding = chardet.detect(value)["encoding"]        
        return (value.decode(encoding), encoding)
    except (TypeError, UnicodeDecodeError):
        return (u'Failed get line', u'Failed detect encoding')

def _buildEncodingErrors(path, encoding): 
    try:
        errors = []
        for line in open(path).readlines():
            try:
                line.decode(encoding)
            except UnicodeDecodeError as ex:           
                errors.append((_decode(line), str(ex)))
    except IOError  as ex: 
        print(ex)
        return []
    else:
        return errors
    

def findEncodingErrors(absPathToDir, encoding):
    import os
    res = {}
    for pathToDir, _, files in os.walk(absPathToDir):
        for fileName in files:
            absPathToFile = os.path.join(pathToDir, fileName)
            errors = _buildEncodingErrors(absPathToFile, encoding)
            if (len(errors) != 0):
                res[absPathToFile] = errors
    return res

def toFile(path, data, code):
    import codecs
    try:
        codecs.open(path, 'w', code).write(data)     
    except IOError as ex:
        print(ex)
        
def buildHtml(errorsList, header):
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
                    u'<tr>'\
                        u'<td width="30%"><b>Путь к файлу</b></td>'\
                        u'<td width="30%"><b>Строка в UTF-8</b></td>'\
                        u'<td width="10%"><b>Исходная кодировка</b></td>'\
                        u'<td width="30%"><b>Текст исключения</b></td>'\
                    u'</tr>'\
                    u'{table}'\
                u'</table>'\
            u'</body>'\
        u'</html>'
        
        
    style = u'table, th, td {border: 1px solid gray;} table {border-collapse: collapse;} .cell{word-break: break-all;}'
        
    table = u''
    for filePath in errorsList:
        for error in errorsList[filePath]:
            line = re.sub(r'\<[^>]*\>', '', error[0][0])
            encoding = error[0][1]
            exception = error[1]
            row = u'<tr><td><div class="cell"><a href="{0}">{0}</a></div></td><td><div class="cell">{1}</div></td><td><div class="cell">{2}</div></td><td><div class="cell">{3}</div></td></tr>'
            table += row.format(filePath, line, encoding, exception)
         
    return res.format(header=header, style=style, table=table)
