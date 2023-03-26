import kabbes_pypi_builder
import kabbes_garden
import kabbes_client
import py_starter as ps

class Client( kabbes_garden.Garden ):

    _BASE_DICT = {}

    def __init__( self, dict={} ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        self.Package = kabbes_client.Package( kabbes_garden._Dir, dict=d )
        self.cfg = self.Package.cfg

        kabbes_garden.Garden.__init__( self )
