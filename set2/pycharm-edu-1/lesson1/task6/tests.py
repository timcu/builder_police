from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "sleep(1)" in placeholder:
        passed()
    elif "sleep" in placeholder:
        failed("The number of seconds to sleep must be supplied as a parameter")
    else:
        failed("Use the 'sleep' function")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


