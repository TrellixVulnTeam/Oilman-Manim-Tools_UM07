import os
from datetime import datetime


def get_name(dir, f):
    now_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    s = "%s_%s%s" % (os.path.splitext(f)[0], now_time, os.path.splitext(f)[1])
    return os.path.join(dir, f)  # 返回新文件路径


def get_new_name_with_copy(dir, f):
    if os.path.exists(os.path.join(dir, f)):
        s = "%s_%s%s" % (os.path.splitext(f)[0], 'Copy', os.path.splitext(f)[1])
        return get_new_name_with_copy(dir, s)  # 新命名文件是否存在
    return os.path.join(dir, f)  # 返回新文件路径
