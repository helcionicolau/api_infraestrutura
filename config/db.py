from sqlalchemy import create_engine, MetaData

# Conexão com o MySQL
# Dados de conexão
usuario = '331882_maxalert'
senha = 'kjdhi%%##$'
servidor = 'mysql-securegestdb.alwaysdata.net'

# Nome das bases de dados
nome_bd_principal = 'securegestdb_bd_maxalert_principal'
nome_bd_infraestrutura = 'securegestdb_bd_infraestrutura'

# String de conexão
con_principal_str = f"mysql+pymysql://{usuario}:{senha}@{servidor}/{nome_bd_principal}"
con_infra_str = f"mysql+pymysql://{usuario}:{senha}@{servidor}/{nome_bd_infraestrutura}"

# Criar engines e metadados
engine_principal = create_engine(con_principal_str)
meta_principal = MetaData(bind=engine_principal)

engine_infra = create_engine(con_infra_str)
meta_infra = MetaData(bind=engine_infra)

# Conexão com o banco de dados
con_principal = engine_principal.connect()
con_infra = engine_infra.connect()