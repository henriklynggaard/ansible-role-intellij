import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


desktop_file_location = "/root/.local/share/applications/intellij-community-2017.1.3.desktop"


def test_desktop_file_exists(File):
    f = File(desktop_file_location)

    assert f.exists
    assert f.is_file


def test_desktop_file_contains_fullpath(File):
    f = File(desktop_file_location)

    assert f.contains("/root/Tools/intellij-community-2017.1.3/bin/idea.png")
    assert f.contains("/root/Tools/intellij-community-2017.1.3/bin/idea.sh")


def test_desktop_file_contains_right_name(File):
    f = File(desktop_file_location)

    assert f.contains("IntelliJ Community Edition 2017.1.3")


def test_start_file_exists(File):
    f = File('/root/Tools/intellij-community-2017.1.3/bin/idea.sh')

    assert f.exists
    assert f.is_file
