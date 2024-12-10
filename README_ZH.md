# Awesome Heurist 🚀

[English](README.md)

这是一个展示如何使用 Heurist API 的示例项目,包含了图像生成和 LLM 对话功能的演示代码。一个 API key 使用各种图文模型。支持数十个主流文生文和文生图模型。完整文档: [Heurist Dev Doc](https://docs.heurist.ai/dev-guide/integration-overview)。
官方 TG: [Heurist Ecosystem Builder](https://t.me/heuristsupport)

## 功能特性 ✨

- 图像生成 (使用 Stable Diffusion 模型) 🖼️
- LLM 对话 (使用 dolphin-2.9-llama3-8b 模型) 💬
- 支持 Python 和 JavaScript/Node.js 两种实现 🐍/🟦

## 开始使用 🚀

### 前置要求 📋

- Python 3.6+ 或 Node.js 12+ 🖥️
- Heurist API 密钥 🔑

### 安装 📦

1. 克隆仓库:

```bash
git clone git@github.com:flashclub/awesome-heurist.git
cd awesome-heurist
```

2. 安装依赖:

对于 Python:

```bash
pip install -r requirements.txt
```

对于 Node.js:

```bash
npm install
```

3. 配置环境变量:

创建一个.env 文件并添加你的 API 密钥:

```bash
HEURIST_API_KEY=your_api_key_here
```

## 使用示例 🎮

### 图像生成 🖼️

使用 Python:

```bash
python image.py
```

使用 Node.js:

```bash
node image.js
# 或使用SDK版本
node image-with-sdk.js
```

### LLM 对话 💬

使用 Python:

```bash
python llm.py
```

使用 Node.js:

```bash
node llm.js
```

## API 示例说明 📚

### 图像生成 🖼️

项目提供了两种方式生成图像:

1. 直接调用 API (image.py/image.js)
2. 使用 Heurist SDK (image-with-sdk.js)

### LLM 对话 💬

支持与 LLM 模型进行简单对话,默认使用 `dolphin-2.9-llama3-8b` 模型。

## 注意事项 ⚠️

- 请确保妥善保管你的 API 密钥 🔒
- API 调用可能会产生费用,请参考 Heurist 的定价政策 💰
- 建议在正式环境中增加错误处理和重试机制 🔄
- 申请 API key(2,000–10,000 免费积分)：[request form](https://dev-api-form.heurist.ai/)

## 许可证 📜

ISC
