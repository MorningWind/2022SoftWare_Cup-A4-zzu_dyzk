import streamlit as st
import apis
import deploy
import cv2
import os

#基本UI布局
st.markdown("# 目标提取 👊")
st.sidebar.markdown("# 目标提取 👊")
st.sidebar.markdown("功能简介：")
st.sidebar.markdown("提取并画出输入图像中的道路。")
st.write("欢迎使用目标提取功能！")
st.image("get.png")

#初始文件名 每次进行同类预测 都会赋予初值
input_name = "input_01"
output_name = "output_01"

#UploadImg双返回值 如果用一般写法 未上传文件时会有报错提示影响交互
return_list = apis.UploadImg("请上传图片：")
if return_list is not None:
    img = return_list[0]
    type = return_list[1]

#推理部分、结果保存和异常显示
cfm = st.button("开始检测")
if cfm:
    if img is not None:
        receive = deploy.Predict_get("model_get",img)
        #得到文件夹内已有文件数（即已进行同类推理的次数） 便于后续文件命名 中途切换其他预测也无妨
        for dirpath, dirnames, filenames in os.walk("./results/get/input"):
            file_counts = len(filenames)
        real_input_name = apis.Increase_string(input_name,file_counts)
        real_output_name = apis.Increase_string(output_name,file_counts)
        #imwrite会自动转换通道数顺序，img已是正常的BGR图像，不能被改变，只能人为提前改变一次↓
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cv2.imwrite("./results/get/input/" + real_input_name + "." + type[6:10] ,img1)
        cv2.imwrite("./results/get/output/" + real_output_name + "." + type[6:10] , receive) 
        st.success("推理成功！如果想继续使用，重新上传新的图片即可！")
        st.write("输入图片已保存为./results/get/input/" + real_input_name + "." + type[6:10])
        st.write("输出结果已保存为./results/get/output/" + real_output_name + "." + type[6:10])
    else:
        st.error("请先上传图片！")