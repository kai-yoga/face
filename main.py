import getconfig
import face
import zipzp
import time
if __name__ == "__main__":
    config = getconfig.getConfig()
    # face.main(config)

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
    time.sleep(20)