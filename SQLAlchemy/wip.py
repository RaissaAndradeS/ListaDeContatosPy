from sqlalchemy import create_engine

engine = create_engine(  # Factory
    'sqlite://',
    echo=True
)

con = engine.connect()

print(connection.connection.dbapi_connection)

con.close()