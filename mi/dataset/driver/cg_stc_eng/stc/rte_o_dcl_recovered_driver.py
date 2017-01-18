##
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##

import os

from mi.logging import config
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.driver.cg_stc_eng.stc.driver_common import RteODclDriver
from mi.core.versioning import version

__author__ = "jpadula"


@version("0.0.3")
def parse(basePythonCodePath, sourceFilePath, particleDataHdlrObj):

    config.add_configuration(os.path.join(basePythonCodePath, 'mi-logging.yml'))

    parser_config = {
        DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.rte_o_dcl',
        DataSetDriverConfigKeys.PARTICLE_CLASS: 'RteODclParserRecoveredDataParticle'
    }

    driver = RteODclDriver(sourceFilePath, particleDataHdlrObj, parser_config)

    return driver.process()
