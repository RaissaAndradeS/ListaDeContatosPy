import sqlalchemy import create_engine, metadata, Table, select 

metadata = metadata()

t = Table(
    'comments', 
    metadada, 
    Column('id', sa.Integer(), nullable=False),
    Column('name', sa.String(), nullable=False),
    Column('comment', sa.String(), nullable=False),
    Column('live', sa.String(), nullable=False),
    Column('created_at', sa.DateTime(), nullable=True),
    PrimaryKeyConstraint('id')
)

engine = create_engine('sqlite:///database.db')

metadata.create_all(engine)

## Outra forma 

import sqlalchemy as sa 

metadata = sa.metadata()
engine = sa.create_engine('sqlite:///database.db')

t = sa.Table('comments', metadata, autoload_with=engine)



# sa.inspect(engine)
# print(inspect.get_table_names())
# print(inspect.get_table_columns())

sql = sa.select(t)

print(sql)