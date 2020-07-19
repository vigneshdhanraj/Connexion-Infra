from supportmanager import PrintException

def get_version():
    return "1.0"


def system_info():
    try:
        sysinfo = {
            'name': '',
            'version': get_version(),
        }
    except Exception:
        PrintException()
        sysinfo = {'name': '', 'version': ''}
    return sysinfo
