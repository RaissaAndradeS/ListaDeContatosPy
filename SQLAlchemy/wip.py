# Apenas um teste com base na live. 

from sqlalchemy import create_engine, text

engine = create_engine(  # Factory
    'sqlite://',
    echo=True
)

with engine.connect() as con:
    with con.begin():
     sql = text('select id, name, comment from comments')
     result = con.execute(sql)


# print(connection.connection.dbapi_connection)
# - A: Atomico/ Atomicidade
