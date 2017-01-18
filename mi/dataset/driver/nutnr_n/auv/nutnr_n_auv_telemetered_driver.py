#!/usr/bin/env python

"""
@package mi.dataset.driver.nutnr_n.auv
@file mi/dataset/driver/nutnr_n/auv/nutnr_n_auv_telemetered_driver.py
@author Jeff Roy
@brief Driver for the nutnr_n_auv instrument

Release notes:

Initial Release
"""

from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.nutnr_n_auv import NutnrNAuvParser
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
        driver = NutnrNAuvTelemeteredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class NutnrNAuvTelemeteredDriver(SimpleDatasetDriver):
    """
    Derived nutnr_n_auv driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        parser = NutnrNAuvParser(stream_handle,
                                 self._exception_callback)

        return parser


