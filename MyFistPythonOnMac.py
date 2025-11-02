
'''
pylint配置：
1， 终端执行python3 -m pip isntall pylint
2，在pycharm配置，pycharm--settings-plugins搜索pylint 安装
3，在pychar-settings-pylint配置里，设置路径，这是3.12的版本，所以用了3.12的路径
    /Library/Frameworks/Python.framework/Versions/3.12/bin/pylint
4，点击test，如果提示found 那么就OK了
5，主函数没有main， 只有if __name__ == "__main__":
'''
def test_print():
    print("hello ,world!!")

test_print()
