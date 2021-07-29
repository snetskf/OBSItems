# encoding: utf-8
# module _hashlib
# from (pre-generated)
# by generator 1.147
""" OpenSSL interface for hashlib module """
# no imports

# functions

def compare_digest(*args, **kwargs): # real signature unknown
    """
    Return 'a == b'.
    
    This function uses an approach designed to prevent
    timing analysis, making it appropriate for cryptography.
    
    a and b must both be of the same type: either str (ASCII only),
    or any bytes-like object.
    
    Note: If a and b are of different lengths, or if an error occurs,
    a timing attack could theoretically reveal information about the
    types and lengths of a and b--but not their values.
    """
    pass

def get_fips_mode(*args, **kwargs): # real signature unknown
    """
    Determine the OpenSSL FIPS mode of operation.
    
    For OpenSSL 3.0.0 and newer it returns the state of the default provider
    in the default OSSL context. It's not quite the same as FIPS_mode() but good
    enough for unittests.
    
    Effectively any non-zero return value indicates FIPS mode;
    values other than 1 may have additional significance.
    """
    pass

def hmac_digest(*args, **kwargs): # real signature unknown
    """ Single-shot HMAC. """
    pass

def hmac_new(*args, **kwargs): # real signature unknown
    """ Return a new hmac object. """
    pass

def new(*args, **kwargs): # real signature unknown
    """
    Return a new hash object using the named algorithm.
    
    An optional string argument may be provided and will be
    automatically hashed.
    
    The MD5 and SHA1 algorithms are always supported.
    """
    pass

def openssl_md5(*args, **kwargs): # real signature unknown
    """ Returns a md5 hash object; optionally initialized with a string """
    pass

def openssl_sha1(*args, **kwargs): # real signature unknown
    """ Returns a sha1 hash object; optionally initialized with a string """
    pass

def openssl_sha224(*args, **kwargs): # real signature unknown
    """ Returns a sha224 hash object; optionally initialized with a string """
    pass

def openssl_sha256(*args, **kwargs): # real signature unknown
    """ Returns a sha256 hash object; optionally initialized with a string """
    pass

def openssl_sha384(*args, **kwargs): # real signature unknown
    """ Returns a sha384 hash object; optionally initialized with a string """
    pass

def openssl_sha3_224(*args, **kwargs): # real signature unknown
    """ Returns a sha3-224 hash object; optionally initialized with a string """
    pass

def openssl_sha3_256(*args, **kwargs): # real signature unknown
    """ Returns a sha3-256 hash object; optionally initialized with a string """
    pass

def openssl_sha3_384(*args, **kwargs): # real signature unknown
    """ Returns a sha3-384 hash object; optionally initialized with a string """
    pass

def openssl_sha3_512(*args, **kwargs): # real signature unknown
    """ Returns a sha3-512 hash object; optionally initialized with a string """
    pass

def openssl_sha512(*args, **kwargs): # real signature unknown
    """ Returns a sha512 hash object; optionally initialized with a string """
    pass

def openssl_shake_128(*args, **kwargs): # real signature unknown
    """ Returns a shake-128 variable hash object; optionally initialized with a string """
    pass

def openssl_shake_256(*args, **kwargs): # real signature unknown
    """ Returns a shake-256 variable hash object; optionally initialized with a string """
    pass

def pbkdf2_hmac(*args, **kwargs): # real signature unknown
    """ Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function. """
    pass

def scrypt(*args, **kwargs): # real signature unknown
    """ scrypt password-based key derivation function. """
    pass

# classes

class HASH(object):
    """
    A hash is an object used to calculate a checksum of a string of information.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided string. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HASHXOF(HASH):
    """
    A hash is an object used to calculate a checksum of a string of information.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest(length) -- return the current digest value
    hexdigest(length) -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HMAC(object):
    """
    The object used to calculate HMAC of a message.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the name, including the hash algorithm used by this object
    digest_size -- number of bytes in digest() output
    """
    def copy(self, clone): # real signature unknown; restored from __doc__
        """ Return a copy ("clone") of the HMAC object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest of the bytes passed to the update() method so far. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """
        Return hexadecimal digest of the bytes passed to the update() method so far.
        
        This may be used to exchange the value safely in email or other non-binary
        environments.
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update the HMAC object with msg. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

openssl_md_meth_names = None # (!) real value is "frozenset({'shake_128', 'sha512_224', 'md5-sha1', 'sha1', 'sha384', 'shake_256', 'sha3_384', 'sha512_256', 'whirlpool', 'blake2s', 'sha3_224', 'sha3_512', 'sm3', 'sha512', 'sha256', 'mdc2', 'ripemd160', 'sha3_256', 'md5', 'sha224', 'md4', 'blake2b'})"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002089E7BA970>'

__spec__ = None # (!) real value is "ModuleSpec(name='_hashlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002089E7BA970>, origin='C:\\\\BuildAgent\\\\system\\\\.persistent_cache\\\\pycharm\\\\pythons4utils\\\\python39\\\\DLLs\\\\_hashlib.pyd')"

