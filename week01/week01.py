from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(datetime.now().strftime("%Y-%m-%d") + ".log")
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

logger.addHandler(handler)


def func():
    timestamp = datetime.now()

    logger.info("调用函数的时间为：{}".format(timestamp))


if __name__ == "__main__":
    func()
