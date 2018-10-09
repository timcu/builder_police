from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()

def test_output():
    results={}
    for i in range(0,60):
        for result in get_file_output():
            try:
                r=int(result)
            except ValueError:
                failed('Received "' + result + '" instead of an integer between 1 and 6')
                return
            if str(r)!=result:
                failed('Received ' + result + ' which is not an integer')
                return
            if r<1 or r>6:
                failed('Received ' + result + ' which is not in the range 1 to 6')
                return
            try:
                results[r]=results[r]+1
            except KeyError:
                results[r]=1
    for key in range(1,7):
        try:
            if results[key]<3:
                failed('Received the number ' + str(key) + ' only ' + str(results[key]) + ' times out of 60. Not random enough')
            elif results[key]>17:
                failed('Received the number ' + str(key) + ' as many as ' + str(results[key]) + ' times out of 60. Not random enough')
            #print(key,results[key])
        except KeyError:
            failed("Didn't receive the number " + str(key) + " after 60 times. Not random enough")
    passed()


if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    test_output()


