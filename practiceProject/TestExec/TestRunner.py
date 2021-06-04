from DriverSetup.DriverConfig import config_driver
from PageObjects.ParentPage import ParentPage
import importlib
import pytest

def config_run(browser,env,cases):
    for suites in cases:
        suite = importlib.import_module(suites)
        for test in suite.cases:
            config_driver(browser)
            environment_module = importlib.import_module("Environment."+env)
            environment_class = getattr(environment_module, env)
            ParentPage.test_values = environment_class()
            #test should have something like TestCases/OrangeHr/Login/LoginOK.py
            pytest.main(["-x", test])
