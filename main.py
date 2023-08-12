import tkinter as tk
import time
import datetime
import os

DEFAULT_TIME = "17:10:00"

def get_target_time_from_file(file_name):
    if not os.path.exists(file_name):
        # 如果文件不存在，则创建并写入默认时间
        with open(file_name, 'w') as file:
            file.write(DEFAULT_TIME)
        return DEFAULT_TIME
    else:
        # 如果文件存在，则从文件读取时间
        with open(file_name, 'r') as file:
            time_str = file.readline().strip()
            if time_str == '':
                # 如果时间格式不正确，重置文件为默认时间
                with open(file_name, 'w') as file:
                    file.write(DEFAULT_TIME)
                return DEFAULT_TIME
            try:
                # 尝试将时间字符串解析为时间，如果失败则重置文件为默认时间
                target_hour, target_minute, target_second = map(int, time_str.split(':'))
                return time_str
            except ValueError:
                with open(file_name, 'w') as file:
                    file.write(DEFAULT_TIME)
                return DEFAULT_TIME
def update_time():
    current_time = datetime.datetime.now()

    # 从文件中获取目标时间
    target_time_str = get_target_time_from_file('time.txt')
    target_hour, target_minute, target_second = map(int, target_time_str.split(':'))

    # 设置目标时间点为每天的指定时间
    target_time = current_time.replace(hour=target_hour, minute=target_minute, second=target_second, microsecond=0)

    # 计算时间差
    time_difference = target_time - current_time

    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    seconds = time_difference.seconds % 60

    # 显示当前时间和距离目标时间的倒计时
    current_time_str = time.strftime('%H:%M:%S')
    countdown_str = f"距 {target_hour:02d}:{target_minute:02d}:{target_second:02d} 还有 {hours} 时 {minutes} 分 {seconds} 秒"
    time_label.config(text=current_time_str + "  ---  " + countdown_str)

    root.after(1000, update_time)  # 每秒更新一次时间


root = tk.Tk()
root.title("小胡看时间")

time_label = tk.Label(root, text="", font=("Helvetica", 24))
time_label.pack(padx=55, pady=20)

update_time()  # 开始更新时间

root.mainloop()
