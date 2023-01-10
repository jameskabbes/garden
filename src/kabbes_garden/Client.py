import pypi_builder
import kabbes_garden
import kabbes_user_client
import py_starter as ps

class Client( kabbes_garden.Garden, pypi_builder.Client ):

    BASE_CONFIG_DICT = {
        "_Dir": kabbes_garden._Dir,
    }

    def __init__( self, dict={}, **kwargs ):

        pypi_builder.Client.__init__( self )
        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        overwrite_cfg = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        self.cfg.merge(overwrite_cfg)

        kabbes_garden.Garden.__init__( self )

