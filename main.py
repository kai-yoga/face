import getconfig
import face
import zipzp

if __name__ == "__main__":
    config = getconfig.getConfig()
    try:
        face.main(config)
        print('照片识别成功')
    except:
        print('照片识别失败')
    try:
        zipzp.main(config)
        print('压缩成功')
    except:
        print('压缩失败')
