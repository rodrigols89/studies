from os.path import abspath
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


"""Setup da Aplicação
Vejam que nós estamos definindo para o Spark trabalhar
com "Delta".
"""
spark = SparkSession \
    .builder \
    .appName("job-1-spark") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")\
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")\
    .getOrCreate()

# definindo o método de logging da aplicação use INFO somente para DEV [INFO,ERROR]
spark.sparkContext.setLogLevel("ERROR")



def read_csv(bucket, path):
    """Função para ler o arquivo .csv dentro do Bucket
    Args:
        bucket: Bucket na AWS
        path: Caminho para o arquivo dentro do Bucket na AWS.

    Returns:
        Retorno é um DataFrame com a tabela no Bucket.
    """
    # lendo os dados do Data Lake
    df = spark.read.format("csv")\
        .option("header", "True")\
        .option("inferSchema","True")\
        .csv(f"{bucket}/{path}")
    # imprime os dados lidos da raw
    print ("\nImprime os dados lidos da raw:")
    print (df.show(5))
    # imprime o schema do dataframe
    print ("\nImprime o schema do dataframe lido da raw:")
    print (df.printSchema())
    return df


def read_delta(bucket, path):
    """Função para ler dados no formato Delta.
    Args:
        bucket: Bucket na AWS
        path: Caminho para o arquivo dentro do Bucket na AWS.

    Returns:
        Retorno é o dado lido em formato Delta.
    """
    df = spark.read.format("delta")\
        .load(f"{bucket}/{path}")
    return df


def write_processed(bucket, path, col_partition, data_format, mode):
    """Função para escrever dados no Bucket processed.

    Args:
        bucket: Bucket na AWS
        path: Caminho para o arquivo dentro do Bucket na AWS.
        col_partition: Coluna de particionamento.
        data_format: Formato do Dado.
        mode: ???

    Returns:
        O retorno é 0 se tudo ocorrer como planejado ou 1 se houver erro.
    """
    print ("\nEscrevendo os dados lidos da raw para delta na processing zone...")
    try:
        df.write.format(data_format)\
            .partitionBy(col_partition)\
            .mode(mode)\
            .save(f"{bucket}/{path}")
        print (f"Dados escritos na processed com sucesso!")
        return 0
    except Exception as err:
        print (f"Falha para escrever dados na processed: {err}")
        return 1


def write_curated(bucket, path, dataframe, data_format, mode):
    """Função para escrever no Bucket curated.

    Args:
        bucket: Bucket na AWS
        path: Caminho para o arquivo dentro do Bucket na AWS.
        dataframe: DataFrame a ser inserido.
        data_format: Formato do dado.
        mode: ???

    Returns:
        O retorno é 0 se tudo ocorrer como planejado ou 1 se houver erro.
    """
    # converte os dados processados para parquet e escreve na curated zone
    print ("\nEscrevendo os dados na curated zone...")
    try:
        dataframe.write.format(data_format)\
                .mode(mode)\
                .save(f"{bucket}/{path}")
        print (f"Dados escritos na curated com sucesso!")
        return 0
    except Exception as err:
        print (f"Falha para escrever dados na processed: {err}")
        return 1


#def write_redshift(url_jdbc, table_name, dataframe):
#    """_summary_
#
#    Args:
#        url_jdbc: _description_
#        table_name: _description_
#        dataframe: _description_
#
#    Returns:
#        _type_: _description_
#    """
#    try:
#        dataframe.write.format("jdbc")\
#                .options(url=url_jdbc,
#                        driver='com.amazon.redshift.jdbc42.Driver',
#                        user='awsuser',
#                        password='U%SlC7*Y807n',
#                        dbtable=table_name
#                        )\
#                .mode('overwrite')\
#                .save()
#        print (f"Dados escritos no Redshift com sucesso!")
#        return 0
#    except Exception as err:
#        print (f"Falha para escrever dados no Redshift: {err}")
#        return 1


def analytics_tables(bucket, dataframe, table_name, flag_write_redshift, url_jdbc):
    """_summary_

    Args:
        bucket: _description_
        dataframe: _description_
        table_name: _description_
        flag_write_redshift: _description_
        url_jdbc: _description_
    """
    # cria uma view para trabalhar com sql
    dataframe.createOrReplaceTempView(table_name)
    # processa os dados conforme regra de negócio
    df_query1 = df.groupBy("name") \
                .agg(sum("circulating_supply").alias("circulating_supply")) \
                .sort(desc("circulating_supply")) \
                .limit(10)
    df_query2 = df.select(col('name'),col('symbol'),col('price'))\
                .sort(desc("price"))\
                .limit(10)
    # imprime o resultado do dataframe criado
    print ("\n Top 10 Cryptomoedas com maior fornecimento de circulação  no mercado\n")
    print (df_query1.show())
    print ("\n Top 10 Cryptomoedas com preços mais altos de 2022\n")
    print (df_query2.show())
    write_curated(f"{bucket}","coins_circulating_supply",df_query1,"delta","overwrite")
    write_curated(f"{bucket}","top10_prices_2022",df_query2,"delta","overwrite")

    #if flag_write_redshift == True:
    #    write_redshift(url_jdbc, "coins_circulating_supply", df_query1)
    #    write_redshift(url_jdbc,"top10_prices_2022",df_query2)


# Ler dados da raw
df = read_csv('arn:aws:s3:::raw-nomedoprojecto','tb_coins')
#df = read_csv('s3a://raw-stack-bootcampde','tb_coins')

# Cria uma coluna de ano para particionar os dados
df = df.withColumn("year", year(df.data_added))

# Processa os dados e escreve na camada processed
write_processed("arn:aws:s3:::processed-nomedoprojecto", "tb_coins", "year", "delta", "overwrite")
#write_processed("s3a://processed-stack-bootcampde","tb_coins","year","delta","overwrite")

# Lear dados da processed e escreve na camada curated.
df = read_delta("arn:aws:s3:::processed-nomedoprojecto","tb_coins")
#df = read_delta("s3a://processed-stack-bootcampde","tb_coins")
analytics_tables("arn:aws:s3:::processed-nomedoprojecto", df, "tbl_coins")

#flag_write_redshift = True
#url_jdbc = "jdbc:redshift://redshift-cluster-1.cufcxu0ztur8.us-east-1.redshift.amazonaws.com:5439/dev"
#analytics_tables("s3a://curated-stack-bootcampde",df,"tb_coins", flag_write_redshift, url_jdbc)

# para a aplicação
spark.stop()
