import pymssql
from emr.config import Config


conn1 = pymssql.connect(Config.MSSQL_HOST, Config.MSSQL_USERNAME, Config.MSSQL_PASSWORD, "Medstreaming")

medstreaming = conn1.cursor(as_dict=True)

conn2 = pymssql.connect(Config.MSSQL_HOST, Config.MSSQL_USERNAME, Config.MSSQL_PASSWORD, "MedstreamingEMRDATADB")

medstreaming_emr_data_db = conn2.cursor(as_dict=True)

conn3 = pymssql.connect(Config.MSSQL_HOST, Config.MSSQL_USERNAME, Config.MSSQL_PASSWORD, "MedstreamingEMRDB")

medstreaming_emr_db = conn3.cursor(as_dict=True)

