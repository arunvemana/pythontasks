import signal, sys


class WaitedInput:
    def __init__(self, message: str, wait_t: int):
        self.message = message
        self.time = wait_t
        self.exe_code()

    def handler(self, *args):
        print("No input from User So CODE run is closing UP!BYE.")
        sys.exit()

    def exe_code(self):
        signal.signal(signal.SIGALRM, self.handler)
        signal.alarm(self.time)

        var = input(self.message)
        if var:
            self.message = f"Is this given input?:->{var}"
        signal.alarm(0)

    def __repr__(self):
        return self.message


print(WaitedInput(message="Give ur input value:", wait_t=5))
