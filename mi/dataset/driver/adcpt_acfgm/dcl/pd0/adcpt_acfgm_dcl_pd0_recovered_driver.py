#!/usr/bin/env python

# ##
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##

import os

from mi.logging import config

from mi.dataset.driver.adcpt_acfgm.dcl.pd0.adcpt_acfgm_dcl_pd0_driver_common import AdcptAcfgmDclPd0Driver
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.core.versioning import version

__author__ = "Jeff Roy"


@version("15.8.0")
def parse(basePythonCodePath, sourceFilePath, particleDataHdlrObj):

    config.add_configuration(os.path.join(basePythonCodePath, 'mi-logging.yml'))

    parser_config = {
        DataSetDriverConfigKeys.PARTICLE_CLASSES_DICT: {
            'velocity': 'Velocity',
            'engineering': 'Engineering',
            'config': 'Config',
        }
    }

    driver = AdcptAcfgmDclPd0Driver(sourceFilePath, particleDataHdlrObj, parser_config)

    return driver.process()
