# Java Cache Practice

应用开发中，`Cache`毫无疑问是很重要的一块：提升应用性能的关键，避免像`DB`这样关键资源的负荷。

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [问题/陷阱](#%E9%97%AE%E9%A2%98%E9%99%B7%E9%98%B1)
- [使用库 vs. 自己实现？](#%E4%BD%BF%E7%94%A8%E5%BA%93-vs-%E8%87%AA%E5%B7%B1%E5%AE%9E%E7%8E%B0)
- [Java Cache Frameworks/Libs](#java-cache-frameworkslibs)
- [Cache Middleware](#cache-middleware)
- [相关资料](#%E7%9B%B8%E5%85%B3%E8%B5%84%E6%96%99)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 问题/陷阱

:point_right: 在应用开发通过`Cache`来性能优化时，要注意或了解下面的问题/陷阱：

1. 多级`Cache`支持
    - 往往应用开发时会考虑加上内存`Cache`，因为内存高于`Cache`中间件（如`Memcached`）
    - 这样数据访问路径就成了：内存`Cache` -> Cache远程`Cache` -> 实际数据（如`DB`）
1. 无实际数据时的防击穿  
    导致没有数据时，一直会访问`DB`。  
    （自己实现时，常常容易忽略这点）
1. `Cache`中没有数据时，即首次加载时，并发的`Cache`请求的防击穿  
    期望在这种情况下，并发请求只会触发一次实际数据请求，数据请求完成后，所有并发`Cache`请求都返回数据。
    （自己实现时，常常容易忽略这点）
1. 使用`Cache`请求时，透明数据的加载，即
    - 业务逻辑不需要自己写这样的逻辑：
        - 如果`Cache`中没有数据读实际数据，设置好`Cache`；
        - 如果`Cache`中有数据返回`Cache`数据。
        - 这样逻辑繁琐易漏易错。
    - `Cache`会持有加载实际数据的`Loader`，参见`Guava`的[`CacheLoader`](https://github.com/google/guava/wiki/CachesExplained)模式。

如果有『击穿』的情况，往往系统性能雪崩，之前性能压测的性能数据就没有意义了。

## 使用库 vs. 自己实现？

总得来说，`Cache`要解决好的问题与业务无关很稳定，所以一定有好的`Cache`框架，并解决好上面这些问题，而不应该自己去实现。

## Java Cache Frameworks/Libs

- Java Caching System - Apache Commons
    - https://commons.apache.org/proper/commons-jcs/index.html
    - https://github.com/apache/commons-jcs
- Guava Cache
    - https://github.com/google/guava/wiki/CachesExplained
- Caffeine is a high performance, near optimal caching library based on Java 8.
    - https://github.com/ben-manes/caffeine
- Ehcache
    - http://www.ehcache.org/
    - https://github.com/ehcache/ehcache3
- J2Cache
    - https://git.oschina.net/ld/J2Cache
- 更多参见 [Java开源缓存框架](http://www.open-open.com/13.htm)

## Cache Middleware

- Redis
    - https://redis.io/
    - https://github.com/antirez/redis
- Memcached
    - https://memcached.org/
    - https://github.com/memcached/memcached
- Tair
    - http://code.taobao.org/p/tair/wiki/intro/
    - https://github.com/alibaba/tair
- 更多参见 http://www.oschina.net/project/tag/109/cacheserver

## 相关资料

- [Cache 框架乱炖](https://juejin.im/entry/5741d07c49830c00614a0319)
- [Ehcache详细解读](http://raychase.iteye.com/blog/1545906)
- [Java Cache系列之Cache概述和Simple Cache](https://yq.aliyun.com/articles/46897)
- [5个强大的Java分布式缓存框架推荐](http://www.codeceo.com/article/5-java-distribute-cache.html)
