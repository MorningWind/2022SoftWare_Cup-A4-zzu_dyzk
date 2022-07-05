import streamlit as st
import apis
import deploy
import cv2
import os

#基本UI布局
st.markdown("# 变化检测 🎶")
st.sidebar.markdown("# 变化检测 🎶")
st.sidebar.markdown("功能简介：")
st.sidebar.markdown("给定两张不同时间拍摄的相同位置（地理配准）的遥感图像，定位出其中建筑变化的区域。")
st.write("欢迎使用变化检测功能！")
st.image("change_det.png")

#初始文件名 每次进行同类预测 都会赋予初值
input_A_name = "input_A_01"
input_B_name = "input_B_01"
output_name = "output_01"

#UploadImg双返回值 如果用一般写法 未上传文件时会有报错提示影响交互
return_list1 = apis.UploadImg("请上传第一张图片(对应前时相A类)：")
if return_list1 is not None:
    img1 = return_list1[0]
    type1 = return_list1[1]

return_list2 = apis.UploadImg("请上传第二张图片(对应后时相B类)：")
if return_list2 is not None:
    img2 = return_list2[0]
    type2 = return_list2[1]

#推理部分、结果保存和异常显示
cfm = st.button("开始检测")
if cfm:
    if img1 is not None and img2 is not None:
        receive = deploy.Predict_change_det("model_change_det",img1,img2)
        #得到文件夹内已有文件数（即已进行同类推理的次数） 便于后续文件命名 中途切换其他预测也无妨
        for dirpath, dirnames, filenames in os.walk("./results/change_det/input_A"):
            file_counts = len(filenames)
        real_input_A_name = apis.Increase_string(input_A_name,file_counts)
        real_input_B_name = apis.Increase_string(input_B_name,file_counts)
        real_output_name = apis.Increase_string(output_name,file_counts)
        #imwrite会自动转换通道数顺序，img已是正常的BGR图像，不能被改变，只能人为提前改变一次↓
        img3 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        img4 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
        cv2.imwrite("./results/change_det/input_A/" + real_input_A_name + "." + type1[6:10] ,img3)
        cv2.imwrite("./results/change_det/input_B/" + real_input_B_name + "." + type2[6:10] ,img4)
        cv2.imwrite("./results/change_det/output/" + real_output_name + "." + type1[6:10] , receive)
        st.success("推理成功!如果想继续使用，重新上传新的图片即可！")
        st.write("输入图片已保存为./results/change_det/input/" + real_input_A_name + "." + type1[6:10])
        st.write("输入图片已保存为./results/change_det/input/" + real_input_B_name + "." + type2[6:10])
        st.write("输出结果已保存为./results/change_det/output/" + real_output_name + "." + type1[6:10])
    else:
        st.error("请先上传图片！")
