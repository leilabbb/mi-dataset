#!/usr/local/bin/python2.7
##
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##

import os

from mi.core.log import get_logger
from mi.dataset.dataset_driver import DataSetDriver
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.parser.adcps_jln_stc import AdcpsJlnStcParser, \
    AdcpsJlnStcMetadataTelemeteredDataParticle, \
    AdcpsJlnStcInstrumentTelemeteredDataParticle, \
    AdcpsJlnStcParticleClassKey
from mi.core.versioning import version


@version("0.0.5")
def parse(basePythonCodePath, sourceFilePath, particleDataHdlrObj):

    from mi.logging import config
    config.add_configuration(os.path.join(basePythonCodePath, 'mi-logging.yml'))
    log = get_logger()

    config = {
        DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.adcps_jln_stc',
        DataSetDriverConfigKeys.PARTICLE_CLASS: None,
        DataSetDriverConfigKeys.PARTICLE_CLASSES_DICT: {
            AdcpsJlnStcParticleClassKey.METADATA_PARTICLE_CLASS:
                AdcpsJlnStcMetadataTelemeteredDataParticle,
            AdcpsJlnStcParticleClassKey.INSTRUMENT_PARTICLE_CLASS:
                AdcpsJlnStcInstrumentTelemeteredDataParticle,
        }
    }
    log.debug("My ADCPS JLN STC Config: %s", config)

    def exception_callback(exception):
        log.debug("ERROR: %r", exception)
        particleDataHdlrObj.setParticleDataCaptureFailure()

    with open(sourceFilePath, 'rb') as file_handle:
        parser = AdcpsJlnStcParser(config,
                                   file_handle,
                                   exception_callback)

        driver = DataSetDriver(parser, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj
