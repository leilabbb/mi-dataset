#!/usr/local/bin/python2.7
##
# OOIPLACEHOLDER
#
# Copyright 2014 Raytheon Co.
##

from mi.core.versioning import version
from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.driver.cg_stc_eng.stc.cg_stc_eng_stc_common_driver import CgStcEngDriver


@version("0.0.3")
def parse(unused, sourceFilePath, particleDataHdlrObj):
    parser_config = {
        DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.cg_stc_eng_stc',
        DataSetDriverConfigKeys.PARTICLE_CLASS: 'CgStcEngStcParserDataParticle'
    }

    driver = CgStcEngDriver(sourceFilePath, particleDataHdlrObj, parser_config)

    return driver.process()
