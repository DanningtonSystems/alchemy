import sys
from termcolor import colored

_VERSION="0.0.1"

def usage():
    print(f"alchemy v{_VERSION}")
    print(f"Created by DanningtonSystems, 2021\n")
    print("Usage:")
    print("alchemy <operation> [options] [targets]")
    print(colored("\nOPERATIONS", attrs=["bold"]))
    print("install - Install a package from specified repositories")
    print("update - Update all packages across all specified repositories")
    print("uninstall - Uninstall a package")
    print("query - Query a package from repositories")
    print(colored("\nOPTIONS", attrs=["bold"]))
    print("-h (--help) - See this message")
    print("-v (--version) - Outputs the version string of Alchemy")

if len(sys.argv) <= 1:
    usage()
    sys.exit(0)
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    usage()
elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
    print(f"alchemy v{_VERSION}")