import sys
import linecache
import json

def pretty_print(data):
    return '\n'.join([line for line in parseString(
        data).toprettyxml(indent=' ' * 2).split('\n') if line.strip()])


def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print(
        f'EXCEPTION IN ({filename}, LINE {lineno} "{line.strip()}"): {exc_obj}')


def writejson(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    return 0


def readjson(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data
