import streamlit as st
import numpy as np
import cv2
import numpy as np
import re

#上传图片函数
def UploadImg(label):
    #能接受.jpg和.png两种常用格式的图片
    uploaded_file = st.file_uploader(label, type=["jpg","png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        #得到RGB格式图片↓
        opencv_image = cv2.imdecode(file_bytes, 1)
        #转换成BGR格式
        rs = cv2.cvtColor(opencv_image,cv2.COLOR_RGB2BGR)
        #返回值rs是原图片本身，uploaded_file.type是文件类型（比如image/png）
        return rs , uploaded_file.type 

#字符串后缀数递增函数 主要用于命名多次推理后的图片
def Increase_string(s, incr_num=1):
    suffix = re.search(r"(_)(\d+)$", s)
    if suffix:
        suffix_plus_1 = re.sub(
            r"(_)(\d+)$",
            lambda x: f"{x.group(1)}{str(int(x.group(2)) + incr_num).zfill(len(x.group(2)))}",s)
    else:
        suffix_plus_1 = f"{s}_1"
    return suffix_plus_1
