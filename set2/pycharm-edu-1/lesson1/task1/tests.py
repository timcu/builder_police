from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "print(" in placeholder:
        passed()
    else:
        failed('use the print() function with a number between 1 and 3')


def test_output():
    correct="5,4,3,2,1,0".split(",")
    correct.insert(0,"Countdown")
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


