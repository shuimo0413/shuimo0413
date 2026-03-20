# 👋 Hi, I am shuimo


专注于**Java 后端开发**，兼顾**物联网开发**与**大语言模型应用开发**，具备微服务、分布式系统、容器化部署实战经验，擅长从 0 到 1 搭建后端服务与物联网通信体系。

## 📌 技术方向

- Java 后端开发（微服务 / 分布式 / 高并发）

- 物联网开发（设备通信 / 协议对接）

- 大语言模型应用开发（RAG / 智能体）

## 🔧 技术栈

### 后端核心

Java、Spring Cloud、Spring Boot、Spring MVC、MyBatis、MyBatis\-Plus、Seata、Sentinel

### 数据存储

MySQL、Redis（分布式锁 / 缓存优化）、Elasticsearch

### 中间件 \&amp; 消息队列

RabbitMQ、Judge0

### 物联网

MQTT 协议、ESP32/ESP8266、设备通信、订阅 / 发布模式、QoS 服务质量等级

### 前端基础

Vue、JavaScript、HTML/CSS

### 容器化 \&amp; 运维

Linux（CentOS/Ubuntu/Debian）、Docker、Docker Compose、SSH 远程管理

### 版本控制 \&amp; 工具

Git、PostMan

### AI 开发

Langchain、Spring AI、RAG 检索增强生成、MCP 工具调用、大语言模型智能体开发

## 🚀 项目实战

|项目名称|技术栈|项目描述|项目地址|
|---|---|---|---|
|AI 智能校园 OJ 平台|SpringBoot、MySQL、Redis、FastAPI、Langchain、Mybatis\-Plus、Judge0、Docker|1\. 实现题目管理、多语言代码提交、多测试点判题、提交记录统计等核心 OJ 功能，支持 Java/Python 等多语言评测<br>2\. 基于 Langchain 开发 AI 智能体，支持多轮对话，可根据用户刷题历史分析水平并智能推荐适配题目<br>3\. 集成 Judge0 专业判题服务，精准返回代码运行时间、内存消耗及错误信息<br>4\. 采用 Spring @Async 实现异步判题，结合 Redis\+MySQL 分层架构，通过布隆过滤器、缓存预热解决缓存穿透 / 击穿 / 雪崩问题<br>5\. 针对高频查询创建 MySQL 索引优化 SQL 性能，实现用户认证、权限控制及完善的错误处理机制<br>6\. 基于 Docker\&amp;Docker Compose 实现项目一键式容器化部署|[GitHub](https://github.com/shuimo0413/oj-docker-)|
|微服务全栈电商平台|SpringBoot、SpringCloud Alibaba、MyBatis\-Plus、MySQL、Redis、Elasticsearch、RabbitMQ、Seata、Gateway、Nacos、Docker|1\. 采用 SpringCloud Alibaba 微服务架构，拆分商品 / 订单 / 用户 / 搜索 / 支付等独立服务，实现服务解耦<br>2\. 基于 Nacos 完成服务注册发现与统一配置管理，Gateway 网关实现路由转发、权限校验与请求过滤<br>3\. 利用 Redis 构建分布式缓存，结合缓存预热、布隆过滤器优化缓存策略，提升接口响应速度<br>4\. 集成 Elasticsearch 实现商品全文检索，支持分词查询、结果高亮、多维度筛选与排序<br>5\. 基于 RabbitMQ 实现异步通信，完成订单创建、支付回调、库存扣减的解耦与流量削峰<br>6\. 引入 Seata 处理分布式事务，保障订单 \- 库存 \- 支付链路的数据最终一致性<br>7\. 采用 Docker 完成服务容器化，实现微服务集群的快速部署与运维|开发中|
|Vue\+MQTT 上位机前端|Vue、MQTT、JavaScript、HTML/CSS|基于 Vue 开发的物联网上位机前端项目，适配 MQTT 订阅 / 发布模式，实现物联网设备的实时通信、数据可视化展示与设备状态监控，支持 QoS 服务质量等级配置，保障设备数据传输的可靠性|开发中|

## 📫 联系我

- 邮箱：[1743355601@qq\.com](mailto:1743355601@qq.com)

- 电话：15032976581

- GitHub：[shuimo0413](https://github.com/shuimo0413)

- 个人博客：[shuimo0413\.github\.io](https://shuimo0413.github.io/)

## 💪 个人能力

1. 精通 Java 基础及并发编程，熟悉 synchronized/volatile 等关键字，掌握线程池、ConcurrentHashMap 使用，了解 JVM 内存模型、垃圾回收与类加载机制

2. 深入理解 MySQL 底层原理，精通事务、索引、MVCC、存储引擎等核心知识点，具备数据库性能优化实战经验

3. 熟练使用 Spring 生态框架，理解 IOC/AOP/ 自动配置 / 循环依赖等核心原理，具备微服务架构设计与开发能力

4. 熟悉 Linux 系统操作与远程管理，能独立完成环境部署、容器化构建与项目运维工作

5. 掌握 Git 多人协作开发流程，能熟练完成代码提交、分支管理、合并与简单回滚操作

6. 具备物联网 MQTT 协议实战经验，熟悉设备通信与上位机开发，能完成物联网系统的前后端对接

7. 掌握大语言模型应用开发技巧，能基于 Langchain/Spring AI 开发 RAG、智能体等 AI 应用
