#!/usr/local/bin/python2.7
##
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##
__author__ = 'Jeff Roy'

from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.presf_abc_dcl import PresfAbcDclParser
from mi.core.versioning import version


@version("15.6.1")
def parse(unused, sourceFilePath, particleDataHdlrObj):
    """
    This is the method called by Uframe
    :param unused
    :param sourceFilePath This is the full path and filename of the file to be parsed
    :param particleDataHdlrObj Java Object to consume the output of the parser
    :return particleDataHdlrObj
    """

    with open(sourceFilePath, 'rU') as stream_handle:

        # create and instance of the concrete driver class defined below
        driver = PresfAbcDclRecoveredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class PresfAbcDclRecoveredDriver(SimpleDatasetDriver):
    """
    Derived presf_abc_dcl driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        parser = PresfAbcDclParser(stream_handle, self._exception_callback, False)

        return parser


