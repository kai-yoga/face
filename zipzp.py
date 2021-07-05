import os
import zipfile
from datetime import datetime


def getFiles(file_path, file_type_list):
    '''Generator
    yield filename'''
    for file in os.listdir(file_path):
        yield {
            'name': file,
            'size': os.path.getsize(os.path.join(file_path, file))
        } if file.split('.')[-1] in file_type_list else None


def genZip(file_path, save_path, max_count, max_storage, file_type_list):
    '''生成zip文件'''
    index = 1
    sumsize = 0
    count = 0
    global_count = 0
    L = []
    for file in getFiles(file_path, file_type_list):
        if file:
            global_count = global_count + 1
            if sumsize + file['size'] < max_storage * 1024 * 1024 and count < max_count:
                zipfile.ZipFile(os.path.join(save_path, str(index) + '.zip'),
                                mode='a',
                                compression=zipfile.ZIP_BZIP2).write(os.path.join(file_path, file['name']))
                count = count + 1
                sumsize = sumsize + file['size']
            else:
                L.append('{},已经生成完成，大小=>{},文件数量=>{}'.format(os.path.join(save_path, str(index) + '.zip'),
                                                            str(round(sumsize / 1024)) + 'K', str(count)))
                index = index + 1
                zipfile.ZipFile(os.path.join(save_path, str(index) + '.zip'),
                                mode='a',
                                compression=zipfile.ZIP_BZIP2).write(os.path.join(file_path, file['name']))
                count = 1
                sumsize = file['size']
    if os.path.exists(os.path.join(save_path, str(index) + '.zip')):
        L.append('{},已经生成完成，大小=>{},文件数量=>{}'.format(os.path.join(save_path, str(index) + '.zip'),
                                                    str(round(sumsize / 1024)) + 'K', str(count)))
    return L


def init(save_path):
    '''生成之前先清空保存路径下的zip文件'''
    for file in os.listdir(save_path):
        if file.split('.') == '.zip':
            os.remove(os.path.join(save_path, file))
    return 1


def main(config):
    '''主函数'''
    config = config["zip"]
    if config["open"] not in ["0"]:
        file_path = config["file_path"]
        save_path = config["save_path"]
        save_file_suffix = config["save_file_suffix"]
        if file_path and save_path and save_file_suffix:
            max_count = float(config["max_count"])
            max_storage = float(config["max_storage"])
            if init(save_path):
                print('{}路径中的压缩文件已经清空完毕'.format(save_path))
            L = genZip(file_path, save_path, max_count=max_count, max_storage=max_storage, file_type_list=save_file_suffix)
            with open(os.path.join(save_path, 'zip_res' + datetime.now().strftime('%Y-%m-%d %H%M%S') + '.txt'), 'w',
                      encoding='utf8') as f:
                f.write('\n'.join(L))
            f.close()
