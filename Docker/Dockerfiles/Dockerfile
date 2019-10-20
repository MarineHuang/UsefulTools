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
 && apt-get -y install vim cmake git unzip wget bzip2 iputils-ping \
 && wget https://raw.githubusercontent.com/MarineHuang/UsefulTools/master/conf/.bashrc_marinehuang -O ~/.bashrc_marinehuang \
 && echo "[ -f ~/.bashrc_marinehuang ] && . ~/.bashrc_marinehuang" >> ~/.bashrc \
 && wget https://raw.githubusercontent.com/MarineHuang/UsefulTools/master/conf/.vimrc_marinehuang -O ~/.vimrc

# Install Java
#RUN wget --quiet https://raw.githubusercontent.com/MarineHuang/UsefulTools/master/Software/oracle/java_se/jdk-11.0.1_linux-x64_bin.tar.gz -O /opt/jdk.tar.gz \
# && tar -xzvf /opt/jdk.tar.gz \
# && rm /opt/jdk.tar.gz \
# && echo "# JAVA" >> ~/.bashrc \
# && echo "export JAVA_HOME=/opt/jdk" >> ~/.bashrc \
# && echo "export PATH=$JAVA_HOME/bin:$PATH" >> ~/.bashrc \
# && echo "export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar" >> ~/.bashrc
 
# Install Tomcat
RUN wget --quiet https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-8/v8.5.47/bin/apache-tomcat-8.5.47.tar.gz -O /opt/tomcat.tar.gz \
 && tar -xzvf /opt/tomcat.tar.gz \
 && rm  /opt/tomcat.tar.gz 

# Install anaconda 
RUN wget --quiet https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh  \
 && /bin/bash ~/anaconda.sh -b -p /opt/conda  \
 && rm ~/anaconda.sh  \
 && echo "# anaconda" >> ~/.bashrc \
 && echo "export PATH=/opt/conda/bin:$PATH" >> ~/.bashrc

