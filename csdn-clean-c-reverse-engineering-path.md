# Android 逆向学习路线：从抓包到 Frida Hook

这是一条真实的 Android 逆向学习路径，从零基础到能独立分析大麦/猫眼等 App 的接口逻辑。

## 第一阶段：基础（1-2 周）

**目标**：能抓包看到 App 的网络请求。

- **HTTP 抓包**：Charles / mitmproxy 配置 SSL 证书
- **Android 证书验证绕过**：大多数 App 会做 SSL Pinning，需要绕过
- **抓包工具进阶**：Wireshark 做深度协议分析

常见坑：Android 7+ 默认不信任用户证书 → 需要 Root + 将证书移到系统目录。

## 第二阶段：逆向入门（2-4 周）

**目标**：能反编译 APK、读懂关键代码。

- **APK 反编译**：Apktool 解包 → jadx 看 Java 源码
- **脱壳**：大部分商业 App 有加固（360、腾讯乐固）→ Frida 脱壳脚本
- **反编译工具对比**：GDA（轻量快速）vs jadx（反编译质量高）vs IDA Pro（Native 层）

## 第三阶段：Frida Hook（4-8 周）

**目标**：能 Hook App 的关键函数，动态修改行为。

- **Frida 基础**：attach/spawn 模式，Hook Java 方法
- **Frida 反检测**：大麦等 App 会检测 Frida → 需要绕过（改端口、改进程名）
- **Frida Gadget**：注入模式，无需 Root
- **实战**：Hook 大麦的座位查询、支付签名等关键函数

## 第四阶段：风控对抗（持续）

**目标**：App 检测不到你的逆向环境。

- **Root 隐藏**：Magisk + Shamiko + Hide My Applist
- **SafetyNet/Play Integrity** 绕过
- **设备指纹** 伪装
- **KernelSU** 替代 Magisk（更底层，更难检测）

---

这 4 个阶段对应我们整理的 20 篇教程（Android 逆向 8 篇 + JS 逆向 2 篇 + Python 6 篇 + 工具 4 篇），每篇都是 `.ipynb` 格式，可以直接在线预览或在本地 Jupyter 运行。

📂 20 篇教程合集：https://github.com/damaiqiangpiao/damai

🌐 大麦抢票技术社区 FAQ：https://damai.daydayup365.top/damai-faq.html

*技术探讨，仅供参考。*
