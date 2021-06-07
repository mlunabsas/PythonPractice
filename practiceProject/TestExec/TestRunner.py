# from DriverSetup.DriverConfig import config_driver
# from PageObjects.ParentPage import ParentPage
import importlib
import pytest

def config_run(case_files):
    #this handle all the file/s like Workbench sent
    for file in case_files:
        # this handle each file sent
        suite = importlib.import_module(file)
        for test in suite.cases:
            #test should have something like TestCases/OrangeHr/Login/test_LoginOK.py
            #atributes like "-x" or "-m" sould be sent here like another parameter ex: pytest.main("-x",[test])
            pytest.main([test])
