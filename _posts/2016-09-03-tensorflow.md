---
layout: post
title: 极简的深度学习环境搭建(Nvidia GTX850 + cuda8.0 + tensorflow0.10.0 + ubuntu 16.04)
tags: Deep_learning
comments: true
modifed: 2016-09-03
---

## 1 &emsp; Linux 版本
<center>![pic1](http://o6qr23o6z.bkt.clouddn.com/post_16-09-03-1.png)</center>

## 2 &emsp; GPU 信息
<center>![pic2](http://o6qr23o6z.bkt.clouddn.com/post_16-09-03-2.png)</center>

## 3 &emsp; 安装nvidia驱动
在software & update中直接更改即可, 由于cuda对驱动版本要求高, 因此最好选择361．安装完后重启一下
<center>![pic3](http://o6qr23o6z.bkt.clouddn.com/post_16-09-03-3.png)</center>

## 4 &emsp; 安装cuda 8.0
* 前往 [cuda下载页面](https://developer.nvidia.com/cuda-release-candidate-download)
* 注册（如果还没有账号）
* 选择deb下载
<center>![pic4](http://o6qr23o6z.bkt.clouddn.com/post_16-09-03-4.png)</center>
* 下载成功后在本地解包安装

```linux
$ sudo dpkg -i cuda-repo-ubuntu1604-8-0-rc_8.0.27-1_amd64.deb
$ sudo apt-get update
$ sudo apt-get install cuda
```

* 设置环境变量
<p>在.bashrc中输入下列语句：</p>

```
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"
export CUDA_HOME=/usr/local/cuda
```

* 测试(以1_Utilities/deviceQuery为例)：

```
$ cd /usr/local/cuda/samples/1_Utilities/deviceQuery
$ make
$ ./deviceQuery
```
&emsp;成功后大概长这样：
<center>![pic5](http://o6qr23o6z.bkt.clouddn.com/post_16-09-03-5.png)</center>

**UPDATE** 

* 装了cuda 8运行pip下载的tensorflow会出现问题。如果读者出现问题，可以考虑安装7.5
* cuda7.5并没有支持ubuntu16.04。但可以参考这个[博文](https://www.pugetsystems.com/labs/hpc/NVIDIA-CUDA-with-Ubuntu-16-04-beta-on-a-laptop-if-you-just-cannot-wait-775/)

## 5 &emsp; 部署cudnn4.0
1. 前往　[cudnn下载页面](https://developer.nvidia.com/cudnn)
2. 下载相应版本的cudnn4
3. 将相应内容拷贝到cuda目录中

```
tar xvzf cudnn-7.5-linux-x64-v4.tgz
sudo cp cuda/include/cudnn.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
```

## 6 &emsp; 安装相应的tensorflow
前往 [tensorflow官网](https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html)，其中列举了不少安装方式，安装带gpu的版本

## 7 &emsp; 测试
可以用tensorflow自带的sample测试,可以看到gpu相对与cpu测试速度有很大的提升：
<p> cpu版本 </p>
<center>![pic6](http://o6qr23o6z.bkt.clouddn.com/post_16-09-03-6.png)</center>
<p> gpu版本 </p>
<center>![pic7](http://o6qr23o6z.bkt.clouddn.com/post_16-09-03-7.png)</center>
