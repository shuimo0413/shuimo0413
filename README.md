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

## FindTA

现在主要时间在 **FindTA** 上。这是给消费金融 / 风控猎头用的招聘系统，多租户 SaaS，已经在腾讯云跑着。仓库不公开。B 端是招聘工作台，C 端有网页和小程序，上面还有一层平台运营：租户、套餐、订单、渠道。

租户之间数据是切开的，登录带 JWT，权限按角色配，品牌、域名入口也可以按租户改。套餐限制次数和功能，付费走微信扫码，付完回调改订单状态。渠道会发邀请码和小程序码，用来看人是从哪进来的。

招聘作业收在候选人那个大弹窗里。列表筛完人，点进去就是初筛、约面试、写评价、发 Offer、走审批、办入职，时间线跟在后面。岗位页左边是机构树，岗位上挂评分卡，后面配岗打分和「岗找人」都用这套维度。驾驶舱是进系统后的首页，待办和图表，点一下能跳到某个人的某一环。

简历 PDF、Word、图片都能传。图片先走 OCR 抽出字，再和文本一起丢给模型做结构化：学校、经历、技能这类拆开存。打开人还能做智能速读，对照某个岗位按评分卡几维打星，再加权合成总分。文件在腾讯云 COS 上。Word 预览是 LibreOffice 转成 PDF 再打开。批量导入、邮箱收取、扫码填表也有，扫码填的要等模型跑完才进可推荐池。

岗找人是单独的检索服务。人进人才库、改简历、解析完成，会异步写向量，文本没变就跳过。检索只在本租户里做：先 embedding 余弦粗排多捞一点，再按当前岗位评分卡加权截断。已入职、中止、还在分析中的人不会推出来。结果写成快照，下次进页面先看上次的名单，不会每次都烧一遍模型。业务后端负责鉴权和租户号，检索服务不直接暴露给前端。

微信那边是 UniApp 小程序，登录、看板、候选人、岗位、套餐拆在分包里。服务号会发通知。统计按北京时间切天，区间用 `[start, end)`，驾驶舱和报表用同一套，免得对账差一天。解析、建索引这种慢活进 Redis 队列，接口先返回。

部署是 Docker。云主机大概 4G 内存，不能在上面跑 Vite，前端在自己电脑 build 完再热更新容器。发版前预检配置和环境，发完打健康检查，避免只更了前端、后端逻辑其实没上去。

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
