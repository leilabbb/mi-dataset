#!/usr/bin/env python

"""
@package mi.dataset.driver.fdchp_a
@file mi/dataset/driver/fdchp_a/fdchp_a_recovered_driver.py
@author Emily Hahn
@brief Driver for the fdchp series a recovered instrument
"""

from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.fdchp_a import FdchpAParser
from mi.core.versioning import version


@version("15.7.1")
def parse(unused, sourceFilePath, particleDataHdlrObj):
    """
    This is the method called by Uframe
    :param unused
    :param sourceFilePath This is the full path and filename of the file to be parsed
    :param particleDataHdlrObj Java Object to consume the output of the parser
    :return particleDataHdlrObj
    """

    with open(sourceFilePath, 'rb') as stream_handle:

        # create and instance of the concrete driver class defined below
        driver = FdchpARecoveredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class FdchpARecoveredDriver(SimpleDatasetDriver):
    """
    Derived fdchp a driver class
    All this needs to do is create a concrete _build_parser method
    """
    def _build_parser(self, stream_handle):
        # build the parser
        return FdchpAParser(stream_handle, self._exception_callback)

