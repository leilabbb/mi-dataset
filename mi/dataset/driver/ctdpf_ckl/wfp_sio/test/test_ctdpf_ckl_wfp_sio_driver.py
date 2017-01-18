#!/home/mworden/uframes/ooi/uframe-1.0/python/bin/python

__author__ = 'Jeff Roy'

from mi.core.log import get_logger
log = get_logger()

from mi import MI_BASE_PATH

import unittest
import os
from mi.dataset.driver.ctdpf_ckl.wfp_sio.ctdpf_ckl_wfp_sio_telemetered_driver import parse

from mi.dataset.dataset_driver import ParticleDataHandler


class SampleTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):

        source_file_path = os.path.join('mi', 'dataset', 'driver',
                                        'ctdpf_ckl', 'wfp_sio', 'resource',
                                        'node58p1_0.wc_wfp.dat')

        particle_data_hdlr_obj = ParticleDataHandler()

        particle_data_hdlr_obj = parse(MI_BASE_PATH, source_file_path, particle_data_hdlr_obj)

        log.debug("SAMPLES: %s", particle_data_hdlr_obj._samples)
        log.debug("FAILURE: %s", particle_data_hdlr_obj._failure)

        self.assertEquals(particle_data_hdlr_obj._failure, False)


if __name__ == '__main__':
    test = SampleTest('test_one')
    test.test_one()
