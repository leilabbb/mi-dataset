#!/usr/bin/env python

"""
@package mi.dataset.driver.adcps_jln.sio
@file mi-dataset/mi/dataset/driver/adcps_jln/sio/adcps_jln_sio_telemetered_driver.py
@author Joe Padula
@brief Telemetered driver for the adcps_jln_sio instrument

Release notes:

Initial Release
"""

from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.adcps_jln_sio import AdcpsJlnSioParser
from mi.core.versioning import version


@version("15.6.2")
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
        driver = AdcpsJlnSioTelemeteredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class AdcpsJlnSioTelemeteredDriver(SimpleDatasetDriver):
    """
    The adcps_jln_sio driver class extends the SimpleDatasetDriver.
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        parser_config = {
            DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.adcps_jln_sio',
            DataSetDriverConfigKeys.PARTICLE_CLASS: 'AdcpsJlnSioDataParticle'
        }

        parser = AdcpsJlnSioParser(parser_config,
                                   stream_handle,
                                   self._exception_callback)

        return parser
