# #
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##

import os

from mi.core.log import get_logger
from mi.logging import config

from mi.dataset.parser.optaa_dj_dcl import OptaaDjDclParser
from mi.dataset.dataset_driver import DataSetDriver
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.core.versioning import version

__author__ = "mworden"


class OptaaDjDclTelemeteredDriver:
    def __init__(self, sourceFilePath, particleDataHdlrObj, parser_config):
        self._sourceFilePath = sourceFilePath
        self._particleDataHdlrObj = particleDataHdlrObj
        self._parser_config = parser_config

    def process(self):
        log = get_logger()

        with open(self._sourceFilePath, "rb") as file_handle:
            def exception_callback(exception):
                log.debug("Exception: %s", exception)
                self._particleDataHdlrObj.setParticleDataCaptureFailure()

            parser = OptaaDjDclParser(self._parser_config,
                                      file_handle, exception_callback, self._sourceFilePath, True)


            driver = DataSetDriver(parser, self._particleDataHdlrObj)

            driver.processFileStream()

        return self._particleDataHdlrObj


@version("15.7.0")
def parse(basePythonCodePath, sourceFilePath, particleDataHdlrObj):
    config.add_configuration(os.path.join(basePythonCodePath, 'mi-logging.yml'))

    parser_config = {
        DataSetDriverConfigKeys.PARTICLE_MODULE: "mi.dataset.parser.optaa_dj_dcl",
        DataSetDriverConfigKeys.PARTICLE_CLASS: None
    }

    driver = OptaaDjDclTelemeteredDriver(sourceFilePath, particleDataHdlrObj, parser_config)

    return driver.process()
