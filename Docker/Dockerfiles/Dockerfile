# ubuntu 16.04 xenial
# Anaconda3-5.0.1


FROM ubuntu:xenial-20190904

MAINTAINER MarineHuang

# Install basic tools
RUN set -ex \
 && echo "" > /etc/apt/sources.list \
 && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get -y install vim cmake git unzip wget bzip2 \
 && wget https://raw.githubusercontent.com/MarineHuang/UsefulTools/master/bashrc/.bashrc_marinehuang -O ~/.bashrc_marinehuang \
 && echo "[ -f ~/.bashrc_marinehuang ] && . ~/.bashrc_marinehuang" >> ~/.bashrc

# Install anaconda 
RUN wget --quiet https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh  \
 && /bin/bash ~/anaconda.sh -b -p /opt/conda  \
 && rm ~/anaconda.sh  \
 && echo "export PATH=/opt/conda/bin:$PATH" >> ~/.bashrc

