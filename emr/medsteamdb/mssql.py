import pymssql
from emr.config import Config
from flask import current_app


try:
    med_streaming_emr_db_connection = pymssql.connect(
        Config.MSSQL_HOST,
        Config.MSSQL_USERNAME,
        Config.MSSQL_PASSWORD,
        "MedstreamingEMRDB"
    )
    med_streaming_emr_db = med_streaming_emr_db_connection.cursor(as_dict=True)
except pymssql.OperationalError as e:
    current_app.logger.error(e)


try:
    med_streaming_connection = pymssql.connect(
        Config.MSSQL_HOST,
        Config.MSSQL_USERNAME,
        Config.MSSQL_PASSWORD,
        "Medstreaming"
    )
    med_streaming = med_streaming_connection.cursor(as_dict=True)
except pymssql.OperationalError as e:
    current_app.logger.error(e)


try:
    med_streaming_emr_data_db_connection = pymssql.connect(
        Config.MSSQL_HOST,
        Config.MSSQL_USERNAME,
        Config.MSSQL_PASSWORD,
        "MedstreamingEMRDATADB"
    )
    med_streaming_emr_data_db = med_streaming_emr_data_db_connection.cursor(as_dict=True)
except pymssql.OperationalError as e:
    current_app.logger.error(e)




