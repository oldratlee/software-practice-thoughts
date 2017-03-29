# Java Cache Practice

:point_right: 应用开发中，`Cache`毫无疑问是很重要的一块：提升应用性能的关键，降低像`DB`这样关键资源的负荷。

<img src="cache.png" width="256" align="right" >

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [关于`Cache`的问题/陷阱](#%E5%85%B3%E4%BA%8Ecache%E7%9A%84%E9%97%AE%E9%A2%98%E9%99%B7%E9%98%B1)
- [使用库 vs. 自己实现？](#%E4%BD%BF%E7%94%A8%E5%BA%93-vs-%E8%87%AA%E5%B7%B1%E5%AE%9E%E7%8E%B0)
- [Java Cache Frameworks/Libs](#java-cache-frameworkslibs)
- [Cache Middleware](#cache-middleware)
- [相关资料](#%E7%9B%B8%E5%85%B3%E8%B5%84%E6%96%99)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 关于`Cache`的问题/陷阱

在应用开发通过`Cache`来性能优化时，要注意或了解下面的问题/陷阱：

1. **_多级_** `Cache`支持
    - 应用开发时往往会考虑加上内存`Cache`，因为内存`Cache`性能高很多于`Cache`中间件（如`Memcached`）
        - 当然要特别注意的是 **_内存`Cache`数据条目上限_** 的设置，避免内存消耗过多导致应用瘫痪。
        - 由于内存中`Cache`数据条目，如何决定哪些数据要`Cache`，移出策略的设置变得要好好思考。
        - 如果`Cache`涉及数据条目很多、很分散没有时间局部性，那么内存`Cache`可能是浪费内存且增加了操作性能更低。
    - 这样数据访问路径就成了：内存`Cache` -> 远程`Cache` -> 实际数据（如`DB`）
1. 无实际数据时的 **_防击穿_**  
    导致没有数据时，一直会访问`DB`。  
    （**_自己实现时，容易忽略这点_**）
1. `Cache`中没有数据时，即首次加载时，并发的`Cache`请求的 **_防击穿_**  
    期望在这种情况下，并发请求只会触发一次实际数据请求，数据请求完成后，所有并发`Cache`请求都返回数据。  
    （**_自己实现时，容易忽略这点_**）
1. 使用`Cache`请求时，**_透明_** 数据的加载，即
    - 业务实现不需要自己写这样的逻辑：
        - 如果`Cache`中没有数据读实际数据，设置好`Cache`；
        - 如果`Cache`中有数据返回`Cache`数据。
        - 这样逻辑繁琐易漏易错。
    - `Cache`会持有加载实际数据的`Loader`，参见`Guava`的[`CacheLoader`](https://github.com/google/guava/wiki/CachesExplained)模式。

如果有『击穿』的情况，系统性能压力上来时会雪崩，而你想依赖的之前性能压测的性能数据已经没有意义了。

## 使用库 vs. 自己实现？

总得来说，应该使用`Cache`框架而不应该自己去实现：

1. `Cache`要解决好的问题与业务无关很稳定，所以一定有好的`Cache`框架，并解决好上面这些问题。
1. `Cache`的并发控制/线程安全的问题，对于一般应用开发者来说，可能没有概念，即使是面向自己场景的简单实现也可能漏洞百出。
1. 完整的`Cache`实现以应对不同场景的需求，要考虑很多方面：
    1. 条目的逐出（`Eviction`）/过期策略，如
        - 最简单常用的基于固定数目上限的`LRU`
        - 基于时间的逐出
        - 基于引用，加速内存`GC`
    1. 逐出条目的回调，方便应用可以集成条目的生命周期，如添加监控
    1. `Cache`的命中率，方便了解系统的情况
    1. ……

## Java Cache Frameworks/Libs

- [Java Caching System](https://github.com/apache/commons-jcs) - Apache Commons
    - https://commons.apache.org/proper/commons-jcs/index.html
- [Guava](https://github.com/google/guava) Cache
    - https://github.com/google/guava/wiki/CachesExplained
- [Caffeine](https://github.com/ben-manes/caffeine) is a high performance, near optimal caching library based on Java 8.
- [Ehcache](https://github.com/ehcache/ehcache3)
    - http://www.ehcache.org/
- [J2Cache](https://git.oschina.net/ld/J2Cache)
- 更多参见 [Java开源缓存框架](http://www.open-open.com/13.htm)

## Cache Middleware

- [Redis](https://github.com/antirez/redis)
    - https://redis.io/
- [Memcached](https://github.com/memcached/memcached)
    - https://memcached.org/
- [Tair](https://github.com/alibaba/tair)
    - http://code.taobao.org/p/tair/wiki/intro/
- 更多参见 http://www.oschina.net/project/tag/109/cacheserver

## 相关资料

- [Cache 框架乱炖](https://juejin.im/entry/5741d07c49830c00614a0319)
- [Ehcache详细解读](http://raychase.iteye.com/blog/1545906)
- [Java Cache系列之Cache概述和Simple Cache](https://yq.aliyun.com/articles/46897)
- [5个强大的Java分布式缓存框架推荐](http://www.codeceo.com/article/5-java-distribute-cache.html)
