import streamlit as st
import apis
import deploy
import cv2
import os

#基本UI布局
st.markdown("# 地物分类 ❄️")
st.sidebar.markdown("# 地物分类 ❄️")
st.sidebar.markdown("功能简介：")
st.sidebar.markdown("对遥感影像进行像素级内容解析，对遥感影像中感兴趣的类别进行提取和分类。")
st.write("欢迎使用地物分类功能！")
st.image("cls.png")

#初始文件名 每次进行同类预测 都会赋予初值
input_name = "input_01"
output_name = "output_01"
img = None
type = None

#UploadImg双返回值 如果用一般写法 未上传文件时会有报错提示影响交互
return_list = apis.UploadImg("请上传图片：")
if return_list is not None:
    img = return_list[0]
    type = return_list[1]

#推理部分、结果保存和异常显示
cfm = st.button("开始检测")
if cfm:
    if img is not None:
        receive = deploy.Predict_cls("model_cls",img)
        #得到文件夹内已有文件数（即已进行同类推理的次数） 便于后续文件命名 中途切换其他预测也无妨
        for dirpath, dirnames, filenames in os.walk("./results/cls/input"):
            file_counts = len(filenames)
        real_input_name = apis.Increase_string(input_name,file_counts)
        real_output_name = apis.Increase_string(output_name,file_counts)
        #imwrite会自动转换通道数顺序，img已是正常的BGR图像，不能被改变，只能人为提前改变一次↓
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #对地物分类而言，输出结果同样需要处理，这样最后呈现的还是BGR图
        receive1 = cv2.cvtColor(receive,cv2.COLOR_BGR2RGB)
        cv2.imwrite("./results/cls/input/" + real_input_name + "." + type[6:10] ,img1)
        cv2.imwrite("./results/cls/output/" + real_output_name + "." + type[6:10] , receive1) 
        st.success("推理成功！如果想继续使用，重新上传新的图片即可！")
        st.write("输入图片已保存为./results/cls/input/" + real_input_name + "." + type[6:10])
        st.write("输出结果已保存为./results/cls/output/" + real_output_name + "." + type[6:10])
    else:
        st.error("请先上传图片！")