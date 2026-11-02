<p align="center">
  <h1 align="center">🧭 ABFRL OC Orchestrator</h1>
  <p align="center">
    <strong>FastAPI gateway that turns one <code>/genie</code> call into catalog text-search and product-detail lookups for a fashion-retail assistant.</strong>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-orchestrator-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/Docker-ready-2496ed?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/github/last-commit/pratiks360/abfrl-oc-orchestrator?style=for-the-badge&label=Last+Commit" alt="Last Commit">
  </p>
</p>

---

## ✨ What Is This?

A single-endpoint orchestrator used by a conversational shopping assistant. The caller sends an `operation` and its `params`; the service fans out to the catalog's natural-language search API, then enriches every hit with its product record.

## 🔌 Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/genie` | Body `{"operation": "text_search", "params": {"query_text": "..."}}` |

Missing `operation` or `params` returns a plain-text prompt asking for them.

## 🧩 How It Works

```
┌──────────┐  /genie   ┌──────────────┐  text_search  ┌──────────────┐
│ Assistant│ ────────► │ orchestrator │ ────────────► │ Catalog NLS  │
│          │ ◄──────── │   (FastAPI)  │ ◄──────────── │     API      │
└──────────┘  products └──────┬───────┘   product ids └──────────────┘
                             │ per id
                             ▼
                       Product detail API → name, image, price
```

## 🚀 Quick Start

```bash
git clone https://github.com/pratiks360/abfrl-oc-orchestrator.git
cd abfrl-oc-orchestrator
pip install fastapi uvicorn requests
python app/main.py        # serves on http://127.0.0.1:8080
```

Or build the included `Dockerfile`.

## 🔒 Security Notes

- The catalog API key is read from the `CATALOG_API_KEY` environment variable.
- A previously committed key was purged from history — rotate it if it was ever real.

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Web** | FastAPI + Uvicorn |
| **HTTP client** | requests |
| **Packaging** | Dockerfile |

---

<p align="center">
  <sub>Built with ❤️ for retail AI experiments.</sub>
</p>
