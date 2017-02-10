"""
Configuration file
"""


class Config:
    """
    Base Configuration
    """

    DEBUG = True
    SECRET_KEY = r'f\x13\xd9fM\xdc\x82\x01b\xdb\x03'
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 120
    SQLALCHEMY_POOL_RECYCLE = 280
    MSSQL_HOST = '192.168.3.116'
    MSSQL_USERNAME = r'mednet\m.atul'
    MSSQL_PASSWORD = 'test123'


class DevelopmentConfig(Config):
    """
    Local Development
    """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/emr'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:maria@aig2016@127.0.0.1/emr'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
