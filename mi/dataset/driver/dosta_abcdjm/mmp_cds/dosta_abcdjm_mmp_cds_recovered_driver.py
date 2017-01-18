#!/usr/bin/env python
##
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##

from mi.core.log import get_logger
from mi.core.versioning import version
from mi.dataset.dataset_driver import DataSetDriver
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.parser.mmp_cds_base import MmpCdsParser

log = get_logger()

__author__ = 'Joe Padula'


@version("0.0.3")
def parse(unused, sourceFilePath, particleDataHdlrObj):
    parser_config = {
        DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.dosta_abcdjm_mmp_cds',
        DataSetDriverConfigKeys.PARTICLE_CLASS: 'DostaAbcdjmMmpCdsParserDataParticle'
    }

    def exception_callback(exception):
        log.debug("ERROR: %r", exception)
        particleDataHdlrObj.setParticleDataCaptureFailure()

    with open(sourceFilePath, 'rb') as stream_handle:
        parser = MmpCdsParser(parser_config, stream_handle, exception_callback)

        driver = DataSetDriver(parser, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj
