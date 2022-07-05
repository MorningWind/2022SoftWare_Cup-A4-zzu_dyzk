import cv2
import numpy as np
import paddlers as pdrs
import streamlit as st
import paddle
from paddlers.tasks.utils.visualize import visualize_detection

def read_image(path):
    im = cv2.imread(path)
    return im[...,::-1]

#目标提取功能部署
def Predict_get(model_dir,input):
    #避免求梯度，节省资源
    with paddle.no_grad():
        predictor = pdrs.deploy.Predictor(model_dir,use_gpu=True)
        result = predictor.predict(img_file=input,warmup_iters=0)
    #获取预测结果
    result_picture = result['label_map']
    col1, col2 = st.columns(2)
    with col1:
        st.write("输入图像")
        st.image(input)
    with col2:
        if isinstance(result_picture, str):
            result_picture = read_image(result_picture)
        result_picture = (result_picture*255).astype('uint8')
        if result_picture.ndim == 2:
            result_picture = np.tile(result_picture[...,np.newaxis], [1,1,3])
        st.write("输出结果")
        st.image(result_picture)
    return result_picture
        
#变化检测功能部署
def Predict_change_det(model_dir,input1,input2):
    #避免求梯度，节省资源
    with paddle.no_grad():
        predictor = pdrs.deploy.Predictor(model_dir,use_gpu=True)
        result = predictor.predict(img_file=(input1,input2),warmup_iters=0)
    #获取预测结果
    result_picture = result['label_map']
    rs = (result_picture*255).astype('uint8')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("输入图像1")
        st.image(input1)
    with col2:
        st.write("输入图像2")
        st.image(input2)
    with col3:
        st.write("输出结果")
        st.image(rs)
    return rs
 
 #目标检测功能部署
def Predict_det(model_dir,input):
      #避免求梯度，节省资源
    with paddle.no_grad():
        predictor = pdrs.deploy.Predictor(model_dir,use_gpu=True)
        #获取预测结果
        result = predictor.predict(img_file=input,warmup_iters=0)
    col1, col2 = st.columns(2)
    with col1:
        st.write("输入图像")
        st.image(input)
    with col2:
        vis = input
        #遍历所有可能的“操场(list格式)”(可应对一图多操场情况)
        for i in result:
            #如果得分高于0.3 认为此处有操场
            if i["score"] > 0.3:
                #获取坐标信息和score
                box = [int(i["bbox"][0]),int(i["bbox"][1]),int(i["bbox"][2]),int(i["bbox"][3]),i["score"]]
                gt = [{
                'category': "playground", 
                'bbox': [box[0], box[1], box[2], box[3]], 
                'score': box[4]
                }]
                #画出预测框 
                vis = visualize_detection(
                np.array(vis), gt, threshold=0.3,
                color=np.asarray([[0,0,255]], dtype=np.uint8), 
                save_dir=None
            )
        st.write("输出结果")
        st.image(vis)
        return vis

#地物分类功能部署
def Predict_cls(model_dir,input):
    #避免求梯度，节省资源
    with paddle.no_grad():
        predictor = pdrs.deploy.Predictor(model_dir,use_gpu=True)
        result = predictor.predict(img_file=input,warmup_iters=0)
    #获取预测结果
    result_picture = result['label_map']
    col1, col2 = st.columns(2)
    with col1:
        st.write("输入图像")
        st.image(input)
    with col2:
        st.write("输出结果")
        lut = get_lut()
        if isinstance(result_picture, str):
            result_picture = cv2.imread(result_picture, cv2.IMREAD_COLOR)
        if result_picture.ndim == 3:
                result_picture = cv2.cvtColor(result_picture, cv2.COLOR_BGR2GRAY)
        result_picture = lut[result_picture]
        st.image(result_picture)
    return result_picture

#地物分类附：颜色对应表
def get_lut():
    lut = np.zeros((256,3), dtype=np.uint8)
    lut[0] = [255, 0, 0]
    lut[1] = [30, 255, 142]
    lut[2] = [60, 0, 255]
    lut[3] = [255, 222, 0]
    lut[4] = [0, 0, 0]
    return lut