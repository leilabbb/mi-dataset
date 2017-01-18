#!/usr/bin/env python

"""
@package mi.dataset.driver.dosta_abcdjm.sio
@file mi-dataset/mi/dataset/driver/dosta_abcdjm/sio/dosta_abcdjm_sio_telemetered_driver.py
@author Joe Padula
@brief Telemetered driver for the dosta_abcdjm_sio instrument

Release notes:

Initial Release
"""

__author__ = 'jpadula'

from mi.core.log import get_logger
log = get_logger()

from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.dosta_abcdjm_sio import DostaAbcdjmSioParser, \
    DATA_PARTICLE_CLASS_KEY, \
    METADATA_PARTICLE_CLASS_KEY, \
    DostaAbcdjmSioTelemeteredMetadataDataParticle, \
    DostaAbcdjmSioTelemeteredDataParticle
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
        driver = DostaAbcdjmSioTelemeteredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class DostaAbcdjmSioTelemeteredDriver(SimpleDatasetDriver):
    """
    The dosta_abcdjm_sio telemetered driver class extends the SimpleDatasetDriver.
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):
        log.debug('_build_parser entered')
        parser_config = {
            DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.dosta_abcdjm_sio',
            DataSetDriverConfigKeys.PARTICLE_CLASS: None,
            DataSetDriverConfigKeys.PARTICLE_CLASSES_DICT: {
                METADATA_PARTICLE_CLASS_KEY: DostaAbcdjmSioTelemeteredMetadataDataParticle,
                DATA_PARTICLE_CLASS_KEY: DostaAbcdjmSioTelemeteredDataParticle
            }
        }

        parser = DostaAbcdjmSioParser(parser_config,
                                      stream_handle,
                                      self._exception_callback)

        return parser

