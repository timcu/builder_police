from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "blast off" == placeholder:
        passed()
    else:
        failed('Incorrect action. Should be "blast off"')


def test_output():
    correct="Countdown,5,4,3,2,1,blast off".split(",")
    actual=get_file_output()
    if len(actual)!=len(correct):
        failed("Output should be " + str(len(correct)) + " lines, not " + str(len(actual)))
        return
    for i in range(len(correct)):
        if correct[i]!=actual[i]:
            failed("Output line " + str(i+1) + " should be " + correct[i])
    passed()


if __name__ == '__main__':
    run_common_tests()
    test_output()
    test_answer_placeholders()


