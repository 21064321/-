# MIT License
# 
# 版权所有 (c) 2024 6ZmI5oC7
# 
# 特此授予任何获得本软件副本和相关文档文件（“软件”）的人，允许在软件中不受限制地使用，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售软件的副本，以及允许软件提供者在符合以下条件的情况下提供这些权利：
# 
# 上述版权声明和本许可声明应包含在软件的所有副本或主要部分中。
# 
# 软件按“原样”提供，不提供任何明示或暗示的担保，包括但不限于适销性、适用于特定目的和不侵权的担保。在任何情况下，作者或版权持有人均不对因软件或软件的使用或其他交易引起的任何索赔、损害或其他责任负责，无论是在合同、侵权或其他行为中。

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import threading
import pyautogui

# 共享标志，用于控制循环的停止
stop_flag = False

# 激活指定标题的窗口
def activate_window():
    window_title = window_title_entry.get()
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        status_label.config(text="窗口已激活")
    except IndexError:
        status_label.config(text="窗口未找到！")

# 发送键盘按键
def send_keys():
    global stop_flag
    stop_flag = False  # 重置停止标志
    loop_count = int(loop_count_entry.get())  # 获取循环次数
    threading.Thread(target=send_keys_loop, args=(loop_count,)).start()  # 启动自动化循环的线程

# 自动化循环
def send_keys_loop(loop_count):
    for _ in range(loop_count):
        if stop_flag:
            break
        pyautogui.hotkey('ctrl', 'v')  # 发送 Ctrl+V
        pyautogui.hotkey('alt', 's')   # 发送 Alt+S
        time.sleep(0.05)  # 等待一段时间
    status_label.config(text="按键已发送")

# 停止循环
def stop_loop():
    global stop_flag
    stop_flag = True
    status_label.config(text="循环已停止")

# 显示使用方法
def show_usage():
    usage_text = """
    使用方法：
    1. 输入要激活窗口的标题。
    2. 提前将需要轰炸的内容复制到剪贴板。
    3. 输入循环次数。
    4. 点击“发送按键”按钮开始自动化循环。
    5. 点击发送后双击发送框即可触发自动发送。
    6. 如果您有更好的建议或者发现任何问题请随时联系我  6@6z577.cn。
    7. 如果您喜欢这个项目，请给个star吧！
    """
    messagebox.showinfo("使用方法", usage_text)

# 创建主窗口
root = tk.Tk()
root.title("剪切板消息轰炸 by:6ZmI5oC7")
root.geometry("338x278")

# 标题输入框
window_title_label = ttk.Label(root, text="窗口标题:")
window_title_label.grid(row=0, column=0, padx=5, pady=5)
window_title_entry = ttk.Entry(root, width=20)
window_title_entry.grid(row=0, column=1, padx=5, pady=5)
window_title_entry.insert(0, "WeChat.exe")

# 循环次数输入框
loop_count_label = ttk.Label(root, text="循环次数:")
loop_count_label.grid(row=1, column=0, padx=5, pady=5)
loop_count_entry = ttk.Entry(root, width=10)
loop_count_entry.grid(row=1, column=1, padx=5, pady=5)
loop_count_entry.insert(0, "10")

# 激活窗口按钮
activate_button = ttk.Button(root, text="激活窗口", command=activate_window)
activate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# 发送按键按钮
send_keys_button = ttk.Button(root, text="发送按键", command=send_keys)
send_keys_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# 停止循环按钮
stop_button = ttk.Button(root, text="停止循环", command=stop_loop)
stop_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# 使用方法按钮
usage_button = ttk.Button(root, text="使用方法", command=show_usage)
usage_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# 状态标签
status_label = ttk.Label(root, text="")
status_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# 弹出欢迎消息框
messagebox.showinfo("欢迎使用剪切板消息轰炸", "该程序仅作为学习交流使用，请勿用于非法用途！")

root.mainloop()
