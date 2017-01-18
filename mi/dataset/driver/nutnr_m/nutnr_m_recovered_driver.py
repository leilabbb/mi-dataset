"""
@package mi.dataset.driver.nutnr_m
@file marine-integrations/mi/dataset/driver/nutnr_n/nutnr_m_recovered_driver.py
@author Emily Hahn
@brief Driver for the nutnr series m instrument
"""

from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.nutnr_m import NutnrMParser
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
        driver = NutnrMRecoveredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()
    return particleDataHdlrObj


class NutnrMRecoveredDriver(SimpleDatasetDriver):
    """
    Derived driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        return NutnrMParser(stream_handle, self._exception_callback)
