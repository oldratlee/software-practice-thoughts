# 🐣  软件实践杂记

<img src="images/miscellany-icon.png" width="27%" align="right" />

[![知识共享协议（CC协议）](https://img.shields.io/badge/License-Creative%20Commons-FE6B3A.svg) ![Attribution-NonCommercial-ShareAlike CC BY-NC-SA](images/LICENSE.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)
[![GitHub stars](https://img.shields.io/github/stars/oldratlee/software-practice-miscellany.svg?style=social&label=Star)](https://github.com/oldratlee/software-practice-miscellany/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/oldratlee/software-practice-miscellany.svg?style=social&label=Fork)](https://github.com/software-practice-miscellany/software-practice-miscellany/fork)

记录与整理平时自己的

- 软件实践的讨论
- 软件实践主题的思考

主题不限，有趣有料就好～ 🥤

> 比起写博客，直接用`github`仓库的`Markdown`来记录真是简单省事！ 😂

## 实践讨论

- 软件实践碎碎念
    - [2021年](broken-thoughts/README.md)
    - [2020年](broken-thoughts/2020.md)
- Code Review
    - [`compileflow`开源项目的代码review](compiler-flow-code-review/README.md)

## 主题思考

- `SCM`
    - [Why `Git`](git/README.md)
    - [`Git`学习资料](git/study-material.md)
    - 分享PPT:
        - [Git/VCS的使用与原则 简介](git/git-usage-and-principle-v0.3.1.pptx)
        - [Git/GitLab(Github)使用](git/git-gitlab-usage.pptx)
- 如何做开源项目
    - 分享PPT：[开源漫游者指南：开源的工作内容与要点](hitchhikers-guide-to-open-source/开源漫游者指南-v0.9.1.pptx)
- 软件文档
    - [如何写一个`issue`](how-to-write-a-issue.md)
- 系统设计与分析
    - 分享PPT：[软件可靠性设计的实践](practice-of-software-reliability-design/软件可靠性设计的实践-v0.9.1.pptx)
    - [平台产品逻辑与执行](product-logic-for-platform-product/README.md)
    - [多响应异步请求模式下需求满足的分析模型](multi-respose-async-request-pattern-analysis-model/README.md)
        - 请求的3个关注维度：`CRC`；`CRC`也是请求的平衡维度，所谓平衡是指：当不可兼得时，可互相置换。
        - **请求所关注与平衡的CRC维度模型 也一样适用于 同步请求模式，并不耦合 多响应异步请求模式。**  
          只是多响应异步请求模式下的复杂性，在分析上对请求维度模型的需要变得迫切了。  
          我们可以用请求维度`CRC`模型作为 引入多响应异步请求模式后对产品/用户体验的优化程度 的一种度量方式。
        - 多响应/异步的模式下，相对于传统的同步模式，可以为业务提供了更灵活方便的策略。
    - [任务分发均匀性的模型量化分析](lb-distribution-uniformity-analysis/README.md)  
        - 任务分发在软件系统的很多地方会出现。
        - 任务分发/`LB`的均匀性是一个需要考虑的问题，会导致不必要的过载甚至宕机。
    - [`Cache`实践](cache-practice/README.md)  
        - 应用开发中，`Cache`毫无疑问是很重要的一块：提升应用性能的关键，降低像`DB`这样关键资源的负荷；
        - 但`Cache`的使用有很多要注意的问题与陷阱。
    - [系统`Load`的样子与计算方式](system-load-calculation-and-looks/README.md)  
      你常常看的`Load 1/5/15`是怎么回事？
- 编程语言
    - [`Lisp` Practice](lisp-practice/README.md)  
      对于大多数程序员来说，`Lisp`是编程语言中的一个神。
