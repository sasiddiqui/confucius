#!/usr/bin/env python
"""Unit tests for confucius.main.demo module"""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('~/Dropbox/Computer/Programming/Python/watson/confucius')
sys.path.append('~/Dropbox/Computer/Programming/Python/watson/confucius/main')

from unittest import TestCase
from mock import patch
import demo

class TestDemo(TestCase):
    """Test the demo script"""

    @patch('demo.classify')
    @patch('demo.__builtin__.raw_input')
    def test_classify(self, mock_classify, mock_input):
        """Test classify call"""

        mock_input.return_value = 'hello'

        demo.classify('f5b432x172-nlc-3555', "hello")
        self.assertTrue(mock_classify.called, "Failed to run classify")
