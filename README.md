# 🔥 Daily Hot News - 每日热点资讯聚合器

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/wow-233/daily-hot-mcp?style=social)](https://github.com/wow-233/daily-hot-mcp)
[![Forks](https://img.shields.io/github/forks/wow-233/daily-hot-mcp?style=social)](https://github.com/wow-233/daily-hot-mcp)

> 自动化抓取 GitHub Trending、Hacker News、ProductHunt 等热门资讯，生成中文 Markdown 文件，配合 Obsidian 阅读。

## ✨ 功能

- 🔥 **GitHub Trending** - 抓取热门开源项目，自动分析项目特性、核心价值和适用场景
- 📰 **Hacker News** - 技术新闻聚合，自动生成中文摘要
- 🚀 **ProductHunt** - 产品发现列表
- 🇨🇳 **中国热门** - 36氪、知乎、微博热点（需要网络代理）

## 📁 项目结构

```
daily-hot-mcp/
├── main.py                 # 主入口
├── config.py               # 配置管理
├── pyproject.toml          # 项目元数据
├── README.md               # 项目说明
├── LICENSE                 # MIT 许可证
├── .env.example            # 配置模板
├── .gitignore
└── scraper/
    ├── __init__.py
    ├── github_scraper.py       # GitHub Trending 抓取
    ├── hackernews_scraper.py   # Hacker News 抓取
    ├── producthunt_scraper.py  # ProductHunt 抓取
    ├── chinese_hotnews.py      # 中国热门抓取
    ├── translator.py           # AI 翻译接口
    └── markdown_generator.py    # Markdown 生成
```

## 🚀 快速开始

### 1. 安装依赖

```bash
uv sync
# 或
pip install -r requirements.txt
```

### 2. 配置

```bash
cp .env.example .env
```

编辑 `.env`：

```env
API_KEY=你的API密钥
BASE_URL=https://api.deepseek.com
MODEL=deepseek-chat
```

**支持的 API 提供商：**

| 提供商 | URL | 模型示例 |
|--------|-----|----------|
| DeepSeek | `https://api.deepseek.com` | `deepseek-chat` |
| OpenAI | `https://api.openai.com/v1` | `gpt-3.5-turbo` |
| 硅基流动 | `https://api.siliconflow.cn/v1` | `Qwen/Qwen2.5-7B-Instruct` |
| OpenRouter | `https://openrouter.ai/api/v1` | `google/gemini-pro` |
| Ollama (本地) | `http://localhost:11434/v1` | `llama3` |

### 3. 运行

```bash
uv run python main.py
```

输出文件默认生成在 `output/` 目录。

## ⚙️ 配置说明

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `API_KEY` | OpenAI 兼容 API 的密钥 | - |
| `BASE_URL` | API 端点地址 | `https://api.deepseek.com` |
| `MODEL` | 使用的模型名称 | `deepseek-chat` |
| `PROXY` | 代理地址（如需访问外网） | 空 |
| `VERIFY_SSL` | 是否验证 SSL 证书 | `false` |

## 🛠️ 技术栈

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" alt="Python" title="Python">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postman/postman-original.svg" width="40" height="40" alt="Requests" title="Requests">
</p>

- **Python 3.10+** - 主要编程语言
- **requests + BeautifulSoup** - 网络爬虫
- **OpenAI 兼容 API** - AI 翻译/分析
- **Obsidian** - 本地阅读

## 📝 注意事项

- GitHub 页面结构可能变化，如抓取失败请提交 Issue
- 中国热门功能需要网络代理支持
- 建议设置合理的 API 调用频率，避免触发限流

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！
