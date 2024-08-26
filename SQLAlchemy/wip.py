# Apenas um teste com base na live. 
metadata = metadata()
from sqlalchemy import create_engine, text

engine = create_engine(  # Factory
    'sqlite://',
    echo=True
)

# with engine.connect() as con:
#    with con.begin():
#     sql = text('select id, name, comment from comments')
#     result = con.execute(sql)

t = Table('comments', metadata, autoload_with=engine)

sql = (
    select(t.c.id, t.c.name, t.c.comment)
    .where(t.c.name == 'tal coisa')
)

print(sql)

with engine.connect() as con:
    result = con.execute(sql)
    print(result.fetchmany(10))

# print(connection.connection.dbapi_connection)
# - A: Atomico/ Atomicidade
