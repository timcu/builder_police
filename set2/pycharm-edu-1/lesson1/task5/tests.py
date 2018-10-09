from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "counter":
        passed()
    else:
        failed("Variable name should be 'counter' not '" + placeholder + "'")


def test_output():
    correct=list(map(str,range(20,0,-1)))
    correct.append("blast off")
    correct.insert(0,"Countdown")
    actual=get_file_output()
    if len(actual)!=len(correct):
        failed("Output should be " + str(len(correct)) + " lines, not " + str(len(actual)))
        return
    for i in range(len(correct)):
        if correct[i]!=actual[i]:
            failed("Line " + str(i+1) + " should be " + correct[i])
    passed()


if __name__ == '__main__':
    run_common_tests()
    test_output()
    #test_answer_placeholders()


