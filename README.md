# Awesome Heurist 🚀

[中文文档](README_ZH.md)

This is a sample project demonstrating how to use the Heurist API, featuring demo code for image generation and LLM conversation capabilities. One API key for various text and image models. Supports dozens of mainstream text-to-text and text-to-image models. Full documentation: [Heurist Dev Doc](https://docs.heurist.ai/dev-guide/integration-overview).
Official TG: [Heurist Ecosystem Builder](https://t.me/heuristsupport)

## Features ✨

- Image Generation (using FLUX.1-dev model) 🖼️
- LLM Conversation (using meta-llama/llama-3.3-70b-instruct model) 💬
- Supports both Python and JavaScript/Node.js implementations 🐍/🟦

## Getting Started 🚀

### Prerequisites 📋

- Python 3.6+ or Node.js 12+
- Heurist API key

### Installation

1. Clone the repository:

```bash
git clone git@github.com:flashclub/awesome-heurist.git
cd awesome-heurist
```

2. Install dependencies:

For Python:

```bash
pip install -r requirements.txt
```

For Node.js:

```bash
npm install
```

3. Configure environment variables:

Create a .env file and add your API key:

```bash
HEURIST_API_KEY=your_api_key_here
```

## Usage Examples

### Image Generation

Using Python:

```bash
python image.py
```

Using Node.js:

```bash
node image.js
# or use the SDK version
node image-with-sdk.js
```

### LLM Conversation

Using Python:

```bash
python llm.py
```

Using Node.js:

```bash
node llm.js
```

## API Examples Explained

### Image Generation

The project provides two ways to generate images:

1. Direct API calls (image.py/image.js)
2. Using Heurist SDK (image-with-sdk.js)

### LLM Conversation

Supports simple conversations with LLM models, using `meta-llama/llama-3.3-70b-instruct` model by default.

## Common issue:

- got error "Invalid auth_key format": add double quotes in .env file
  like this API_KEY="abc#123", some systems might recognize # as a code comment and ignore it

## Important Notes ⚠️

- Keep your API key secure 🔒
- API calls may incur charges, please refer to Heurist's pricing policy 💰
- Consider adding error handling and retry mechanisms in production environments 🔄
- Request API key (2,000–10,000 free credits): [request form](https://dev-api-form.heurist.ai/), invite code: ai16z

## License 📜

ISC
