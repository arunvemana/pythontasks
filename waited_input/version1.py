import asyncio


async def input_timeout(message: str, timeout: int = 0):
    """
            :why:
    Default input doesn't have timeout feature
    until u pressed "return" or "enter"
        :functionality:
    Take input from the user and have to press "enter" or "return"
    before the given timeout , if u don't press "enter/return" that given
    input won't be assign
    :param message:
    :param timeout:
    :return:
    """
    sys.stdout.write(message)
    sys.stdout.flush()
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    def user_answer():
        loop.create_task(queue.put(sys.stdin.readline()))

    loop.add_reader(sys.stdin.fileno(), user_answer)

    try:
        return await asyncio.wait_for(queue.get(), timeout=timeout)
    except asyncio.TimeoutError:
        sys.stdout.write('\n')
        sys.stdout.flush()
        raise
    finally:
        loop.remove_reader(sys.stdin.fileno())
        sys.stdout.flush()


async def run():
    try:
        var = await  input_timeout("message: ", 4)
    except asyncio.TimeoutError:
        var = "hello"
    print(var)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
