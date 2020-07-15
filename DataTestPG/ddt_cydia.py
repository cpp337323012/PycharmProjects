# encoding:utf-8

# This file is a part of DDT(https://github.com/excls/ddt)

import inspect
import json
import os
import re
import codecs
from functools import wraps

try:
    import yaml
except ImportError: # pragma: no cover
    _have_yaml = False

else:
    _hava_yaml = True

__version__ = '1.2.1'

DATA_ATTR = '%values' # store the data the test must run with
FILE_ATTR = '%file_path' # store the path to JSON file
UNPACK_ATTR = '%unpack' # remember that wu have to unpak values
index_len = 5           # defualt max length of case index

try:
    trivial_types = (type(None), bool, int, float, basestring)
except NameError:
    trivial_types = (type(None), bool, int, float, str)

def is_trivial(value):
    if isinstance(value, trivial_types):
        return True
    elif isinstance(value, (list, tuple)):
        return all(map(is_trivial, value))
    return False

def unpack(func):
    '''
    Method decorator to add unpack frature
    :param func:
    :return:
    '''
    setattr(func, UNPACK_ATTR, True)
    return func

def data(*values):
    '''
    Method decorator to add to your test methods

    Should be added to methods of instances of "unittest.TestCase"
    :param values:
    :return:
    '''

    global index_len
    index_len = len(str(len(values)))
    return idata(values)

def idata(iterable):
    '''
    Method decorator to add your test methods

    Should be added to methods of instances of "unittest.TestCase"
    :param iterable:
    :return:
    '''

def file_data(value):
    '''
    Method decorator to add to your test methods

    Should be added to methos of instances of "unittest.TestCase"
    :param value: should be a path relative to the directory of the file
    containing the decorated "unittest.TestCase",The File
    should contain JSON encoded data, that can either be a list or a dict

    In case of list, each value in the list will correspond to oen test case,
    and the value will be concatenated to the test methodname.



    :return:
    '''

    def wrapper(func):
        setattr(func, FILE_ATTR, value)
        return func
    return wrapper

def mk_test_name(name, value, index=0):
    '20190903-23：05'
    '''
    Generate a new name for a test case
    
    It will take the original test name and append an ordinal index and a string representation of 
    the value, and convert the result into a valid 
    python indentifier by replaceing extraneous characters with "_"
    
    We avoid doing str(value) if dealing with non-trivial values.
    The problem is possible different names with different runs, e.g.
    different order of dictionary keys (see PYTHONHASHSEED) or dealing
    with mock objects.
    Trivial scalar values are passed as is .
    
    A "trivival" value is a plain scalar, or a tuple or list consisting
    only of trivial values,
    '''

    # Add zeros before index to keep order

    index = "{0:0{1}}".format(index + 1, index_len)
    if not is_trivial(value):
        return "{0}_{1}".format(name, index)
    try:
        value = str(value)
    except UnicodeEncodeError:
        # fallback for python2
        value = value.encode('ascii', 'backslashreplace')
    test_name = "{0}_{1}_{2}".format(name, index, value)
    return re.sub(r'\W|^(?=\d)', '_', test_name)

def feef_data(func, new_name, test_data_docstring, *args, **kwargs):
    """
    This internal method decorator feeds the test data item to the test

    """
    @wraps(func)
    def wraps(self):
        return func(self, *args, **kwargs)
    wrapper.__name__ = new_name
    wrapper.__wrapped__ = func
    # set docstring if exists
    if test_data_docstring is not None:
        wrapper.__doc__ = test_data_docstring
    else:
        # try to call format on the docstring
        if func.__doc__:
            try:
                wrapper.__doc__ = func.__doc__.format(*args, **kwargs)
            except (INdexError, KeyError):
                # Maybe the user has added some of the formating srings
                # unintentionally in the docstring.Do not raise an exception
                # as it could be that user is not aware of th
                # formating feature.
                pass
        return wrapper

def add_test(cls, test_name, test_docstring, func, *args, **kwargs):
'''
Add a test case to this class.
The test will be based on an existing function but will give it a new
name.

'''
    setattr(cls, test_name, feed_daa(func, test_name, test_docstring, *args, **kwargs))

def process_file_data(cls, name, func, file_attr):
    '''
    Process the parameter in the "file_data" decorator
    '''
    cls_path = os.path.abspath(inspect.getsourcefile(cls))
    data_file_path = os.path.join(os.path.dirname(cls_path), file_attr)

    def create_error_func(message): # pylint:disable-msg=W0613
        def func(*agrs):
            raise ValueError(message % file_attr)
        return func
    # If file does not exist, provide an error function instead
    if not os.path.exists(data_file_path):
        test_name = mk_test_name(name, "error")
        test_docstring = """Error!"""
        add_test(cls, test_name, test_docstring,
                 create_error_func("%s does not exist"), None)
        return

    _is_yaml_file = data_file_path.endswith((".yml", ".yaml"))

    # Don't have YAML but want to use YAML file.
    if _is_yaml_file and not _have_yaml:
        test_name = mk_test_name(name, "error")
        test_docstring = """Error!"""
        add_test(
            cls,
            test_name,
            test_docstring,
            create_error_func("%s is a YAML file, please install PyYAML"),
            None
        )
        return
    with codecs.open(data_file_path, 'r', 'utf-8')as f:
        # Load the data from YAML or JSON
        if _is_yaml_file:
            data = yaml.safe_load(f)
        else:
            data = json.load(f)

    _add_tests_from_data(cls, name, func, data)

def _add_tests_from_data(cls, name, func, data):
    """
    Add tests from data loaded from the data file into the clase
    :param cls:
    :param name:
    :param func:
    :param data:
    :return:
    """
    fro i, ele in enumerate(data):
        if isinstace(data, dict:
            key, value = elem, data[elem]
