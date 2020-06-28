from db import session, Products

products = session.query(Products).all()

mapColor = {}

#mapeando o i e para nunca repetir assinatura de cores
for i, product in enumerate(products):
    mapColor[product.color+':'+str(i)] = product.reviews

mapReduce = {}

#reduce
for key in mapColor.keys():
    aux = key.split(':')
    try:
        mapReduce[aux[0]] += mapColor[key]
    except:
        mapReduce[aux[0]] = mapColor[key]

print(mapReduce)


#poderia fazer de forma direta tbm:
for product in products:
    try:
        mapReduce[product.color]] += product.reviews
    except:
        mapReduce[product.color]] = product.reviews
