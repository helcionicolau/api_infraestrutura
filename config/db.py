# MYSQL
# from sqlalchemy import create_engine,MetaData
# engine=create_engine('mysql+pymysql://root@localhost:3306/bd_maxalert_principal')
# meta=MetaData()
# con=engine.connect()

# # SQLSERVER
# from sqlalchemy import create_engine, MetaData
# import urllib

# # Conexão com o SQL Server usando o Windows Authentication
# # Substitua 'server_name' e 'database_name' pelos valores reais do seu servidor SQL Server e do banco de dados.
# # Se necessário, inclua também outros parâmetros específicos de configuração do seu servidor.
# params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=DESKTOP-NHETBCR\SQLEXPRESS;DATABASE=bd_maxalert_principal;Trusted_Connection=yes;")
# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# # Metadados
# meta = MetaData()

# # Conexão com o banco de dados
# con = engine.connect()

from sqlalchemy import create_engine, MetaData
import urllib

# Conexão com o primeiro SQL Server
params_principal = {
    "server": "DESKTOP-NHETBCR\SQLEXPRESS",
    "database": "bd_maxalert_principal"
}

params_encoded_principal = urllib.parse.quote_plus(f"DRIVER={{SQL Server}};SERVER={params_principal['server']};DATABASE={params_principal['database']};Trusted_Connection=yes;")
engine_principal = create_engine(f"mssql+pyodbc:///?odbc_connect={params_encoded_principal}")
meta_principal = MetaData(bind=engine_principal)

# Conexão com o segundo SQL Server
params_infra = {
    "server": "DESKTOP-NHETBCR\SQLEXPRESS",
    "database": "bd_infraestrutura"
}

params_encoded_infra = urllib.parse.quote_plus(f"DRIVER={{SQL Server}};SERVER={params_infra['server']};DATABASE={params_infra['database']};Trusted_Connection=yes;")
engine_infra = create_engine(f"mssql+pyodbc:///?odbc_connect={params_encoded_infra}")
meta_infra = MetaData(bind=engine_infra)

# Conexão com o banco de dados
con_principal = engine_principal.connect()
con_infra = engine_infra.connect()
