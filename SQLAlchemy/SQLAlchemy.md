## <center> SQLAlchemy </center>

O SQLAlchemy é um kit de ferramentas para trabalhar com banco de dados SQL e Python. O principal objetivo é "automações" para diversas coisas. 

Para usar, ativar o ambiente virtual do Python e pip install sqlalchemy.

No meu caso. <br>
 -- SQLAlchemy\Scripts\activate.

Core - Núcleo - a base de tudo, ele é responsável por criar a conexão com o banco de dados, fazer buscas e definir tipos.

A Engine - Motor - conexão no banco de dados, dialeto é mecanismo específico para cada banco e o pool de conexões.

A Engine é o coração de tudo, é uma fábica de conexões com o banco de dados.

<center> Engine -> dialeto -> DBAPI </center>

Existe vários dialetos possíveis padrões dentro do SQLAlchemy. E existe vários plugins para outros. 

Após a conexão, no 'pool' o reservatório de conexões. Chega, pede conexão para o banco e após criar, ele não fecha a conexão. 
Um exemplo é o ```print(engine.pool)```. 

Schemas/Types - são metadados das tabelas que podem ser descritos com Schemas e seus determinados Tipos.

Reflection - funções de inspeções são agregadas a contrução de schemas, para evitar a criação dos metadados em um banco que já existe