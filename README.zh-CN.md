# Project Plan · 项目依赖计划

[English](README.md) | 简体中文

先看哪些任务能开始、哪条依赖链决定整体结束时间。输入任务、工时、前置条件和验收标准，得到有序计划与关键路径。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-project-plan/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考](docs/input.zh-CN.md) · [反馈问题](https://github.com/KarmenLoop/skill-project-plan/issues)

## 能做什么

三个依赖任务分别在偏移 1、4、6 完成，关键路径为 a → b → c，estimated_duration 为 6。

工时单位由你统一约定；工具不处理人员排班、资源优化，也不承诺实际交付日期。

![项目依赖计划 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-project-plan-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-project-plan 0.2.1`。三个依赖任务分别在偏移 1、4、6 完成，关键路径为 a → b → c，estimated_duration 为 6。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

每项任务填写唯一 ID、正数 duration、depends_on 和可检查的 acceptance；所有工时单位一致，owner 可选。

增加并行工作，比较其结束时间与关键路径；再尝试缺失依赖和循环依赖，理解无效计划为何会在排程前被拒绝。

准备新输入前可查看[字段约定](docs/input.zh-CN.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**关键路径会考虑周末和人员空闲吗？** 不会。它只使用工时和依赖关系，真实日历与人员安排需要另外处理。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/input.zh-CN.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。
