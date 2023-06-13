from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String

engine = create_engine('sqlite:///Books.db', echo = True)
meta = MetaData()

Books = Table(
    'Books', meta,
    Column('id', Integer, primary_key=True, autoincrement= True),
    Column('title', String),
    Column('year', Integer)
)

meta.create_all(engine)

book_title = input("Enter book title: ")
book_year = input("Enter book year: ")
book_year = int(book_year)

if book_year > 2023:
    print("Error!")
else:
    print("Succes!")
    query = Books.insert().values(title = book_title, year = book_year)

query2 = Books.select()

conn = engine.connect()
r1 = conn.execute(query)
result = conn.execute(query2)

for row in result:
    print("Title: {} | Year: {} |".format(row[1],row[2]))
