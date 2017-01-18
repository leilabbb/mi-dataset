#!/usr/bin/env python

"""
@package mi.dataset.driver.wc_hmr.cspp
@file mi/dataset/driver/wc_hmr/cspp/wc_hmr_cspp_recovered_driver.py
@author Jeff Roy
@brief Driver for the wc_hmr_cspp instrument

Release notes:

Initial Release
"""

from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.wc_hmr_cspp import \
    WcHmrCsppParser, \
    WcHmrEngRecoveredDataParticle, \
    WcHmrMetadataRecoveredDataParticle

from mi.dataset.parser.cspp_base import \
    METADATA_PARTICLE_CLASS_KEY, \
    DATA_PARTICLE_CLASS_KEY
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

    with open(sourceFilePath, 'rU') as stream_handle:

        # create and instance of the concrete driver class defined below
        driver = WcHmrCsppRecoveredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class WcHmrCsppRecoveredDriver(SimpleDatasetDriver):
    """
    Derived wc_wm_cspp driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        parser_config = {
            DataSetDriverConfigKeys.PARTICLE_CLASS: None,
            DataSetDriverConfigKeys.PARTICLE_CLASSES_DICT: {
                METADATA_PARTICLE_CLASS_KEY: WcHmrMetadataRecoveredDataParticle,
                DATA_PARTICLE_CLASS_KEY: WcHmrEngRecoveredDataParticle,
            }
        }

        parser = WcHmrCsppParser(parser_config, stream_handle,
                                 self._exception_callback)

        return parser


