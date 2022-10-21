# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import base64


def encode_file(src):
    dest=src.replace('.zip','.bas')
    if os.path.isfile(src):
        with open(src, 'rb') as fs:
            file = base64.b64encode(fs.read())
            fs.close()
        with open(dest, 'wb') as fd:
            fd.write(file)
            fd.close()
            print(src+'....Cryptoed!')
        return True
    return False


def decode_file(src):
    dest = src.replace('.bas', '.zip')
    if os.path.isfile(src):
        with open(src, 'rb') as fs:
            file = fs.read()
            fs.close()
        with open(dest, 'wb') as fd:
            fd.write(base64.b64decode(file))
            fd.close()
            print(src + '....DeCryptoed!')
        return True
    return False


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    files=' '.join(os.listdir(r'./'));
    # print(files)
    if '.bas' in files:
        for fname in os.listdir(r'./'):
            if (fname[-4:] == '.bas'):
                # print(fname)
                decode_file(fname)
    else:
        for fname in os.listdir(r'./'):
            if (fname[-4:] == '.zip'):
                encode_file(fname)
    print('done!')
