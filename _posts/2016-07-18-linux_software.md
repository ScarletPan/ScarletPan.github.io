---
layout: post
title: Software config in linux
tags: linux
comments: false
modifed: 2016-07-18
---

# 目录

* [搜狗拼音](#1)
* [SS-link](#2)
* [Git](#4)
* [Ruby](#5)
* [Nodejs](#6)
* [Jekyll](#7)
* [Mysql](#8)
* [Apache](#9)


### <h2 id="1"> [1] &emsp;Sougoupinyin</h2>
1. download from website
2. ``` $ sudo dpkg -i sogoupinyin_2.0.0.0078_amd64.deb```
3. ``` $ sudo apt-get install -f```
4. ``` $ sudo dpkg -i sogoupinyin_2.0.0.0078_amd64.deb```

### <h2 id="2"> [2] &emsp; Shadowsocks Qt-5 + SwitchyOmega</h2>
1. 下载

```
$ sudo add-apt-repository ppa:hzwhuang/ss-qt5
$ sudo apt-get update
$ sudo apt-get install shadowsocks-qt5
```

2. setting->network->proxy->socks host + port.
3. add SwitchyOmega into chromium

### <h2 id="3"> [3] &emsp; Atom text edit </h2>
```
$ sudo add-apt-repository ppa:webupd8team/atom
$ sudo apt-get update
$ sudo apt-get install atom
```

### <h2 id="4"> [4] &emsp; git </h2>

1. 下载：

```
$ sudo apt-get git
```
2. 配置：

```
$ git config --global user.name "ScarletPan"
$ git config --global user.email "myscarlet@sina.com"
$ ssh-keygen -t rsa -C "myscarlet@sina.com" #生成 ssh-key
$ eval "$(ssh-agent -s)" # 检查ssh-agent
$ ssh-add ~/.ssh/id_rsa # 将新产生的秘钥加入
$ gedit .ssh/id_rsa.pub # 将内容复制到github用户SSH-key中
```

### <h2 id="5"> [5] &emsp; ruby</h2>
1. 下载：

```
$ sudo apt-get install ruby2.3
```
2. 配置

```
$ gem source -r https://rubygems.org/  #更换到内陆的下载源
$ gem source -a https://ruby.taobao.org
$ sudo apt-get install ruby-dev
```

### <h2 id="6"> [6] &emsp; Nodejs </h2>
```
$ sudo apt-get install nodejs # nodejs -v4.2.6
```

### <h2 id="7"> [7] &emsp; jekyll </h2>
```
$ sudo gem install jekyll
$ sudo gem install jekyll-sitemap
$ sudo gem install jekyll-paginate
$ sudo gem install jekyll-gist
$ sudo gem install redcarpet
```

### <h2 id="8"> [8] &emsp; mysql </h2>
```
$ sudo apt-get install mysql-server
```
```
$ mysql_secure_installation
```
&emsp; The first question will ask if you want to change the root password, but because you just set it, enter n. For all other questions, press ENTER to accept the default response.

### <h2 id="9"> [9] &emsp; apache </h2>
参考：[python + apache + django 配置  ]("https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04")
