import runner
import importlib

def config_environment():
    environment_module = importlib.import_module("Environment." + runner.actual_environment)
    environment_class = getattr(environment_module, runner.actual_environment)
    return environment_class()