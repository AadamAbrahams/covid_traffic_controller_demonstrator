#!/usr/bin/env python

"""Tests for `covid_traffic_controller_demonstrator` package."""


import unittest
from click.testing import CliRunner

from covid_traffic_controller_demonstrator import covid_traffic_controller_demonstrator
from covid_traffic_controller_demonstrator import cli


class TestCovid_traffic_controller_demonstrator(unittest.TestCase):
    """Tests for `covid_traffic_controller_demonstrator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'covid_traffic_controller_demonstrator.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
