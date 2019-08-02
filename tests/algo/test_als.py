# -*- coding: utf-8 -*-
import unittest
from buffalo.misc import aux
from buffalo.algo.als import ALS
from buffalo.misc.log import set_log_level
from buffalo.algo.options import AlsOption

from .base import TestBase


class TestALS(TestBase):
    def test0_get_default_option(self):
        AlsOption().get_default_option()
        self.assertTrue(True)

    def test1_is_valid_option(self):
        opt = AlsOption().get_default_option()
        self.assertTrue(AlsOption().is_valid_option(opt))
        opt['save_best'] = 1
        self.assertRaises(RuntimeError, AlsOption().is_valid_option, opt)
        opt['save_best'] = False
        self.assertTrue(AlsOption().is_valid_option(opt))

    def test2_init_with_dict(self):
        set_log_level(3)
        opt = AlsOption().get_default_option()
        ALS(opt)
        self.assertTrue(True)

    def test3_init(self):
        opt = AlsOption().get_default_option()
        self._test3_init(ALS, opt)

    def test4_train(self):
        opt = AlsOption().get_default_option()
        opt.d = 5
        self._test4_train(ALS, opt)

    def test5_validation(self):
        opt = AlsOption().get_default_option()
        opt.d = 5
        opt.num_iters = 20
        opt.validation = aux.Option({'topk': 10})
        opt.tensorboard = aux.Option({'root': './tb',
                                      'name': 'als'})
        self._test5_validation(ALS, opt)

    def test6_topk(self):
        opt = AlsOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test6_topk(ALS, opt)

    def test7_train_ml_20m(self):
        opt = AlsOption().get_default_option()
        opt.num_workers = 8
        opt.validation = aux.Option({'topk': 10})
        self._test7_train_ml_20m(ALS, opt)

    def test8_serialization(self):
        opt = AlsOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test8_serialization(ALS, opt)

    def test9_compact_serialization(self):
        opt = AlsOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test9_compact_serialization(ALS, opt)


if __name__ == '__main__':
    unittest.main()
