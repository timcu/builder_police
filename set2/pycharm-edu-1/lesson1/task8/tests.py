from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file
import sys
from subprocess import Popen, PIPE, STDOUT
from threading import Thread
from queue import Queue, Empty


def test_using_threads():

    ioq=Queue()

    def stream_watcher(identifier, stream):
        #for line in stream:
        #    ioq.put((identifier,line))
        line=''
        for c in iter(lambda: stream.read(1),''):
            line+=c
            if c in '?\n':
                ioq.put((identifier,line))
                line=''
        if not stream.closed:
            #print("Closing stream " + identifier)
            stream.close()


    def test_guesser_success():
        max=64
        min=0
        tfsuccess=False
        tfpassed=False
        while True:
            try:
                #block for 1 second
                item=ioq. get(timeout=1)
            except Empty:
                if proc.poll() is not None:
                    break
            else:
                identifier, line = item
                print(identifier,":",line.strip())
                if 'You win' in line:
                    if min==guess and min!=0:
                        failed("Should not say 'too low' when answer matches guess")
                    elif max==guess:
                        failed("Should not say 'too high' when answer matches guess")
                    tfsuccess=True
                    tfpassed=True
                if 'too low' in line:
                    min=guess
                elif 'too high' in line:
                    max=guess
                elif 'Guess?' in line:
                    guess=(max+min)//2
                    proc.stdin.write(str(guess) + "\n")
                    proc.stdin.flush()
        if not tfsuccess:
            failed('Should say "You win" when final answer reached within 10 guesses')
        elif tfpassed:
            passed()


    def test_guesser_high_low():
        maxguess=65
        minguess=-1
        guess=maxguess
        tfguesshigh=True
        tfpassed=True
        while True:
            try:
                #block for 1 second
                item=ioq.get(timeout=1)
            except Empty:
                if proc.poll() is not None:
                    break
            else:
                identifier, line = item
                print(identifier,":",line.strip())
                if 'too low' in line:
                    if tfguesshigh:
                        tfpassed=False
                        failed("Guess " + str(guess) + " should return 'too high' not 'too low'")
                    else:
                        guess=maxguess-(guess-minguess)-1
                        tfguesshigh=True
                elif 'too high' in line:
                    if not tfguesshigh:
                        tfpassed=False
                        failed("Guess " + str(guess) + " should return 'too low' not 'too high'")
                    else:
                        tfguesshigh=False
                        guess=minguess+(maxguess-guess)
                elif 'Guess?' in line:
                    proc.stdin.write(str(guess) + "\n")
                    proc.stdin.flush()
        if tfpassed:
            passed('test_guesser_high_low')


    def test_guesser_max_guesses_and_string_handling():
        tffailure=False
        tftestedstring=False
        guesses=0
        while guesses<12:
            try:
                #block for 1 second
                item=ioq.get(timeout=1)
            except Empty:
                if proc.poll() is not None:
                    break
            else:
                identifier, line = item
                print(identifier,":",line.strip())
                calc=False
                if 'You lose' in line:
                    tffailure=True
                elif 'Please only enter integers' in line:
                    tftestedstring=True
                elif 'Guess?' in line:
                    proc.stdin.write("string\n")
                    proc.stdin.flush()
                    guesses+=1
        if guesses<10:
            failed("Should allow 10 guesses but only allowed " + str(guesses))
        elif guesses>10:
            failed("Should only allow 10 guesses but allowed " + str(guesses))
        elif not tftestedstring:
            failed("Should detect non-integer string and say 'Please only enter integers'")
        elif not tffailure:
            failed('Should say "You lose" when final answer not reached within 10 guesses')
        else:
            passed('test_guesser_max_guesses_and_string_handling')


    # universal_newlines ensures default encoding is used and communication is by strings not bytearrays
    proc = Popen([sys.executable, sys.argv[-1]], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    Thread(target=stream_watcher, name='stdout-watcher', args=('STDOUT', proc.stdout)).start()
    Thread(target=stream_watcher, name='stderr-watcher', args=('STDERR', proc.stderr)).start()
    test_guesser_high_low()

    proc = Popen([sys.executable, sys.argv[-1]], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    Thread(target=stream_watcher, name='stdout-watcher', args=('STDOUT', proc.stdout)).start()
    Thread(target=stream_watcher, name='stderr-watcher', args=('STDERR', proc.stderr)).start()
    test_guesser_max_guesses_and_string_handling()

    proc = Popen([sys.executable, sys.argv[-1]], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    Thread(target=stream_watcher, name='stdout-watcher', args=('STDOUT', proc.stdout)).start()
    Thread(target=stream_watcher, name='stderr-watcher', args=('STDERR', proc.stderr)).start()
    test_guesser_success()




if __name__ == '__main__':
    run_common_tests()
    test_using_threads()
