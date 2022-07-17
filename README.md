# Image Classification Web Application :cat: :dog:

## 功能说明
使用pytorch自带的模型和预训练权重制作web服务器，别人可以通过上传照片在进行预测分类结果。整理流程是先本地搭建好环境，可以运行出本地网页进行测试，之后部署成为服务器，任何人都可以通过链接进行测试。这一步主要使用streamlit cloud。详细讲解请到csdn中查看https://blog.csdn.net/cp1314971/article/details/125832450?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22125832450%22%2C%22source%22%3A%22cp1314971%22%7D&ctrtid=LjRZu


## 安装步骤如下

conda create -n web python=3.7

activate web

conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch

pip install streamlit

注意不要使用requirements.txt进行环境安装，因为在部署阶段streamlit cloud也是直接连接到github仓库中，在streamlit cloud中已经存在streamlit的环境。

## 运行代码
在终端切换到当前文件夹的命令下

streamlit run app.py

## 部署

请参看streamlit官方说明，此代码的环境是python3.7，同样需要在streamlit cloud创建中选择好python版本 https://docs.streamlit.io/
