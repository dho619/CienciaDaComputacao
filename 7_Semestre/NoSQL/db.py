import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_string = "postgres://geovane:1.618_3,14@localhost:5432/Prova7P2b"

engine = sqlalchemy.create_engine(sqlalchemy_string)

# Define e cria a tabela
Base = declarative_base()

#schema para ser usado na uniao das tabelas products e sizes
products_sizes = sqlalchemy.Table('products_sizes', Base.metadata,
    sqlalchemy.Column('size_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('sizes.id')),
    sqlalchemy.Column('product_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id'))
)


#criando tabelas
class Categorys(Base):
    __tablename__ = 'categorys'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.String(length=100), unique=True)
    products = sqlalchemy.orm.relationship("Products",  back_populates='category')

    def __repr__(self):
        return "<Categorys(description='{0}'>".format(self.description)


class Sizes(Base):
    __tablename__ = 'sizes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.String(length=100), unique=True)
    products = sqlalchemy.orm.relationship("Products", secondary=products_sizes, back_populates='sizes')

    def __repr__(self):
        return "<Sizes(description='{0}'>".format(self.description)

class Products(Base):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=200))
    mrp = sqlalchemy.Column(sqlalchemy.Float)
    price = sqlalchemy.Column(sqlalchemy.Float)
    pdp_url = sqlalchemy.Column(sqlalchemy.String(length=500))
    brand_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    description = sqlalchemy.Column(sqlalchemy.String(length=3000))
    rating = sqlalchemy.Column(sqlalchemy.Float)
    reviews = sqlalchemy.Column(sqlalchemy.Integer)
    style_attributes = sqlalchemy.Column(sqlalchemy.String(length=3000))
    color = sqlalchemy.Column(sqlalchemy.String(length=50))
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('categorys.id'))
    category = sqlalchemy.orm.relationship("Categorys", back_populates='products')
    sizes = sqlalchemy.orm.relationship("Sizes", secondary=products_sizes, back_populates='products')


    def __repr__(self):
        return "<Product(name='{0}', mrp='{1}', price='{2}', pdp_url='{3}', brand_name='{4}', description='{5}', rating='{6}',reviews='{7}', color='{8}')>".format(
                            self.name, self.mrp, self.price, self.pdp_url, self.brand_name, self.description, self.rating, self.reviews, self.color)

# Criando uma sessao no banco
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
