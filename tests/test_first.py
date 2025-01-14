from nunininu_check_os_ver.osver import get os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v == "ubuntu 24.04.1"
