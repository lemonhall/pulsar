'''\
Simple python script which helps writing python 2.6 \
forward compatible code with python 3'''
import os
import sys
import types

ispy3k = sys.version_info[0] == 3

UTF8 = 'utf-8'

if ispy3k: # Python 3
    ispy32 = sys.version_info[1] >= 2
    string_type = str
    itervalues = lambda d : d.values()
    iteritems = lambda d : d.items()
    int_type = int
    zip = zip
    map = map
    range = range
    from io import BytesIO, StringIO
    import pickle
    i2b = lambda n : bytes((n,))
    
    class UnicodeMixin(object):
        
        def __unicode__(self):
            return '{0} object'.format(self.__class__.__name__)
        
        def __str__(self):
            return self.__unicode__()
        
        def __repr__(self):
            return '%s: %s' % (self.__class__.__name__,self)
    
    def execfile(filename, globals=None, locals=None):
        if globals is None:
            globals = sys._getframe(1).f_globals
        if locals is None:
            locals = sys._getframe(1).f_locals
        with open(filename, "r") as fh:
            exec(fh.read()+"\n", globals, locals)
            
    def raise_error_trace(err,traceback):
        raise err.with_traceback(traceback)
            
else: # Python 2
    ispy32 = False
    string_type = unicode
    execfile = execfile
    itervalues = lambda d : d.itervalues()
    iteritems = lambda d : d.iteritems()
    int_type = (types.IntType, types.LongType)
    from itertools import izip as zip, imap as map
    from ._py2 import *
    range = xrange
    
    i2b = lambda n : chr(n)
    
    from cStringIO import StringIO
    BytesIO = StringIO
    
    import cPickle as pickle    
    
    class UnicodeMixin(object):
        
        def __unicode__(self):
            return unicode('{0} object'.format(self.__class__.__name__))
        
        def __str__(self):
            return self.__unicode__().encode()
        
        def __repr__(self):
            return '%s: %s' % (self.__class__.__name__,self)
    


        