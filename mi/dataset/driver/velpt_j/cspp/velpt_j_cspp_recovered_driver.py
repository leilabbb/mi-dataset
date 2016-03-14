#!/usr/bin/env python

"""
@package mi.dataset.driver.velpt_j.cspp
@file mi/dataset/driver/velpt_j/cspp/velpt_j_cspp_recovered_driver.py
@author Emily Hahn
@brief Driver for the recovered velpt series j instrument through cspp
"""

from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.velpt_j_cspp import VelptJCsppParser, VelptJCsppMetadataRecoveredDataParticle, \
    VelptJCsppInstrumentRecoveredDataParticle

from mi.dataset.parser.cspp_base import METADATA_PARTICLE_CLASS_KEY, DATA_PARTICLE_CLASS_KEY
from mi.core.versioning import version


@version("15.6.1")
def parse(basePythonCodePath, sourceFilePath, particleDataHdlrObj):
    """
    This is the method called by Uframe
    :param basePythonCodePath This is the file system location of mi-dataset
    :param sourceFilePath This is the full path and filename of the file to be parsed
    :param particleDataHdlrObj Java Object to consume the output of the parser
    :return particleDataHdlrObj
    """

    with open(sourceFilePath, 'rU') as stream_handle:

        # create and instance of the concrete driver class defined below
        driver = VelptJCsppRecoveredDriver(basePythonCodePath, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class VelptJCsppRecoveredDriver(SimpleDatasetDriver):
    """
    Derived velpt j cspp driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        parser_config = {
            DataSetDriverConfigKeys.PARTICLE_CLASSES_DICT: {
                METADATA_PARTICLE_CLASS_KEY: VelptJCsppMetadataRecoveredDataParticle,
                DATA_PARTICLE_CLASS_KEY: VelptJCsppInstrumentRecoveredDataParticle,
            }
        }

        return VelptJCsppParser(parser_config, stream_handle, self._exception_callback)
