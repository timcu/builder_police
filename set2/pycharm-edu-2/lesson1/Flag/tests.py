from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from unittest import mock
from triptera_pe_tests import mock_send_building, mock_create

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


@mock.patch('ircbuilder.MinetestConnection.create', mock_create)
@mock.patch('ircbuilder.MinetestConnection.send_building', mock_send_building)
def run_patched_tests():
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    # test_building()


if __name__ == '__main__':
    run_patched_tests()
