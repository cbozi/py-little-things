import os
def rmv_dir(top):
    '删除非空文件夹'
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)

for root,dirs, files in os.walk(os.curdir):
    file_name = []
    for each_file in files:
        file_name.append(os.path.splitext(each_file)[0])
    for each_dir in dirs:
        if each_dir.endswith('.sdr') and (os.path.splitext(each_dir)[0] not in file_name):
            print('removed', os.path.join(root, each_dir))
            rmv_dir(os.path.join(root, each_dir))

