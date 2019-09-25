# Computer-Network-Course-Project

#### CN_W2_Project_Progress

#### 目前已完成的进度

- 完成了确定选题、初步构思

  - 用Python搭建实现以下功能的GUI：

    - [ ] GUI界面搭建(Tkinter)
    - [ ] 登陆常用邮箱(poplib, temp)
      - [x] 163
      - [ ] QQ
      - [ ] outlook
      - [ ] mails.tsinghua
      - [ ] sem.tsinghua

    - [x] 收取和查看已有邮件(re, base64, quoari)
      - [x] 所有时间
      - [ ] 支持刷新
      - [ ] 根据需要加载
    - [ ] 删除邮件
    - [ ] 回复/发送邮件
    - [ ] 退出邮箱

#### 未来一周要完成的任务

- 完成收取和查看已有邮件
- 完成删除邮件
- 完成GUI的初步搭建

#### 笔记

##### MIME 协议

- 常见格式为：
  - ![snip_1](misc/snip_1.png)
  - 其中：
    - 标红框的是基本结构，包括邮件的Send address, Date, From, To,  Subject等
    - 表绿色框的是MIME协议下分隔各个邮件数据的标识符boundary
    - 表淡蓝色框的是分隔邮件头和邮件体的空行
    - 表橙色框的是表示邮件该部分内容的数据为utf-8字符集(charset)、Base64编码(encoding)的格式，图中第二个橙色框的数据解码为“网易商城”
- 关于Document-Type
  - 常见格式包括
    - multipart/mixed: used in mail head
    - multipart/alternative: used in mail head
    - text/html: html
    - text/plain: plain text
- 关于字符集和编码
  - 字符集
    - byte
    - utf-8
  - 编码
    - B: base64
    - Q: quoted-printable
    - 7bit or 8bit: not found yet

##### 处理MIME协议格式的初步设想

- 获得邮件初始信息
- capture信件基本信息
  - 包括
    - from
    - to
    - date
    - cc
    - boundary
- 根据boundary获取信件内容
- 根据charset, content-transfer-encoding正确编译数据
- 根据content-type显示不同内容

##### 难点

- 回信的识别和处理
- 附件的识别和处理

##### Tkinter

wedgetsxuan'y

- How Listbox and Other wedgets link
  - Listbox.curselection() 
    - returns the index of chosen items preset in the listbox object
- How to present MIME context in Tkinter GUI
- How to refresh mailbox