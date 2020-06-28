import sys #para pegar o paramentro
from db import Base, engine, session, Categorys, Products, Sizes
import pandas as pd
import numpy as np

planilha = pd.read_excel('amazon_com.xlsx')

categorys = set(planilha['product_category'].values)# pega valores unicos da coluna de categoria

#pegar tds os tipos em produtos
sizes = []
for s in [x.split(',') for x in planilha['total_sizes']]:
    aux = [x.lstrip() for x in s]
    sizes += aux
sizes = set(sizes)#pegar valores unicos

if (len(sys.argv) > 1 and sys.argv[1].lower() == 'create_db'):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

for category in categorys:
    newCategory = Categorys(description=category[:100])
    session.add(newCategory)
    session.commit()

for size in sizes:
    newSize = Sizes(description=size[:100])
    session.add(newSize)
    session.commit()

for registro in planilha.itertuples():
    newProduct = Products( name = registro.product_name[:200] , mrp = registro.mrp , price = registro.price ,pdp_url = registro.pdp_url ,
                           brand_name = registro.brand_name[:100] , description = registro.description[:3000] , rating = registro.rating ,
                           reviews = registro.review_count , style_attributes = registro.style_attributes[:3000] , color = registro.color[:50]
                         )

    for sizeProd in str(registro.available_size).split(','):
        size = session.query(Sizes).filter_by(description=sizeProd.lstrip()).first()
        if size:
            newProduct.sizes.append(size)


    session.add(newProduct)
    session.commit()
