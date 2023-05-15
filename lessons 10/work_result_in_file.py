import datetime


def result_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Function launched at {current_time} with result {result}\n"

        with open("log.txt", "a") as file:
            file.write(log_message)

        return result

    return wrapper


@result_logger
def sum_args(*args):
    return sum(args)


sum_args()
