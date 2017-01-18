"""
@package mi.dataset.driver.phsen_abcdef.imodem
@file mi-dataset/mi/dataset/driver/phsen_abcdef/imodem/phsen_abcdef_imodem_recovered_driver.py
@author Joe Padula
@brief Recovered driver for the phsen_abcdef_imodem instrument

Release notes:

Initial Release
"""

__author__ = 'jpadula'

from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.parser.phsen_abcdef_imodem import \
    PhsenAbcdefImodemParser, \
    PhsenAbcdefImodemParticleClassKey
from mi.dataset.parser.phsen_abcdef_imodem_particles import \
    PhsenAbcdefImodemControlRecoveredDataParticle, \
    PhsenAbcdefImodemInstrumentRecoveredDataParticle,\
    PhsenAbcdefImodemMetadataRecoveredDataParticle
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

        # create an instance of the concrete driver class defined below
        driver = PhsenAbcdefImodemRecoveredDriver(unused, stream_handle, particleDataHdlrObj)

        driver.processFileStream()

    return particleDataHdlrObj


class PhsenAbcdefImodemRecoveredDriver(SimpleDatasetDriver):
    """
    The phsen_abcdef_imodem recovered driver class extends the SimpleDatasetDriver.
    """

    def _build_parser(self, stream_handle):

        parser_config = {
            DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.phsen_abcdef_imodem_particles',
            DataSetDriverConfigKeys.PARTICLE_CLASS: None,
            DataSetDriverConfigKeys.PARTICLE_CLASSES_DICT: {
                PhsenAbcdefImodemParticleClassKey.METADATA_PARTICLE_CLASS:
                PhsenAbcdefImodemMetadataRecoveredDataParticle,
                PhsenAbcdefImodemParticleClassKey.CONTROL_PARTICLE_CLASS:
                PhsenAbcdefImodemControlRecoveredDataParticle,
                PhsenAbcdefImodemParticleClassKey.INSTRUMENT_PARTICLE_CLASS:
                PhsenAbcdefImodemInstrumentRecoveredDataParticle,
            }
        }

        parser = PhsenAbcdefImodemParser(parser_config,
                                         stream_handle,
                                         self._exception_callback)

        return parser

