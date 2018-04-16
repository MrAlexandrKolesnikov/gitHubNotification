import subprocess
import sys
import os


class Arguments:
    @staticmethod
    def has_args(flag_name):
        return False if not len(sys.argv) > 1 else False if not sys.argv[1] == flag_name else True

    @staticmethod
    def get(index):
        return sys.argv[index]

    @staticmethod
    def count():
        return len(sys.argv)


class Executor:
    @staticmethod
    def run(commands=[], *args):
        child = subprocess.Popen(commands, stdout=subprocess.PIPE)
        while child.poll() is None:
            output_line = child.stdout.readline()
            if output_line:
                print(output_line.decode("utf-8")[:-1])
        code = child.returncode
        if code:
            os.sys.exit(code)
