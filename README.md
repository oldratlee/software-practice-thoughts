`Lisp` Practice
=======================

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Quick Start](#quick-start)
  - [`lisp`安装](#lisp%E5%AE%89%E8%A3%85)
    - [`Steel Bank Common Lisp`](#steel-bank-common-lisp)
    - [`CLISP`](#clisp)
    - [`lisp`运行时介绍](#lisp%E8%BF%90%E8%A1%8C%E6%97%B6%E4%BB%8B%E7%BB%8D)
  - [web application quick start](#web-application-quick-start)
- [相关资料](#%E7%9B%B8%E5%85%B3%E8%B5%84%E6%96%99)
  - [`lisp`文章](#lisp%E6%96%87%E7%AB%A0)
  - [`lisp`书籍](#lisp%E4%B9%A6%E7%B1%8D)
  - [已有的资料汇编](#%E5%B7%B2%E6%9C%89%E7%9A%84%E8%B5%84%E6%96%99%E6%B1%87%E7%BC%96)
  - [个人整理资料](#%E4%B8%AA%E4%BA%BA%E6%95%B4%E7%90%86%E8%B5%84%E6%96%99)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

Quick Start
---------------

### `lisp`安装

我偷懒了 :smile: ，只说明了`Mac`下的安装方式，如果是`Linux`下通过包管理器有类似简单安装方法。

#### `Steel Bank Common Lisp`

`Mac`下安装

```bash
brew install sbcl
```

[`sbcl`的官网](http://www.sbcl.org/)

#### `CLISP`

`Mac`下安装

```bash
brew install clisp
```

[`clisp`的官网](http://www.clisp.org/)

#### `lisp`运行时介绍

有哪些`lisp`运行时可以看看下面的这个链接，简单了解一下：

- [Free Common Lisp Compilers, Interpreters, Development Systems](http://www.thefreecountry.com/compilers/commonlisp.shtml)

### web application quick start

参见 [从零开始，给出完整运行起一个`Lisp` `web`框架`clack`的`Hello World`应用](lisp-web-app-quick-start.md)。

相关资料
-------------------

### `lisp`文章

- [`lisp`学习之路](http://daiyuwen.freeshell.org/gb/lisp.html)
    - [`Lisp`之根源](http://daiyuwen.freeshell.org/gb/rol/roots_of_lisp.html)
    - [创造者的鉴赏力](http://daiyuwen.freeshell.org/gb/taste/taste.html)
- [`Lisp`的永恒之道](http://coolshell.cn/articles/7526.html)
- [为什么`Lisp`语言如此先进？（译文）](http://www.ruanyifeng.com/blog/2010/10/why_lisp_is_superior.html)
- [`Google Common Lisp`风格指南](http://lisp.es/Google-Common-Lisp-Style-Guide/GoogleCLSG-zhCN.xml) / [Google Common Lisp Style Guide](http://google-styleguide.googlecode.com/svn/trunk/lispguide.xml)  
模式意味着“我的语言不够用了。” ── *Rich Hickey*  
`Common Lisp`是一个强大的多范式程序语言。能力越强，责任越大。
    - 来自[Style guides for Google-originated open-source projects](https://code.google.com/p/google-styleguide/)  
      `Google`各种语言的代码风格指南。
- [`LISP` - 维基百科](http://zh.wikipedia.org/wiki/LISP)
- [`Common Lisp` - 维基百科](http://zh.wikipedia.org/wiki/Common_Lisp)

### `lisp`书籍

- [`ANSI Common Lisp`中文版](http://acl.readthedocs.org/en/latest/zhCN/index.html)
- [`The Common Lisp Cookbook`](http://cl-cookbook.sourceforge.net/index.html)
- [通向`Lisp`之路 - 书籍豆列](http://book.douban.com/doulist/1128439/)
- [想要学习`Lisp`，应该看哪些书、上哪些论坛呢？ - 知乎](http://www.zhihu.com/question/19621539)
- [学习 `LISP` 有哪些网站或书籍推荐？ - 知乎](http://www.zhihu.com/question/19711404)

### 已有的资料汇编

- [Awesome Common Lisp](https://github.com/CodyReichert/awesome-cl)

### 个人整理资料

- [`Lisp`书籍推荐和点评](https://github.com/oldratlee/translations/blob/master/recommend-lisp-books/README.md)
    - 特别提一下[学习`lisp`的书籍推荐](https://github.com/oldratlee/translations/blob/master/recommend-lisp-books/recommend-lisp-books.md)。这篇文章难能可贵地点评了几本书的风格和优劣。    
        让我知道**_Successful Lisp: How to Understand and Use Common Lisp_**这本入门的好书。[在线版](http://psg.com/~dlamkins/sl/contents.html) / [`PDF`版](http://ebixio.com/online_docs/SuccessfulLisp.pdf)  
        由于`LISP`与其它语言从**基本概念**就开始的差异，已有的语言经验反而是个学习阻碍，深入浅出的巧妙讲解对入门太重要了。
