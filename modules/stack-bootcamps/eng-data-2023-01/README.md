# Bootcamp de Engenharia de Dados do canal Stack (Janeiro 2023)

> Meus códigos e exemplos do **Bootcamp de Engenharia de Dados** do canal [Stack do Youtube](https://www.youtube.com/c/Stack_tecnologias/featured).

## Conteúdo

 - [Arquitetura do Projeto](#project-architecture)
 - [Criando uma conta IAM (Identity and Access Management)](#iam)
 - [Criando um Banco de Dados RDS (Relational Database Service) na AWS](#rds)
 - [Testando conexão com o Banco de Dados na AWS (Database Client extension)](#testing-aws-db)
 - [Pegando dados da API coinmarketcap e salvando no Banco de Dados](#testing-api-db)
 - [Criando o Data Lake (Buckets) na AWS com S3](#data-lake-s3)
 - [Criando o DMS (Database Migration Service) na AWS](#dms)
 - [Criando Endpoints no DMS na AWS](#endpoints-dms)
 - [Configurações do projeto](#settings)

---

<div id="project-architecture"></div>

## Arquitetura do Projeto

![img](images/project-architecture.png)  

 - **Data Source:**
 - **Ingestion:**
 - **Data Lake:**
   - Armazena diversos tipos de dados (Exemplo um diretório com arquivos JSON, CSV, Parquet, Delta).
 - **[Delta Lake (delta.io)](https://delta.io/):**
   - Formato especial de armazenar dados.
 - **Preprocessing:**
 - **Serving:**
 - **Management:**
 - **Data Warehouse:**

---

<div id="iam"></div>

## Criando uma conta IAM (Identity and Access Management)

> Agora por motivos de segurança vamos criar uma conta **"IAM (Identity and Access Management)"** para não ficar acessando e modificando recursos como usuário **"root"**.

Para começar pesquise por **"IAM"** na *AWS*:

![img](images/iam-01.png)  

 - Clique em "Users":
   - Add users:
     - Coloque o nome do usuário (ex: drigols).
     - Habilite permissão ao "console".
       - Provide user access to the AWS Management Console - optional
     - Crie uma senha para o usuário:
       - I want to create an IAM user
       - Custom password
       - Desmarque a opção que exige que o usuário crie uma nova senha quando conectar:
         - Users must create a new password at next sign-in (recommended).
     - Clique em "NEXT":
     - Agora ele vai pergunta se você desejar colocar o usuário em algum grupo:
       - Crie um GRUPO = Administrators
       - Marque a opção:
         - AdministratorAccess
     - Marque o grupo que você criou em clique em "NEXT"
     - Por fim clique em "Crate user"
     - Agora ele vai lhe dar um retorno com:
       - Console sign-in URL:
         - https://109710384575.signin.aws.amazon.com/console
       - User name:
         - drigols
       - Console password:
         - `***************`

---

<div id="rds"></div>

## Criando um Banco de Dados RDS (Relational Database Service) na AWS

Agora vamos criar um Banco de Dados Postgre na AWS utilizando o serviço **RDS (Relational Database Service)**:

 - Primeiro pesquisa por RDS.
 - Clique em "DB Instances (0/40)".
 - Create Database.
 - Escolha o banco de dados Postgre.
 - Escolha o nível gratúito (Free tier).
 - Escolha o nome da **instância do servidor** *(DB instance identifier)*:
   - **server**
 - Escolha o nome do usuário principal (Master username):
   - Eu poderia colocar ADM, Root.
   - Porém, vamos manter como **"postgres"** que já é quase padrão para quem trabalhar com Database e Postgres.
 - Escolha uma senha de conexão (Master password + Confirm master password):
   - `skX45837V&8h`
 - Escolha a opção de acesso público ao Banco de Dados *(Public access)*:
   - Ou seja, a AWS vai gerar um IP (DNS) público para quem deseja acessar o Banco de Dados.
 - Agora escolha o nome do Banco de Dados em "Additional configuration" > "Initial database name":
   - `coins`
 - Habilite proteção contra exclusão:
   - Additional configuration > Deletion protection > Enable deletion protection
   - Ou seja, ninguém vai conseguir apaga esse Banco de Dados sem querer.
   - Para apagar esse Banco de Dados, será necessário entrar nessa instância na AWS e desabilitar essa opção manualmente para só depois conseguir apagar esse Banco de Dados.
 - Finalmente clique em criar banco de dados:
   - Pode demorar algum tempo.
 - **NOTE:**  
   - **Liberando a porta "5432" na instância:**
     - Depois que a nossa instância (server) e o Banco de Dados for criado nós precisamos liberar a porta *"5432"* qual o postgres trabalhar.
     - Para isso clique em:
       - Security > VPC security groups > default (sg-014a5d44163dcec9b);
       - Procure por regras de entrada (Inbound Rules):
         - Editar regras de entrada (Edit Inbound Rules):
           - Coloque meu ip (My IP) source e clique em *"Save Rules"*.

![img](images/inbound-rules.png)  

---

<div id="testing-aws-db"></div>

## Testando conexão com o Banco de Dados na AWS (Database Client extension)

Agora vamos tentar nos conectar com o Banco de Dados na AWS utilizando a extensão Database Client no VSCode:

![img](images/testing-db.png)  

---

<div id="testing-api-db"></div>

## Pegando dados da API coinmarketcap e salvando no Banco de Dados

Os dados que nós vamos consumir vem da API [CoinMarketCap](https://coinmarketcap.com/api/) e depois serão salvos em um Banco de Dados Postgres na AWS. Para entender como foi feito o processo veja o [Jupyter Notebook clicando aqui](notebooks/api-and-db.ipynb).

Agora que você entendeu as partes do código para consumir os dados da API e salvar em um Banco de Dados na AWS, veja os códigos completo a seguir:

[app.py](ingestao-rds/app.py)
```python
from sqlalchemy.orm import declarative_base
from requests import Session
from model import Coins

import pandas as pd
import json


def check_if_valid_data(df: pd.DataFrame) -> bool:
    
    # Check if dataframe is empty
    if df.empty:
        print("\nDataframe empty. Finishing execution")
        return False 

    # Check for nulls
    if df.symbol.empty:
        raise Exception("\nSymbol is Null or the value is empty")
 
     # Check for nulls
    if df.price.empty:
        raise Exception("\nPrice is Null or the value is empty")

    # Check for nulls
    if df.data_added.empty:
        raise Exception("\nData is Null or the value is empty")

    return True


def load_data(table_name, coins_df, session_db, engine_db):
    
    # validate
    if check_if_valid_data(coins_df):
        print("\nData valid, proceed to Load stage")
    
    # load data on database
    try:
        coins_df.to_sql("tb_coins", engine_db, if_exists='append', index=False)
        print ('\nData Loaded on Database')
    except Exception as err:
        print(f"\nFail to load data on database: {err}")

    session_db.commit()
    session_db.close()
    print("\nClose database successfully")
    return session_db


def get_data(session_db, engine_db, start, limit, convert, key, url):
    
    # set limit of data from api
    parameters = {
        'start': start,
        'limit': limit,
        'convert': convert
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }

    session = Session()
    session.headers.update(headers)

    name = []
    symbol = []
    data_added = []
    last_updated = []
    price = []
    volume_24h = []
    circulating_supply = []
    total_supply = []
    max_supply = []
    volume_24h = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        print ('\n')
        for coin in data['data']:
            name.append(coin['name'])
            symbol.append(coin['symbol'])
            data_added.append(coin['date_added'])
            last_updated.append(coin['last_updated'])
            circulating_supply.append(coin['circulating_supply'])
            total_supply.append(coin['total_supply'])
            max_supply.append(coin['max_supply'])
            price.append(coin['quote']['USD']['price'])
            volume_24h.append(coin['quote']['USD']['volume_24h'])
            percent_change_1h.append(coin['quote']['USD']['percent_change_1h'])
            percent_change_24h.append(coin['quote']['USD']['percent_change_24h'])
            percent_change_7d.append(coin['quote']['USD']['percent_change_7d'])

        # Prepare a dictionary in order to turn it into a pandas dataframe below.    
        coin_dict = {
            "name" : name,
            "symbol": symbol,
            "data_added" : data_added,
            "last_updated" : last_updated,
            "price": price,
            "volume_24h": volume_24h,
            "circulating_supply" : circulating_supply,
            "total_supply": total_supply,
            "max_supply": max_supply,
            "volume_24h": volume_24h,
            "percent_change_1h": percent_change_1h,
            "percent_change_24h": percent_change_24h,
            "percent_change_7d": percent_change_7d
        }
    except Exception as e:
        print (f'Error to get data from APi: {e}')
        exit(1)
    
    # Create dataframe to structure data.
    coins_df = pd.DataFrame(coin_dict, columns = ["name", "symbol", "data_added", "last_updated","price","volume_24h","circulating_supply","total_supply","max_supply","percent_change_1h","percent_change_24h","percent_change_7d"])
    print ("Data on Pandas Dataframe:\n")
    print(coins_df.head(100))
    
    # Call the function to load data on database.
    load_data('tb_coins', coins_df, session_db, engine_db)


# Declaration base.
Base = declarative_base()

# Make the coin table.
get_session_db, get_engine = Coins.start()

# Call the get_data function and load data on database.
get_data(
    get_session_db,
    get_engine,
    '1',
    '5000',
    'USD',
    '7e8d0c0c-187a-4e0e-830a-5bbc92a73486',
    'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
)
```

[model.py](ingestao-rds/model.py)
```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Coins(Base):
    __tablename__ = 'tb_coins'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String)
    symbol = Column(String)
    data_added = Column(Text)
    last_updated = Column(Text)
    price = Column(Float)
    volume_24h = Column(Float)
    circulating_supply = Column(Float)
    total_supply = Column(Float)
    max_supply = Column(Float)
    volume_24h = Column(Float)
    percent_change_1h = Column(Float)
    percent_change_24h = Column(Float)
    percent_change_7d = Column(Float)

    def start():
        db_string = "postgresql://postgres:skX45837V&8h@server.ceukrpnlio5b.us-east-1.rds.amazonaws.com:5432/coins"
        engine = create_engine(db_string)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        print ('\nTable created on database')
        return session, engine
```

---

<div id="data-lake-s3"></div>

## Criando o Data Lake (Buckets) na AWS com S3

 - Pesquise por "S3" na AWS.
   - Clique no serviço.
 - **Criando os Buckets:**
   - **Clique em "Create Bucket":**
     - Coloqueo o nome do Bucket (Bucket name):
       - "raw-nomedoprojecto"
       - raw = Os dados mais brutos possíveis  (os Cientistas NÃO TEM ACESSO).
       - nomedoprojecto = O nome do projeto a qual o bucket pertence.
     - Adicione uma Tag ao Bucket (Tags(1) - optional -> Add Tag):
       - Key=Projeto, Value=Bootcamp.
       - Key=Team, Value=Stack.
       - Key=CentroCusto, Value=TI.
     - Finalmente, clique em "Create Bucket".
   - **Clique novamente em "Create Bucket"**
     - Coloqueo o nome do Bucket (Bucket name):
       - "processed-nomedoprojecto"
       - processed = Onde os dados já estão processados (os Cientistas de Dados TEM ACESSO).
       - nomedoprojecto = O nome do projeto a qual o bucket pertence.
     - Adicione uma Tag ao Bucket (Tags(1) - optional -> Add Tag):
       - Key=Projeto, Value=Bootcamp.
       - Key=Team, Value=Stack.
       - Key=CentroCusto, Value=TI.
     - Finalmente, clique em "Create Bucket".
   - **Clique novamente em "Create Bucket"**
     - Coloqueo o nome do Bucket (Bucket name):
       - "curated-nomedoprojecto"
       - curated = Aqui são os dados finais. Ou seja, já podemos disponibilizar ele para o time de negócio ou fazer um Dashboard para os stackholders.
       - nomedoprojecto = O nome do projeto a qual o bucket pertence.
     - Adicione uma Tag ao Bucket (Tags(1) - optional -> Add Tag):
       - Key=Projeto, Value=Bootcamp.
       - Key=Team, Value=Stack.
       - Key=CentroCusto, Value=TI.
     - Finalmente, clique em "Create Bucket".

---

<div id="dms"></div>

## Criando o DMS (Database Migration Service) na AWS

 - Agora pesquise por DMS (Database Migration Service) na AWS:
   - Clique nele.
   - Clique em "Create Application Instance".
   - Coloque o nome da instância:
     - "dms-instance-01".
   - Coloque uma descrição:
     - "Serviço de Ingestão para o Data Lake".
   - Configure a instância da máquina (Instance configuration):
     - Engine Version = 3.4.6.
     - Multi AZ = Single.AZ.
   - Remova acesso público (Public accessible).
   - Adicione Tags:
     - Key=Projeto, Value=Bootcamp.
     - Key=Team, Value=Stack.
     - Key=CentroCusto, Value=TI.
   - Finalmente, clique em "Create Application Instance".

---

<div id="endpoints-dms"></div>

## Criando Endpoints no DMS na AWS

> Os "Endpoints" são uma forma de nós conectamos nossa "fonte" e um "target".

 - Clique em "Endpoints":
   - Clique em "Create endpoint":
     - Escolha o Endpoints do tipo "source".
     - Selecione a opção "Select RDS DB instance":
       - Selecione a nossa fonte de dados que vai ser o nosso Banco de Dados Postgre RDS = server.
     - Configure o Endpoint (Endpoint configuration):
       - Endpoint identifier = rd-source-postgresql
       - Provide access information manually: Suas credenciais de ADM no Postgre RDS:
         - Username: postgres
         - Password: skX45837V&8h
     - Adicione Tags:
       - Key=object, Value=endpoint.
   - Clique novamente em "Create endpoint":
     - Escolha o Endpoints do tipo "target".
     - **NOTE:** Os target vão ser os nossos "Buckets" no Data Lake.
     - Configure o Endpoint (Endpoint configuration):
       - Endpoint identifier = s3-target-datalake
       - Target engine = Amazon S3
       - Adicione o ARN (Service access role ARN):
         - arn:aws:iam::109710384575:role/Role-DMS-S3-raw
         - Essa regra/policy foi criada manualmente no vídeo.
       - Aponte para o **nome do Bucket** e o **diretório** que nós vamos escrever:
         - Bucket name = raw-nomedoprojecto
         - Bucket folder = Vamos deixar em branco, ou seja, ele vai escrever dentro da raiz.
     - Endpoint settings:
       - Add new setting:
         - AddColumnName + Value = true.
     - Adicione Tags:
       - Key=object, Value=endpoint-target.

---

<div id="settings"></div>

## Configurações do projeto

Configurações Python:

```
python -m venv environment
```

```python
# Linux Approach
source environment/bin/activate

# Windows Approach
source environment/Scripts/activate
```

```
python -m pip install --upgrade pip
```

---

**REFERENCES:**  
[Stack](https://www.youtube.com/@Stack_tecnologias)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
