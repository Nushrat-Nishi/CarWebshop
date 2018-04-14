from pyramid.config import Configurator
from .factory.db_session_factory import DbSessionFactory

def init_db(config):
    DbSessionFactory.global_init()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()

    init_db(config)

    return config.make_wsgi_app()
