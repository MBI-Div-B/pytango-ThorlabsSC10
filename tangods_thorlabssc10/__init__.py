from .ThorlabsSC10 import ThorlabsSC10


def main():
    import sys
    import tango.server

    args = ["ThorlabsSC10"] + sys.argv[1:]
    tango.server.run((ThorlabsSC10,), args=args)
