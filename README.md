# <img src="docs/assets/logo.png" width="40" height="40" alt="ArkhamMirror Logo" style="vertical-align: middle;"> ArkhamMirror

![ArkhamMirror Banner](docs/assets/banner.png)

> **Connect the dots without connecting to the cloud.**

ArkhamMirror is an air-gapped, AI-powered investigation platform for journalists and researchers. It runs 100% locally on your machine, turning chaos into order using advanced NLP, Vision AI, and Knowledge Graphs.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Sponsor](https://img.shields.io/badge/Sponsor-Ko--fi-red)](https://ko-fi.com/arkhammirror)

---

## ⚡ Key Features at a Glance

| Feature | Description |
| :--- | :--- |
| **🕵️ Local AI** | Chat with your data using **Offline RAG** (Retrieval-Augmented Generation). |
| **🔍 Semantic Search** | Find documents by *concept*, not just exact keywords. |
| **🕸️ Knowledge Graph** | Visualize hidden connections between People, Orgs, and Places. |
| **⏳ Auto-Timeline** | Extract dates and events to reconstruct what happened when. |
| **📊 Visual Table Extraction** | Recover complex financial tables from PDFs/Images using Vision models. |
| **⚠️ Contradiction Detection** | Automatically flag conflicting statements across documents. |
| **🔒 Absolute Privacy** | Zero cloud dependencies. Your data never leaves your specialized "Data Silo". |

---

## Try ACH Online - No Installation Required

**[Launch the ACH Tool](https://mantisfury.github.io/ArkhamMirror/ach/)** - A standalone Analysis of Competing Hypotheses tool that runs entirely in your browser.

- Based on Richard Heuer's CIA methodology for evaluating competing explanations
- All data stays in your browser's localStorage - nothing is sent to any server
- Optional AI assistance via your own API keys (OpenAI, Groq, Anthropic, or local LLMs)
- Export analyses as JSON, Markdown, or PDF reports

Perfect for quick analyses without setting up the full ArkhamMirror platform.

---

## 🚀 Getting Started

ArkhamMirror includes a **Smart Installer** that sets up Python, Docker, and Database dependencies for you.

### Windows (One-Click)

Double-click `setup.bat` and follow the **AI Setup Wizard**.

### Mac / Linux

```bash
chmod +x setup.sh
./setup.sh
```

---

## 📚 Documentation

Detailed guides for features and workflows:

* **[User Guide](docs/USER_GUIDE.md)**: Full walkthrough of features and setup.
* **[Network & Privacy](docs/NETWORK.md)**: What gets downloaded, telemetry options, and air-gapped operation.
* **[ACH Analysis Guide](docs/ACH_GUIDE.md)**: Analysis of Competing Hypotheses methodology.

---

## 🖼️ Gallery

![Dashboard](docs/assets/images/dashboard.png)

### Advanced Analysis

| Narrative Reconstruction | Gap Finding | Contradiction Chain |
| :---: | :---: | :---: |
| ![Motive](docs/assets/images/motive.png) | ![Gaps](docs/assets/images/gaps.png) | ![Web of Lies](docs/assets/images/weboflies.png) |

### Forensics

| Entity Graph | Author Unmasking |
| :---: | :---: |
| ![Graph](docs/assets/images/graph.png) | ![Author Unmask](docs/assets/images/authorunmask.png) |

---

## 💖 Support the Project

This tool was born from a desire to give journalists powerful forensics without the monthly subscription costs or privacy risks of cloud platforms.

If it helps you uncover the truth, consider buying me a coffee!

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/arkhammirror)
