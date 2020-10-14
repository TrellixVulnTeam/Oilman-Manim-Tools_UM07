
import os
import shutil
from datetime import datetime


def get_new_name(dir, f):
    if os.path.exists(os.path.join(dir, f)):
        now_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        s = "%s_%s%s" % (os.path.splitext(f)[0], now_time, os.path.splitext(f)[1])
        return get_new_name(dir, s)  # 新命名文件是否存在
    return os.path.join(dir, f)  # 返回新文件路径


#p = get_new_name(r"C:\Users\lishihang\Desktop\新建文件夹", "1.txt")
#shutil.copy(r"C:\Users\lishihang\Desktop\1.txt", p)
