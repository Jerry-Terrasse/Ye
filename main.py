import os
import sys
import cv2

def toBin(bt):
    res = format(bt, 'b')
    res = '0' * (8-len(res)) + res
    return res

def encrypt(img, res):
    cnt = int()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                img[i][j][k] |= 1
                img[i][j][k] ^= 1 if res[cnt]=='0' else 0
                cnt += 1
                if cnt == len(res):
                    return

if __name__ == '__main__':
    path = sys.argv[1]
    msg = sys.argv[2]
    img = cv2.imread(path)
    bts = msg.encode()
    bts += b'\0'
    res = list()
    for bt in bts:
        res.append(toBin(bt))
    res = ''.join(res)
    encrypt(img, res)
    print(img[0][0],img[0][1],img[0][2])
#    cv2.imwrite("out.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imwrite("out.bmp", img)
