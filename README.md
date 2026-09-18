<div align="center">

# shuimo

后端 · 物联网 · LLM · MC

[博客](https://shuimo0413.github.io/) · [邮箱](mailto:1743355601@qq.com) · [GitHub](https://github.com/shuimo0413)

<br/>

<img src="https://skillicons.dev/icons?i=java,spring,mysql,redis,docker,linux,nodejs,ts,python,vue,react,git" alt="tech stack" />

</div>

平常写得最多的是 Java / Spring 和 Node。课设、接设备、上班做业务，最后都落到接口、库表、缓存和部署上。模型相关的活也碰：简历解析、检索、小助手这类，不训大模型，主要是把现成的 API 接到真实业务里。前端能写 Vue / React，小程序用过 UniApp。服务器一般是 Debian / Ubuntu，Docker 自己打镜像、自己发。

常用：Spring Boot、MyBatis-Plus、MySQL、Redis、RabbitMQ、Nacos、Gateway；Node 这边 Express、JWT、队列；设备用 MQTT 和 ESP8266 / ESP32；模型用 LangChain / LangGraph、Embedding、OCR。

---


## 项目

| 项目 | 技术栈 | 说明 | 链接 |
| --- | --- | --- | --- |
| FindTA 智能招聘 | Node.js、Express、MySQL、Redis、React、UniApp、DeepSeek、LangGraph、Docker、微信支付、腾讯云 COS | 多租户招聘 SaaS。JWT + 角色权限 + 套餐支付；候选人弹窗里走完初筛到入职；简历 OCR 后结构化；岗找人向量检索只在本租户内粗排再按评分卡打分；小程序分包；4G 云主机上 Docker 发版，前端本机构建后热更新。 | 未开源 |
| 校园 OJ | Spring Boot、MySQL、Redis、MyBatis-Plus、Judge0、LangChain、Docker | 题目 / 提交 / 多测试点判题。Judge0 跑 C、C++、Java、Python，返回时间和内存。`@Async` 排队，页面不卡沙箱。Redis + 布隆过滤器挡乱查，热点加索引。助手按刷题记录推题。Compose 一键拉起。 | [GitHub](https://github.com/shuimo0413/oj-docker-) |
| 词汇网络 | Nest.js、React、MySQL、DeepSeek | 词形 / 前缀 / 语义做成力导向图，可筛选。闪卡 + SM-2，进度在 IndexedDB。DeepSeek 讲用法、编口诀、出例句、小测。词书可换（如四级）。 | [GitHub](https://github.com/shuimo0413/Word-Network) |
| BASpark | C#、WPF、WebView2、Canvas | Windows 点击特效，复刻蔚蓝档案粒子。WPF 做壳，Canvas 在 WebView2 里画。点下去才渲染，停手休眠。进程黑白名单，全屏游戏可自动隐藏。 | [GitHub](https://github.com/shuimo0413/BASpark) |
| MQTT 上位机 / 小车 | Vue、MQTT、Spring Boot、ESP8266 | 网页订主题看遥测、下指令，QoS 可调。Spring Boot 经 MQTT 控 ESP8266 小车。设备到页面是通的。 | [上位机](https://github.com/shuimo0413/-vue-mqtt-) · [小车](https://github.com/shuimo0413/-springboot-mqtt-esp32-) |
| 校园二手 | Spring Boot 3、Vue、MySQL、OSS | 学号认证、发布、搜索、留言、校园卡结算、互评。多模块后端，图放 OSS。 | [GitHub](https://github.com/shuimo0413/shuimo-mall) |
| 缘之空 HD Remake | C++、Kirikiri、SDL2 | AVG 工程，不是从零写引擎。数据在 `data/`。Windows / Android / iOS / 鸿蒙都能编。 | [GitHub](https://github.com/shuimo0413/yosuga-no-sora-remake) |
| WeChatChatReader | Python、OCR | 识别已打开的微信窗口气泡，把字抠出来。自己归档用，不是协议抓包。 | [GitHub](https://github.com/shuimo0413/WeChatChatReader) |
| 法环铁魔法 | Java 21、NeoForge 1.21.1 | Iron's Spells 扩展。辉石弹、彗星头渲染，数值走配置。 | [GitHub](https://github.com/shuimo0413/Iron-Magic-Elden-Ring) |
| Music Agent | FastAPI、LangGraph、Chroma、React | 音乐知识库 RAG，对话框问答。 | 本地项目 |
