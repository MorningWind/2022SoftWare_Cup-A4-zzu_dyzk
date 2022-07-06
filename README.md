# 遥感图像自动解译系统 #
## ——简介及使用说明 ##

本系统由**郑州大学**本科生团队zzu_dyzk队（钱昊晨、杨晓阳）设计，直接面向2022年**软件杯**A4赛道——基于百度飞桨的遥感图像智能解译平台，也可作为**遥感、深度学习**与**Web**系统相结合的简单案例。

本系统主要具有**变化检测、地物分类、目标检测、目标提取**四大功能。


## 系统开发简介 ##
我们的遥感图像自动解译系统是完全使用**Python**语言开发，基于**Streamlit**库实现前端Web设计、基于**Paddlepaddle**和**PaddleRS**库实现后端功能部署，使用**本地算力**推理而不需要联网使用的系统。

### 核心库简介： ###

1.**Streamlit**：Streamlit是一个基于 Python 的 Web 应用程序框架，致力于以更高效、更灵活的方式可视化数据，并分析结果。它是一个开源库，可以帮助数据科学家和学者在短时间内开发机器学习 (ML) 可视化仪表板。只需几行代码，我们就可以构建并部署强大的数据应用程序。

2.**Paddlepaddle**：飞桨(PaddlePaddle)是集深度学习核心框架、工具组件和服务平台为一体的技术先进、功能完备的开源深度学习平台，已被中国企业广泛使用，深度契合企业应用需求，拥有活跃的开发者社区生态。提供丰富的官方支持模型集合，并推出全类型的高性能部署和集成方案供开发者使用。（摘自飞桨官网）

3.**PaddleRS**：PaddleRS是基于飞桨开发的遥感处理平台，支持遥感图像分类，目标检测，图像分割，以及变化检测等常用遥感任务，帮助开发者更便捷地完成从训练到部署全流程遥感深度学习应用。

使用的其他诸如Opencv-python（用于图像处理）、Numpy（用于数据处理）等常用库不一一赘述。

开发工具方面，我们使用Anaconda3包管理工具+Vscode的组合。

## 使用说明 ##
### 完成四步即可直接运行本系统： ###
1.安装Anaconda3包管理工具（已有则跳过）

官网下载地址：[https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe](https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe)

百度网盘下载地址：[https://pan.baidu.com/s/1F44GBvhPM2Im5TRpeOXHcQ](https://pan.baidu.com/s/1F44GBvhPM2Im5TRpeOXHcQ)
提取码：0086

2.环境配置

代码运行需要的环境environment已经放在release中

另附百度网盘下载地址：[https://pan.baidu.com/s/1cAx2gCaE995dXTGFrhmzXg](https://pan.baidu.com/s/1cAx2gCaE995dXTGFrhmzXg)
提取码：0086

下载并解压后直接放在本地**Anaconda3/envs**目录下即可

也可以选择自己进行环境配置，所用的依赖及对应版本已经放在requirements.txt中（不推荐）

环境必须以**environment**命名，否则下文的start.bat将失效，需要修改bat文件内容或自己激活环境运行。

3.模型下载

change_det（变化检测）、cls（地物分类）、det（目标检测）、get（目标提取）所需部署格式的模型已经放在release中，同样防止下载速度较慢，提供百度网盘下载链接：[https://pan.baidu.com/s/14wrRFztdRNqWGezlW-Yw5w](https://pan.baidu.com/s/14wrRFztdRNqWGezlW-Yw5w)提取码：0086

也可自己训练模型，但要保证导出格式被PaddleRS所支持，可在百度提供的baseline基础上进行训练：

[变化检测](https://aistudio.baidu.com/aistudio/projectdetail/3684588?channelType=0&channel=0)
[地物分类](https://aistudio.baidu.com/aistudio/projectdetail/3792606?channelType=0&channel=0)
[目标检测](https://aistudio.baidu.com/aistudio/projectdetail/3792609?channelType=0&channel=0)
[目标提取](https://aistudio.baidu.com/aistudio/projectdetail/3792610?channelType=0&channel=0)

得到模型后，须以对应名称**model_ + 功能名**（即我提供的模型文件夹名）命名放置在**code目录**下方可正常运行（否则需要修改代码路径）

4.双击code目录下的start.bat文件即可运行

start.bat批处理文件本质是集合了激活环境、运行主页文件指令。

## 代码引用说明 ##

1.streamlit库函数：[https://docs.streamlit.io/library/api-reference](https://docs.streamlit.io/library/api-reference)

2.部署基本流程源自PaddleRS百度官方：

[https://github.com/PaddleCV-SIG/PaddleRS/tree/develop/deploy](https://github.com/PaddleCV-SIG/PaddleRS/tree/develop/deploy)

[
https://github.com/PaddleCV-SIG/PaddleRS/tree/develop/deploy/export](https://github.com/PaddleCV-SIG/PaddleRS/tree/develop/deploy/export)

3.四项功能的部署思想借鉴百度官方的4个baseline方案（即上述训练模型处四个链接）

## 传送门 ##
点击查看本系统的具体**功能介绍**↓

[遥感图像自动解译系统——功能介绍](https://github.com/MorningWind/2022SoftWare_Cup-A4-zzu_dyzk/blob/master/code/README.md)

