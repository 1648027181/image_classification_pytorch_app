# Image Classification Web Application :cat: :dog:

## 功能说明
使用pytorch自带的模型和预训练权重制作web服务器，别人可以通过上传照片在进行预测分类结果。整理流程是先本地搭建好环境，可以运行出本地网页进行测试，之后部署成为服务器，任何人都可以通过链接进行测试。这一步主要使用streamlit cloud。


## 安装步骤如下

conda create -n web python=3.7
activate web
conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch
pip install streamlit

