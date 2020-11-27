from datetime import datetime
from pathlib import Path
import logging
import os


def func():
    # 获取当前的时间
    timestamp = datetime.now()

    # 判断当前工作路径下是否存在目录，若不存在则新建
    log_file_parent_path = os.path.join(os.getcwd(), datetime.now().strftime("%Y-%m-%d"))

    p = Path(log_file_parent_path)

    if not p.is_dir():
        p.mkdir(exist_ok=True, parents=True)

    # 日志记录
    logging.basicConfig(filename=log_file_parent_path + "/geek.log",
                        level=logging.INFO,
                        format="%(message)s")

    logging.info("调用函数的时间为：{}".format(timestamp))


if __name__ == "__main__":
    func()
