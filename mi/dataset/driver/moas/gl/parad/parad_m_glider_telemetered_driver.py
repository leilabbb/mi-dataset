#!/usr/local/bin/python2.7
##
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##
__author__ = 'dmergens'

import os
from mi.logging import config
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.driver.moas.gl.parad.parad_m_glider_driver import ParadMDriver
from mi.core.versioning import version


@version("15.6.1")
def parse(unused, sourceFilePath, particleDataHdlrObj):
    parser_config = {
        DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.glider',
        DataSetDriverConfigKeys.PARTICLE_CLASS: 'ParadTelemeteredDataParticle',
    }

    driver = ParadMDriver(unused, sourceFilePath, particleDataHdlrObj, parser_config)
    return driver.process()
