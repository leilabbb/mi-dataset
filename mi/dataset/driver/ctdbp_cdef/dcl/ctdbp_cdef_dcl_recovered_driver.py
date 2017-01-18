#!/usr/bin/env python

"""
@package mi.dataset.driver.ctdbp_cdef.dcl
@file mi-dataset/mi/dataset/driver/ctdbp_cdef/dcl/ctdbp_cdef_dcl_recovered_driver.py
@author Jeff Roy
@brief Driver for the ctdbp_cdef_dcl instrument (Recovered Data)

Release notes:

Initial Release
"""

from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.ctdbp_cdef_dcl import CtdbpCdefDclParser
from mi.core.versioning import version

MODULE_NAME = 'mi.dataset.parser.ctdbp_cdef_dcl'


@version("15.7.1")
def parse(unused, sourceFilePath, particleDataHdlrObj):
    """
    This is the method called by Uframe
    :param unused
    :param sourceFilePath This is the full path and filename of the file to be parsed
    :param particleDataHdlrObj Java Object to consume the output of the parser
    :return particleDataHdlrObj
    """

    with open(sourceFilePath, 'rU') as stream_handle:

        # create an instance of the concrete driver class defined below
        driver = CtdbpCdefDclRecoveredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class CtdbpCdefDclRecoveredDriver(SimpleDatasetDriver):
    """
    Derived ctdbp_cdef_dcl driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        # The parser inherits from simple parser - other callbacks not needed here
        parser = CtdbpCdefDclParser(False,
                                    stream_handle,
                                    self._exception_callback)

        return parser
