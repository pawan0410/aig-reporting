import pymssql
from emr.config import Config
from flask import current_app


class MedStreaming(object):

    def __init__(self):
        try:
            self.connection = pymssql.connect(
                Config.MSSQL_HOST,
                Config.MSSQL_USERNAME,
                Config.MSSQL_PASSWORD,
                "Medstreaming"
            )
        except pymssql.OperationalError as e:
            self.connection = None
            current_app.logger.log(e.message)

    @classmethod
    def cursor(cls):
        return cls.connection.cursor(as_dict=True)


class MedStreamingEMRDataDb(object):

    def __init__(self):
        try:
            self.connection = pymssql.connect(
                Config.MSSQL_HOST,
                Config.MSSQL_USERNAME,
                Config.MSSQL_PASSWORD,
                "MedstreamingEMRDATADB"
            )
        except pymssql.OperationalError as e:
            self.connection = None
            current_app.logger.log(e.message)

    @classmethod
    def cursor(cls):
        return cls.connection.cursor(as_dict=True)


class MedStreamingEMRDB(object):

    def __init__(self):
        try:
            self.connection = pymssql.connect(
                Config.MSSQL_HOST,
                Config.MSSQL_USERNAME,
                Config.MSSQL_PASSWORD,
                "MedstreamingEMRDB"
            )
        except pymssql.OperationalError as e:
            self.connection = None
            current_app.logger.log(e.message)

    @classmethod
    def cursor(cls):
        return cls.connection.cursor(as_dict=True)

