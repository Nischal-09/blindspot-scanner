<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Vite-8-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

# 🛡️ BlindSpot — OWASP Vulnerability Scanner

**BlindSpot** is a full-stack web vulnerability scanning platform that detects OWASP Top 10 risks, outdated components, and security misconfigurations. It combines passive reconnaissance with active security probing, CVE enrichment, and AI-powered professional security report generation.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔍 **Passive Scanning** | HTTP header analysis, cookie flags, software fingerprinting, SSL/TLS validation |
| ⚡ **Active Scanning** | XSS probe injection, SQL injection detection (including blind SQLi), path traversal |
| 🧬 **Technology Detection** | Wappalyzer-based fingerprinting of frontend/backend frameworks, CMS, libraries |
| 📊 **Risk Scoring** | CVSS-aligned severity grading (A+ to F) with OWASP Top 10 coverage mapping |
| 🔗 **CVE Enrichment** | Real-time lookup against OSV & NVD databases for known vulnerabilities |
| 🤖 **AI Security Reports** | Professional PDF/HTML reports generated via Gemini AI with remediation guidance |
| 🔐 **Authentication** | Supabase JWT-based authentication with role-based access control |
| 🧩 **Chrome Extension** | Browser extension for one-click scanning of the current tab |
| 📥 **Nuclei Integration** | 13,000+ Nuclei community templates for comprehensive vulnerability coverage |
| 💾 **Elasticsearch** | Optional persistent storage with time-series indexing (works in memory-only mode too) |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Chrome Extension                            │
│                  (Manifest V3 · popup.js)                       │
└──────────────────────┬──────────────────────────────────────────┘
                       │ REST API
┌──────────────────────▼──────────────────────────────────────────┐
│                   React Frontend (Vite)                         │
│           Dashboard · Scan Results · Reports                    │
│                Supabase Auth · Real-time UI                     │
└──────────────────────┬──────────────────────────────────────────┘
                       │ API Calls
┌──────────────────────▼──────────────────────────────────────────┐
│                FastAPI Backend (Uvicorn)                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │  Scanner  │  │  Engine  │  │    AI    │  │  Enrichment  │   │
│  │ passive   │  │  risk    │  │ Gemini   │  │  CVE/OSV/NVD │   │
│  │ active    │  │  scoring │  │ reports  │  │  lookup      │   │
│  │ rules     │  │  OWASP   │  │ PDF gen  │  │  caching     │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │ Storage  │  │ Importers│  │  Export  │                      │
│  │ ES/JSON  │  │ Wappalyz │  │ JSON/PDF │                      │
│  │ in-mem   │  │ Nuclei   │  │ HTML     │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
blindspot-scanner/
├── backend/                    # FastAPI backend server
│   ├── app.py                  # Main API server (REST endpoints)
│   ├── auth.py                 # JWT authentication (Supabase)
│   ├── config.py               # Central configuration
│   ├── requirements.txt        # Python dependencies
│   ├── ai/                     # AI report generation (Gemini)
│   │   ├── report_generator.py # PDF/HTML report builder
│   │   └── prompts.py          # AI prompt templates
│   ├── engine/                 # Risk scoring & OWASP mapping
│   ├── enrichment/             # CVE lookup (OSV, NVD)
│   ├── export/                 # JSON/PDF/HTML export
│   ├── importers/              # Wappalyzer & Nuclei loaders
│   ├── scanner/                # Core scanning engine
│   │   ├── scan_manager.py     # Scan orchestration
│   │   ├── passive_scanner.py  # Passive security checks
│   │   ├── active_scanner.py   # Active security probes
│   │   ├── rule_scanner.py     # Rule-based detection
│   │   ├── surface_mapper.py   # Attack surface mapping
│   │   ├── request_handler.py  # HTTP request utilities
│   │   └── response_normalizer.py
│   └── storage/                # Elasticsearch & JSON storage
├── web_frontend/               # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx             # Main application component
│   │   ├── App.css             # Application styles
│   │   ├── supabaseClient.js   # Supabase auth client
│   │   └── main.jsx            # Entry point
│   ├── package.json
│   └── vite.config.js
├── extension/                  # Chrome browser extension
│   ├── manifest.json           # Manifest V3
│   ├── popup.html/css/js       # Extension popup UI
│   └── background.js           # Service worker
├── data/                       # Detection data
│   ├── nuclei-templates/       # 13,000+ Nuclei templates
│   └── safe_versions.json      # Known safe software versions
├── rules/                      # Detection rules
│   ├── scan_rules.json         # Curated vulnerability rules
│   └── correlation_rules.json  # Cross-finding correlation
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **Node.js 18+** & npm
- **Git**
- *(Optional)* Elasticsearch 8.x
- *(Optional)* Google Gemini API key (for AI reports)

