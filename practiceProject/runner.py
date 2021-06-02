import argparse
from TestExec.TestRunner import config_run
#Usage ex: python runner.py --browser chrome firefox edge --environment test testv dev --test suite

# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()

CLI.add_argument(
  "--browser",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=str,  # any type/callable can be used here
  default=["chrome"],  # default if nothing is provided
)

CLI.add_argument(
  "--environment",
  nargs="*",
  type=str,  # any type/callable can be used here
  default=["TestVolatil"],
)

CLI.add_argument(
  "--test",
  nargs="*",
  type=str,  # any type/callable can be used here
  default=["TestCases/OrangeHr/Login/LoginOK.py"],
)

# parse the command line
args = CLI.parse_args()

# access CLI options
print("Browser: %r" % args.browser)
print("Environment: %r" % args.environment)
print("Case/Suite: %r" % args.test)
config_run(args.browser[0],args.environment[0],args.test[0])
