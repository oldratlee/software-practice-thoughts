Lisp Web App Quick Start
==============================

从零开始，给出完整运行起一个`Lisp` `web`框架`clack`的`Hello World`应用的步骤。

安装`Lisp`环境
------------------------

```bash
brew install sbcl
```

这里安装的是`sbcl`（[Steel Bank Common Lisp](http://www.sbcl.org/)）。

安装`Quicklisp`库管理器
------------------------

### 下载`Quicklisp`

```bash
curl -O http://beta.quicklisp.org/quicklisp.lisp
```

### 加载`Quicklisp`运行`sbcl`

```bash
sbcl --load quicklisp.lisp
```

### 在`sbcl`中完成安装`Quicklisp`

```lisp
(quicklisp-quickstart:install :path "/Users/jerry/.quicklisp/")
```

> 注意1：  
缺省是安装在`$HOME/quicklisp/`，如果安装到`$HOME/.quicklisp/`
```lisp
(quicklisp-quickstart:install :path "/Users/jerry/.quicklisp/")
```  
注意把`/Users/jerry/.quicklisp/`换成你的`HOME`目录的路径。

> 注意2：  
如果已经安装过了并有了`Quicklisp`的目录，则执行
```lisp
(load #P"/Users/jerry/quicklisp/setup.lisp")
```  
后面是字符串是`<Quicklisp目录>/setup.lisp`。

### 缺省加载`Quicklisp`

```lisp
(ql:add-to-init-file)
```  
这样退出了`sbcl`再进入会自动加载`Quicklisp`，省得手动重复加载过程。

> 注意1：  
退出`sbcl`可以用：
```lisp
(quit)
```

运行`clack`框架的`Hello World`应用
------------------------

### 导入`clack`库

```lisp
(ql:quickload :clack)
```

第一次会触发下载`clack`，需要一些时间。

### 启动`Hello World`应用

```lisp
(clack:clackup
  (lambda (env)
    (declare (ignore env))
    '(200 (:content-type "text/plain") ("Hello, Clack!"))))
```

访问<http://127.0.0.1:5000/>，可以看到`Hello, Clack!`。

### 关闭`HTTP`服务

```lisp
(clack:stop *)
```

参考资料
------------------------

- [Quicklisp](http://www.quicklisp.org/beta/)
    - [Making a small Lisp project with quickproject and Quicklisp](http://xach.livejournal.com/278047.html)
- [Getting Clack](http://clacklisp.org/tutorial/02-getting-clack.html)
    - [Clack](http://clacklisp.org/)