### 1. Clone the Repository

```bash
git clone https://github.com/Nischal-09/blindspot-scanner.git
cd blindspot-scanner
```

### 2. Backend Setup

```bash
# Create and activate a virtual environment
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in `backend/` or set these environment variables:

```bash
# Required for AI reports
GEMINI_API_KEY=your_gemini_api_key_here

# Optional — Elasticsearch (scanner works without it in memory-only mode)
ES_HOST=https://localhost:9200
ES_USER=elastic
ES_PASS=your_es_password

# Optional — Supabase (for authentication)
SUPABASE_JWT_SECRET=your_jwt_secret
```

> **Note:** The scanner works perfectly without Elasticsearch — it will automatically fall back to in-memory storage mode.

### 4. Start the Backend

```bash
cd backend
python -m uvicorn app:app --host 0.0.0.0 --port 5001 --reload
```

The API will be available at `http://localhost:5001`

### 5. Frontend Setup

```bash
cd web_frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173` (or whichever port Vite assigns).

### 6. Chrome Extension (Optional)

1. Open Chrome → `chrome://extensions/`
2. Enable **Developer Mode** (top right)
3. Click **Load unpacked**
4. Select the `extension/` folder

---

## 🔧 API Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/api/scan` | Submit a new scan | ✅ |
| `GET` | `/api/scan/{id}/status` | Check scan status | ✅ |
| `GET` | `/api/scan/{id}/results` | Get scan results | ✅ |
| `GET` | `/api/scan/{id}/report` | Get JSON report | ✅ |
| `GET` | `/api/scan/{id}/report/pdf` | Download AI PDF report | ✅ |
| `GET` | `/api/scan/{id}/report/html` | Download HTML report | ✅ |
| `GET` | `/api/rules` | List active detection rules | ✅ |
| `POST` | `/api/rules/reload` | Reload detection rules | 🔒 Admin |

---

## 🔒 Security Features

### Scanning Capabilities

- **HTTP Security Headers** — CSP, HSTS, X-Frame-Options, X-Content-Type-Options
- **Cookie Security** — Secure, HttpOnly, SameSite flags
- **SSL/TLS Analysis** — Certificate validation, protocol version checks
- **Software Fingerprinting** — Version detection via Wappalyzer data
- **XSS Detection** — Reflected XSS probe injection with canary tracking
- **SQL Injection** — Error-based and blind (time-based) SQLi detection
- **Path Traversal** — Directory traversal and sensitive file exposure
- **OWASP Top 10 Mapping** — All findings mapped to OWASP categories

### Built-in Security

- JWT-based authentication with Supabase
- Rate limiting on login attempts (5 attempts, 15-min lockout)
- Security headers on all responses (X-Content-Type-Options, X-Frame-Options, etc.)
- CORS configuration with explicit origin allowlisting
- Request body size limits (5 MB)
- Active probe rate limiting (10 RPS default)

---

## 🤖 AI Report Generation

BlindSpot integrates with Google Gemini to generate professional security assessment reports. Reports include:

- Executive summary
- Risk assessment with severity breakdown
- Detailed findings with evidence
- OWASP Top 10 coverage analysis
- Prioritized remediation roadmap
- Professional PDF formatting

> Set your `GEMINI_API_KEY` environment variable to enable AI reports.

---

## 📊 Risk Scoring

The risk engine calculates a composite security score (0-100) based on:

- **Severity weights** — Critical (10), High (7), Medium (4), Low (1)
- **Finding density** — Number of findings relative to attack surface
- **OWASP coverage** — Breadth of vulnerability categories detected

Grades: **A+** (0-5) → **A** (6-15) → **B** (16-30) → **C** (31-50) → **D** (51-70) → **F** (71-100)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, FastAPI, Uvicorn |
| Frontend | React 19, Vite 8 |
| Auth | Supabase (JWT) |
| Database | Elasticsearch 8.x (optional) |
| AI | Google Gemini API |
| Reports | ReportLab (PDF), Custom HTML |
| Detection | Nuclei Templates, Wappalyzer |
| Extension | Chrome Manifest V3 |
| CVE Data | OSV API, NVD API |

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

### Attribution

This project is based on [BlindSpot](https://github.com/basitansari07/BlindSpot) by **basitansari07**, customized and extended with additional features and documentation.

---

## ⚠️ Disclaimer

This tool is intended for **authorized security testing only**. Always obtain proper authorization before scanning any target. Unauthorized scanning may violate laws and regulations. The authors are not responsible for any misuse of this tool.
