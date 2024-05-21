# 剪切板轰炸工具

这是一个使用Python编写的剪切板轰炸工具。它可以读取剪切板中的第一条文本，并在指定程序中重复执行粘贴发送操作。循环次数由用户决定。

## 使用方法

1. 下载可执行文件并双击运行。
2. 按照提示输入循环次数。

## 打包方法

如果你想将此程序打包成可执行文件，请按照以下步骤操作：

1. 安装Python 3.1.2解释器。
2. 安装`pyinstaller`库：在终端中运行`pip install pyinstaller`。
3. 安装`pyautogui`库：在终端中运行`pip install pyautogui`。
4. 在终端中执行`pyinstaller --onefile --noconsole "hz.py"`。

这将生成一个名为`hz.exe`的可执行文件，然后双击运行。

## 许可协议

MIT License

Copyright (c) [2024] 6ZmI5oC7

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY arising from, out of or in connection with the software or the use or other dealings in the Software.

