from parent_class import ParentClass
import platform
import dir_ops as do
import py_starter as ps

class Garden( ParentClass ):

    def __init__( self ):
        ParentClass.__init__( self )
        self.get_repo_Dirs()
        self.get_src_Dirs()
        self.get_package_Dirs()
        #self.write_packages()
        self.write_repos()

    def get_repo_Dirs( self ):
        self.repo_Dirs = self.cfg[ 'user_profile.packages.Dir' ].list_contents_Paths( block_dirs = False, block_paths =True )

    def get_src_Dirs( self ):
        self.src_Dirs = do.Dirs()
        for repo_Dir in self.repo_Dirs:
            self.src_Dirs._add( repo_Dir.join_Dir( path = self.cfg['src_name'] ) )    

    def get_package_Dirs( self ):
        self.package_Dirs = do.Dirs()
        for src_Dir in self.src_Dirs:
            for package_Dir in src_Dir.list_contents_Paths( block_dirs=False, block_paths=True,  ):
                if not package_Dir.dirs[-1].endswith( '.egg-info' ):
                    self.package_Dirs._add( package_Dir )


    def write_packages( self ):
        string = '\n'.join( [ Dir.dirs[-1] for Dir in self.package_Dirs ] )
        self.cfg['packages.Path'].write( string=string, overwrite=True)

    def write_repos( self ):
        string = '\n'.join( [ Dir.dirs[-1] for Dir in self.repo_Dirs ] )
        self.cfg['repos.Path'].write( string=string, overwrite=True)

    def export_pythonpath( self, override:bool=False ):

        joined_pythonpath = do.join_env_var_paths( [Dir.path for Dir in self.src_Dirs] )
        print ('PYTHONPATH')
        print (joined_pythonpath)

        if not override:
            override = self.cfg['override']
        if not override:
            override = ps.confirm_raw( string='This will export to your PYTHONPATH' )
        if not override:
            return

        if platform.system() == 'Darwin' or platform.system() == 'Linux':
            string = 'export ' + self.cfg['pythonpath_key'] + '=' + joined_pythonpath
            self.cfg['user_profile.environment.Path'].write( string = string, overwrite=True )

        else:
            print ('No instructions for exporting PYTHONPATH yet')



