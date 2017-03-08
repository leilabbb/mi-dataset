#!/usr/bin/env python

import os
import unittest
from nose.plugins.attrib import attr

from mi.core.log import get_logger
from mi.dataset.dataset_driver import ParticleDataHandler
from mi.dataset.driver.parad_j.cspp.parad_j_cspp_telemetered_driver import parse
from mi.dataset.driver.parad_j.cspp.resource import RESOURCE_PATH

__author__ = 'Joe Padula'
log = get_logger()


@attr('UNIT', group='mi')
class SampleTest(unittest.TestCase):

    def test_one(self):

        source_file_path = os.path.join(RESOURCE_PATH, '11079364_PPD_PARS.txt')

        particle_data_handler = ParticleDataHandler()

        particle_data_handler = parse(None, source_file_path, particle_data_handler)

        log.debug("SAMPLES: %s", particle_data_handler._samples)
        log.debug("FAILURE: %s", particle_data_handler._failure)

        self.assertEquals(particle_data_handler._failure, False)


if __name__ == '__main__':
    test = SampleTest('test_one')
    test.test_one()
