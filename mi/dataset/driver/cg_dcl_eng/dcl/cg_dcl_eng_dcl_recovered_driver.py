#!/usr/bin/env python

"""
@package mi.dataset.driver.cg_dcl_eng.dcl
@file mi-dataset/mi/dataset/driver/cg_dcl_eng/dcl/cg_dcl_eng_dcl_recovered_driver.py
@author Mark Worden
@brief Driver for the cg_dcl_eng_dcl instrument

Release notes:

Initial Release
"""

from mi.dataset.dataset_parser import DataSetDriverConfigKeys
from mi.dataset.dataset_driver import SimpleDatasetDriver
from mi.dataset.parser.cg_dcl_eng_dcl import CgDclEngDclParser, CgDclEngDclParticleClassTypes, \
    CgDclEngDclMsgCountsRecoveredDataParticle, \
    CgDclEngDclCpuUptimeRecoveredDataParticle, \
    CgDclEngDclErrorRecoveredDataParticle, \
    CgDclEngDclGpsRecoveredDataParticle, \
    CgDclEngDclPpsRecoveredDataParticle, \
    CgDclEngDclSupervRecoveredDataParticle, \
    CgDclEngDclDlogMgrRecoveredDataParticle, \
    CgDclEngDclDlogStatusRecoveredDataParticle, \
    CgDclEngDclStatusRecoveredDataParticle, \
    CgDclEngDclDlogAarmRecoveredDataParticle
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

    with open(sourceFilePath, 'rb') as stream_handle:

        driver = CgDclEngDclRecoveredDriver(unused, stream_handle, particleDataHdlrObj)
        driver.processFileStream()

    return particleDataHdlrObj


class CgDclEngDclRecoveredDriver(SimpleDatasetDriver):
    """
    Derived flntu_x_mmp_cds driver class
    All this needs to do is create a concrete _build_parser method
    """

    def _build_parser(self, stream_handle):

        parser_config = {
            DataSetDriverConfigKeys.PARTICLE_MODULE: 'mi.dataset.parser.cg_dcl_eng_dcl',
            DataSetDriverConfigKeys.PARTICLE_CLASS: None,
            DataSetDriverConfigKeys.PARTICLE_CLASSES_DICT: {
                CgDclEngDclParticleClassTypes.MSG_COUNTS_PARTICLE_CLASS:
                    CgDclEngDclMsgCountsRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.CPU_UPTIME_PARTICLE_CLASS:
                    CgDclEngDclCpuUptimeRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.ERROR_PARTICLE_CLASS:
                    CgDclEngDclErrorRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.GPS_PARTICLE_CLASS:
                    CgDclEngDclGpsRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.PPS_PARTICLE_CLASS:
                    CgDclEngDclPpsRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.SUPERV_PARTICLE_CLASS:
                    CgDclEngDclSupervRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.DLOG_MGR_PARTICLE_CLASS:
                    CgDclEngDclDlogMgrRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.DLOG_STATUS_PARTICLE_CLASS:
                    CgDclEngDclDlogStatusRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.STATUS_PARTICLE_CLASS:
                    CgDclEngDclStatusRecoveredDataParticle,
                CgDclEngDclParticleClassTypes.DLOG_AARM_PARTICLE_CLASS:
                    CgDclEngDclDlogAarmRecoveredDataParticle,
            }

        }

        parser = CgDclEngDclParser(parser_config,
                                   stream_handle,
                                   self._exception_callback)

        return parser


