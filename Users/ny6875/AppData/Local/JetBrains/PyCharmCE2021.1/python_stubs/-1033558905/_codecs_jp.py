# encoding: utf-8
# module _codecs_jp
# from (built-in)
# by generator 1.147
# no doc
# no imports

# functions

def getcodec(*args, **kwargs): # real signature unknown
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod object at 0x000001E67E596460>, 'find_spec': <classmethod object at 0x000001E67E596490>, 'find_module': <classmethod object at 0x000001E67E5964C0>, 'create_module': <classmethod object at 0x000001E67E5964F0>, 'exec_module': <classmethod object at 0x000001E67E596520>, 'get_code': <classmethod object at 0x000001E67E5965B0>, 'get_source': <classmethod object at 0x000001E67E596640>, 'is_package': <classmethod object at 0x000001E67E5966D0>, 'load_module': <classmethod object at 0x000001E67E596700>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__map_cp932ext = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC3810>'

__map_jisx0208 = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC3540>'

__map_jisx0212 = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC3570>'

__map_jisx0213_1_bmp = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC36C0>'

__map_jisx0213_1_emp = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC3750>'

__map_jisx0213_2_bmp = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC36F0>'

__map_jisx0213_2_emp = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC3780>'

__map_jisx0213_bmp = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC3720>'

__map_jisx0213_emp = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC37B0>'

__map_jisx0213_pair = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC37E0>'

__map_jisxcommon = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001E67FCC35D0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_codecs_jp', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

