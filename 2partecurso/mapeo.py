import ConfigParser

interprete = ConfigParser.ConfigParser()
interprete.read('protomap.map')
print interprete.get('seccion','a')
print interprete.get('seccion','b')
print interprete.get('seccion2','c')
#sections
print interprete.sections()#que secciones tengo
#item
print interprete.items('seccion2')#que items tengo en una seccion
