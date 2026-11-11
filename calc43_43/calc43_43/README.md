# calc43_43

一个简洁、安全的 Python 命令行四则运算计算器，支持加减乘除、括号与浮点数，带完整的单元测试。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 功能特性

- ➕ 加法 / ➖ 减法 / ✖️ 乘法 / ➗ 除法
- 🔢 支持浮点数与小括号
- 🛡️ 输入过滤，防止恶意代码注入
- ✅ 5 个单元测试全部通过

## 快速开始

要求：Python 3.8 及以上。

```bash
git clone https://github.com/<你的用户名>/calc43_43.git
cd calc43_43
python calculator.py
```

使用示例：

```
欢迎使用 calc43 命令行计算器 (输入 q 退出)
calc43> (3+4)*2
= 14.0
calc43> 10/0
错误: 除数不能为 0
calc43> q
再见！
```

## 运行测试

```bash
python tests.py
```

## 项目结构

```
calc43_43/
├── calculator.py   # 主程序
├── tests.py        # 单元测试
├── LICENSE         # MIT 许可证
├── CONTRIBUTING.md # 贡献指南
├── CHANGELOG.md    # 更新日志
└── docs/
    └── strategy-analysis.md  # "五看三定" 战略分析
```

## 分支模型

本项目采用 **GitHub Flow** 分支模型：

- `main`：始终可发布的稳定分支
- `feature-xxx`：功能开发分支，通过 Pull Request 合并回 `main`

## 许可证

本项目采用 [MIT License](LICENSE)，可自由使用、修改与分发，只需保留版权声明。

## 贡献

欢迎提交 Issue 与 Pull Request，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
