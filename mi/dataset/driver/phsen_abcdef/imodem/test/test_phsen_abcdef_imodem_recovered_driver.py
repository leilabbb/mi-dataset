__author__ = 'Joe Padula'

from mi.core.log import get_logger
log = get_logger()

from mi import MI_BASE_PATH

import unittest
import os
from mi.dataset.driver.phsen_abcdef.imodem.phsen_abcdef_imodem_recovered_driver import parse

from mi.dataset.dataset_driver import ParticleDataHandler


class SampleTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):

        sourceFilePath = os.path.join('mi', 'dataset', 'driver',
                                      'phsen_abcdef', 'imodem', 'resource',
                                      'phsen1_20140730_190554.DAT')

        particle_data_hdlr_obj = ParticleDataHandler()

        particle_data_hdlr_obj = parse(MI_BASE_PATH, sourceFilePath, particle_data_hdlr_obj)

        log.debug("SAMPLES: %s", particle_data_hdlr_obj._samples)
        log.debug("FAILURE: %s", particle_data_hdlr_obj._failure)

        self.assertEquals(particle_data_hdlr_obj._failure, False)


if __name__ == '__main__':
    test = SampleTest('test_one')
    test.test_one()
