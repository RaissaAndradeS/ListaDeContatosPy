import sqlalchemy as sa 

metadata = sa.metadata()

t = sa.Table(
    'comments', 
    metadada, 
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('live', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
)

engine = sa.create_engine('sqlite:///database.db')

metadata.create_all(engine)

## Outra forma 

import sqlalchemy as sa 

metadata = sa.metadata()
engine = sa.create_engine('sqlite:///database.db')

t = sa.Table('comments', metadata, autoload_with=engine)

print(t.columns)

# sa.inspect(engine)
# print(inspect.get_table_names())
# print(inspect.get_table_columns())