#################### Build-System Image ####################
FROM ubuntu:20.04 AS build-system

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG DEBIAN_FRONTEND=noninteractive
#
# Install apt-get basic tooling
RUN apt-get update && apt-get install --no-install-recommends -y \
    apt-utils \
    python3 \
    python3-pip \
    vim \
    git \
    clang\
    clang-12\
    make\
    gdb \
    ssh \
    curl \
    bash-completion \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
#
#Set sym links to tools
RUN ln -s /usr/bin/python3 /usr/bin/python \
    && rm -rf /usr/bin/pip \
    && ln -s /usr/bin/pip3 /usr/bin/pip
#
#Install cmake and conan
RUN pip install cmake \
    && pip install conan
#
# Add dev user with no root rights
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

#SET HOME DIR
ENV HOME /home/$USERNAME



#install git shell extension
#RUN curl -L https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh > ~/.bash_git && echo "source ~/.bash_git" >> ~/.bashrc
#RUN sed -Ei 's/(PS1=.*)(\\\[\\033\[00m\\\]\\\$.*)/\1\\[\\033[01;33m\\]$(__git_ps1)\2/p' ~/.bashrc

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog