import os
class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    development configuration child class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}