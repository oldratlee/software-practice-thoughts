# 📚 🐣 软件实践文集

<a href="##"><img src="images/miscellany-icon.png" width="15%" align="right" /></a>

[![知识共享协议（CC协议）](https://img.shields.io/badge/License-Creative%20Commons-FE6B3A.svg?logo=apache) ![Licence: CC BY-NC-SA 4.0](images/LICENSE.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)  
[![GitHub stars](https://img.shields.io/github/stars/oldratlee/software-practice-miscellany.svg?style=social&label=Star)](https://github.com/oldratlee/software-practice-miscellany/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/oldratlee/software-practice-miscellany.svg?style=social&label=Fork)](https://github.com/software-practice-miscellany/software-practice-miscellany/fork)

记录与整理平时自己的

- 软件实践的讨论
- 软件实践主题的思考

主题不限，有趣有料就好～ 🥤

> PS：比起写博客，直接用`github`仓库的`Markdown`来记录真是简单省事！ 😂

- 🙈 [自己](http://weibo.com/oldratlee)写的这些内容难免有不足和不对之处，欢迎 👏
    - 建议，[提交`Issue`](https://github.com/oldratlee/software-practice-miscellany/issues/new)
    - 指正，[`Fork`后提通过`Pull Request`贡献修改](https://github.com/oldratlee/software-practice-miscellany/fork)
- 如果理解上有疑问 或是 应用过程中碰到疑惑，请[提交 🙌 `Issue`](https://github.com/oldratlee/software-practice-miscellany/issues/new) ，一起学习交流讨论！

----------------------------------------

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [⏳ 按内容时间排序](#-%E6%8C%89%E5%86%85%E5%AE%B9%E6%97%B6%E9%97%B4%E6%8E%92%E5%BA%8F)
- [🎵 按内容主题分类](#-%E6%8C%89%E5%86%85%E5%AE%B9%E4%B8%BB%E9%A2%98%E5%88%86%E7%B1%BB)
    - [实践讨论](#%E5%AE%9E%E8%B7%B5%E8%AE%A8%E8%AE%BA)
    - [如何做开源项目](#%E5%A6%82%E4%BD%95%E5%81%9A%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE)
    - [系统设计与分析](#%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1%E4%B8%8E%E5%88%86%E6%9E%90)
    - [`SCM`](#scm)
    - [软件文档](#%E8%BD%AF%E4%BB%B6%E6%96%87%E6%A1%A3)
    - [编程语言](#%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

----------------------------------------

# ⏳ 按内容时间排序

<a href="##"><img src="images/miscellany-icon.png" width="15%" align="right" /></a>

> 下一节是 [⬇️ **按内容主题分类** ⬇️](#-%E6%8C%89%E5%86%85%E5%AE%B9%E4%B8%BB%E9%A2%98%E5%88%86%E7%B1%BB)

- **2025-10** [并发任务编排的实现与设计 —— 以`Java CompletableFuture`为例](implementation-n-design-of-concurrency-orchestration/)
- **2021年** [软件实践碎碎念](broken-thoughts/README.md)
- **2021-06** [平台产品逻辑与执行](product-logic-for-platform-product/README.md)
    - **全接管业务的功能** 是平台的目标，直接体现了平台的核心竞争力。  
      全接管业务的平台功能的多少/比例 可以用来度量 平台的成熟程度。
    - 在平台产品功能中，要区分 哪些是接管的功能，哪些是整合的功能。
    - **不要用美好正义的愿望 来替代 残酷务实的逻辑。**  
      即产品逻辑 推演要包含给出 如何『做成』一个产品（可行性），而不仅是给出 为什么要『要做』一个产品（有需求）。
    - 排除法 对于不确定的规划的事 是不适用的；因为 事情是不是有解/整体组合功能是不是能发展出来 还是未知的。
- **2021-04** [多响应异步请求模式下需求满足的分析模型](multi-response-async-request-pattern-analysis-model/README.md)
    - 请求的3个关注维度`CRC`：**完整性**（`Completeness`）、**响应性**（`Responsiveness`）与**正确性**（`Correctness`）。
    - `CRC`也是请求的平衡维度，所谓平衡是指：当不可兼得时，可互相置换。
    - **请求所关注与平衡的CRC维度模型 也一样适用于 同步请求模式，并不耦合 多响应异步请求模式。**  
      只是多响应异步请求模式下的复杂性，在分析上对请求维度模型的需要变得迫切了。  
      我们可以用请求维度`CRC`模型作为 引入多响应异步请求模式后对产品/用户体验的优化程度 的一种度量方式。
    - 多响应/异步的模式下，相对于传统的同步模式，可以为业务提供了更灵活方便的策略。
- **2020年** [软件实践碎碎念](broken-thoughts/2020.md)
- **2020-08** [`compileflow`开源项目的Code Review](compiler-flow-code-review/README.md)
    - Review与交流讨论的过程 是自己整理学习的过程。大部分的整理内容 其实是独立于具体的一个开源项目。
    - 涉及如 代码实现（文档、可靠性、专业性）、系统设计（领域/模型拆分的原则与实践、扩展设计）、工程实践（版本管理、构建、测试）。
- **2020-08** | 2017-08 … 2014 分享PPT [软件可靠性设计的实践](practice-of-software-reliability-design/软件可靠性设计的实践-v0.9.2.pptx)
- **2020-07** 分享PPT [Git/VCS的使用与原则 简介](git/git-usage-and-principle-v0.3.1.pptx)
- **2020-03** [系统`Load`的样子与计算方式](system-load-calculation-and-looks/README.md)  
  你常常看的`Load 1/5/15`是怎么回事？
- **2020-02** 分享PPT [开源漫游者指南：开源的工作内容与要点](hitchhikers-guide-to-open-source/开源漫游者指南-v0.9.1.pptx)
    - 开源是一个充分竞争的环境，不能没有差异化或有明显缺陷，有问题无法隐藏。竞争三要素：1) 成本 2) 差异化 3) 专业化
        - 产品有明确的独特性、差异化（性能/功能） => 拉新/启动
        - 产品界面的部分 重要 => 留存
        - 持续发版/用户(大)Case收集透出（活跃、质量） => 流失 vs. 口碑传播
    - 伸手当是主流；一般用户成为贡献者都是小提交贡献；核心贡献者 肯定会是大厂公司的人，注重形成公司间团队的合作联盟。
- **2019-10** [任务分发均匀性的模型量化分析](lb-distribution-uniformity-analysis/README.md)  
    - 任务分发在软件系统的很多地方会出现。
    - 任务分发/`LB`的均匀性是一个需要考虑的问题，会导致不必要的过载甚至宕机。
- **2017-03** [`Cache`实践](cache-practice/README.md)
    - 应用开发中，`Cache`毫无疑问是很重要的一块：提升应用性能的关键，降低像`DB`这样关键资源的负荷；
    - 但`Cache`的使用有很多要注意的问题与陷阱。
- **2015-06** 分享PPT [Git/GitLab(Github)使用](git/git-gitlab-usage.pptx)
- **2015-06** 软件文档 [如何写一个`issue`](how-to-write-a-issue.md)
- **2014-12** [Git学习资料](git/study-material.md)
- **2014-09** [Why Git](git/README.md)
- **2014-09** 编程语言 [`Lisp` Practice](lisp-practice/README.md)  
      对于大多数程序员来说，`Lisp`是编程语言中的一个神。

# 🎵 按内容主题分类

<a href="##"><img src="images/miscellany-icon.png" width="15%" align="right" /></a>

> 上一节是 [⬆️ **按内容时间排序** ⬆️](#-%E6%8C%89%E5%86%85%E5%AE%B9%E6%97%B6%E9%97%B4%E6%8E%92%E5%BA%8F)

## 实践讨论

- 软件实践碎碎念
    - [2021年](broken-thoughts/README.md)
    - [2020年](broken-thoughts/2020.md)
- Code Review
    - [`compileflow`开源项目的Code Review](compiler-flow-code-review/README.md)
        - Review与交流讨论的过程 是自己整理学习的过程。大部分的整理内容 其实是独立于具体的一个开源项目。
        - 涉及如 代码实现（文档、可靠性、专业性）、系统设计（领域/模型拆分的原则与实践、扩展设计）、工程实践（版本管理、构建、测试）。

## 如何做开源项目

- 分享PPT [开源漫游者指南：开源的工作内容与要点](hitchhikers-guide-to-open-source/开源漫游者指南-v0.9.1.pptx)
    - 开源是一个充分竞争的环境，不能没有差异化或有明显缺陷，有问题无法隐藏。竞争三要素：1) 成本 2) 差异化 3) 专业化
        - 产品有明确的独特性、差异化（性能/功能） => 拉新/启动
        - 产品界面的部分 重要 => 留存
        - 持续发版/用户(大)Case收集透出（活跃、质量） => 流失 vs. 口碑传播
    - 伸手当是主流；一般用户成为贡献者都是小提交贡献；核心贡献者 肯定会是大厂公司的人，注重形成公司间团队的合作联盟。

## 系统设计与分析

- 分享PPT [软件可靠性设计的实践](practice-of-software-reliability-design/软件可靠性设计的实践-v0.9.2.pptx)
- [平台产品逻辑与执行](product-logic-for-platform-product/README.md)
    - **全接管业务的功能** 是平台的目标，直接体现了平台的核心竞争力。  
      全接管业务的平台功能的多少/比例 可以用来度量 平台的成熟程度。
    - 在平台产品功能中，要区分 哪些是接管的功能，哪些是整合的功能。
    - **不要用美好正义的愿望 来替代 残酷务实的逻辑。**  
      即产品逻辑 推演要包含给出 如何『做成』一个产品（可行性），而不仅是给出 为什么要『要做』一个产品（有需求）。
    - 排除法 对于不确定的规划的事 是不适用的；因为 事情是不是有解/整体组合功能是不是能发展出来 还是未知的。
- [多响应异步请求模式下需求满足的分析模型](multi-response-async-request-pattern-analysis-model/README.md)
    - 请求的3个关注维度`CRC`：**完整性**（`Completeness`）、**响应性**（`Responsiveness`）与**正确性**（`Correctness`）。
    - `CRC`也是请求的平衡维度，所谓平衡是指：当不可兼得时，可互相置换。
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

## 并发

- [并发任务编排的实现与设计 —— 以`Java CompletableFuture`为例](implementation-n-design-of-concurrency-orchestration/)

## `SCM`

- [Why Git](git/README.md)
- [Git学习资料](git/study-material.md)
- 分享PPT
    - [Git/VCS的使用与原则 简介](git/git-usage-and-principle-v0.3.1.pptx)
    - [Git/GitLab(Github)使用](git/git-gitlab-usage.pptx)

## 软件文档

- [如何写一个`issue`](how-to-write-a-issue.md)

## 编程语言

- [`Lisp` Practice](lisp-practice/README.md)  
  对于大多数程序员来说，`Lisp`是编程语言中的一个神。
