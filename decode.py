import os
import sys
import cv2

def decrypt(img):
    res = list()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                res.append('1' if (img[i][j][k] & 1) else '0')
    return ''.join(res)

if __name__ == '__main__':
    path = sys.argv[1]
    img = cv2.imread(path)
    res = decrypt(img)
    msg = list()
    for i in range(len(res)//8):
        bt = res[i*8 : (i+1)*8]
        bt = int(bt, 2)
        if bt == 0:
            break
        msg.append(bt)
    msg = bytes(msg)
    msg = msg.decode()
    print(msg)
