from sqlalchemy import create_engine

engine = create_engine(  # Factory
    'sqlite://'
)

print(engine)
print(engine.dialect)