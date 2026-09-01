<div align="center">

# shuimo

河北工程技术学院 · 人工智能

后端 · 物联网 · LLM

[博客](https://shuimo0413.github.io/) · [邮箱](mailto:1743355601@qq.com) · [GitHub](https://github.com/shuimo0413)

<br/>

<img src="https://skillicons.dev/icons?i=java,spring,mysql,redis,docker,linux,nodejs,ts,python,vue,react,git" alt="stack" />

</div>

平常写得最多的是 Java / Spring 和 Node。课设、接设备、上班做业务，最后都落到接口、库表、缓存和部署上。模型相关的活也碰：简历解析、检索、小助手这类，不训大模型，主要是把现成的 API 接到真实业务里。前端能写 Vue / React，小程序用过 UniApp。服务器一般是 Debian / Ubuntu，Docker 自己打镜像、自己发。

常用的大概是这些：Spring Boot、MyBatis-Plus、MySQL、Redis、RabbitMQ、Nacos、Gateway；Node 这边 Express、JWT、队列；设备用 MQTT 和 ESP8266 / ESP32；模型用 LangChain / LangGraph、Embedding、OCR。Git 和 Linux 是日常。

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

<div align="center">

### 仓库

<table>
  <tr>
    <td>
      <a href="https://github.com/shuimo0413/oj-docker-">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=shuimo0413&repo=oj-docker-&theme=github_dark&hide_border=true" alt="oj" />
      </a>
    </td>
    <td>
      <a href="https://github.com/shuimo0413/Word-Network">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=shuimo0413&repo=Word-Network&theme=github_dark&hide_border=true" alt="word-network" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/shuimo0413/BASpark">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=shuimo0413&repo=BASpark&theme=github_dark&hide_border=true" alt="baspark" />
      </a>
    </td>
    <td>
      <a href="https://github.com/shuimo0413/yosuga-no-sora-remake">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=shuimo0413&repo=yosuga-no-sora-remake&theme=github_dark&hide_border=true" alt="yosuga" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/shuimo0413/WeChatChatReader">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=shuimo0413&repo=WeChatChatReader&theme=github_dark&hide_border=true" alt="wechat" />
      </a>
    </td>
    <td>
      <a href="https://github.com/shuimo0413/Iron-Magic-Elden-Ring">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=shuimo0413&repo=Iron-Magic-Elden-Ring&theme=github_dark&hide_border=true" alt="elden-ring" />
      </a>
    </td>
  </tr>
</table>

</div>

**[OJ](https://github.com/shuimo0413/oj-docker-)** 是校园判题站。Spring Boot 管题目、提交、用户；真正跑代码交给 Judge0，C / C++ / Java / Python 都能测，多测试点，返回时间和内存。判题走 `@Async`，提交先落库再排队，页面不用卡着等沙箱。题目和排行榜这类热点放 Redis，布隆过滤器挡一下乱查的 id。高频条件在 MySQL 上建了索引。里面有个 LangChain 助手，能看你做过的题，按标签和通过情况推下一题。整套用 Docker Compose 拉起来。

**[词汇网络](https://github.com/shuimo0413/Word-Network)** 是背单词用的。前端 React，后端 Nest.js，词和词之间的形近、前缀、语义做成图，页面上用力导向铺开，可以按关系筛。背词是闪卡，进度按 SM-2 写在 IndexedDB 里，换电脑不会自动跟着走。旁边接了 DeepSeek，可以讲用法、编口诀、出例句、小测一下。词书可以换，比如四级。

**[BASpark](https://github.com/shuimo0413/BASpark)** 是 Windows 上的点击特效，对着《蔚蓝档案》界面那种粒子做的。壳子是 WPF，画面在 WebView2 里用 Canvas 画。鼠标点下去才起渲染，停手就休眠，尽量不占后台。可以配进程黑白名单，全屏游戏或某几个软件里自动把特效藏掉，免得打游戏还飘粒子。

**[缘之空 HD Remake](https://github.com/shuimo0413/yosuga-no-sora-remake)** 是 AVG 工程，不是从零写引擎。运行时是 Kirikiri + SDL2，游戏数据在 `data/`。Windows 能编，Android / iOS / 鸿蒙也有工程。主要是引擎适配、资源组织和跨端编译，体积不小。

**[WeChatChatReader](https://github.com/shuimo0413/WeChatChatReader)** 用来读已经打开的微信窗口：找到聊天气泡，OCR 把字抠出来。自己归档、检索聊天记录用，不是协议层抓包。

**[法环铁魔法](https://github.com/shuimo0413/Iron-Magic-Elden-Ring)** 是 Minecraft 1.21.1 NeoForge 模组，挂在 Iron's Spells 上加法环风格的咒。辉石弹、彗星头渲染、法术数值走配置。Java 21，自己的 Gradle。

物联网那条线是 [Vue 上位机](https://github.com/shuimo0413/-vue-mqtt-) 加 [Spring Boot 控 ESP8266 小车](https://github.com/shuimo0413/-springboot-mqtt-esp32-)。车和传感器走 MQTT 上报，网页订主题看实时数据、下指令，QoS 能调。从单片机到页面是通的。

[校园二手](https://github.com/shuimo0413/shuimo-mall) 是 Spring Boot 3 多模块：学号认证、发布、搜索、留言、校园卡结算、互评。图放 OSS。另外自己做过一个音乐知识库 RAG，FastAPI + LangGraph + Chroma，前端是 React 对话框。

---

<div align="center">

<table>
  <tr>
    <td>
      <img src="https://github-readme-stats.vercel.app/api?username=shuimo0413&show_icons=true&theme=github_dark&hide_border=true" alt="stats" />
    </td>
    <td>
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=shuimo0413&layout=compact&theme=github_dark&hide_border=true&langs_count=8" alt="langs" />
    </td>
  </tr>
</table>

<img src="https://komarev.com/ghpvc/?username=shuimo0413&style=flat-square&color=8b8b8b&label=views" alt="views" />

</div>
