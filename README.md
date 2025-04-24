# 🧠 AI Evals Dashboard

**AI Evals Dashboard** is a modern, full-stack application designed to evaluate, visualize, and track the performance of LLM-based and enterprise AI deployments across multiple infrastructures.

---

## 🌟 Why It Exists

LLM-based products often go live without proper evaluation systems in place. Without clear insight into adoption metrics, latency trends, hallucination rates, or cost efficiency, it's hard to tell if your AI investment is working—or working safely.

**This app exists to:**
- Provide stakeholders a clear view of AI system performance
- Standardize evaluations across teams
- Track cost, accuracy, latency, and user opt-out rates
- Support decision-making with real-time data from Snowflake/Databricks

---

## 🚀 What It Does

- **Ingests evaluation metrics** from enterprise data sources (Snowflake, Databricks)
- **Visualizes key metrics** in real time: Accuracy, Latency, Cost, Opt-out Rate
- **Offers CI/CD and health monitoring** for production-grade reliability
- **Provides secure public dashboards** via NGINX + HTTPS

---

## 🧩 System Components

| Layer            | Stack/Tooling                      |
|------------------|-----------------------------------|
| Frontend         | React, Recharts, Tailwind         |
| Backend API      | FastAPI, Python 3.11              |
| Data Connectors  | Snowflake, Databricks             |
| CI/CD            | GitHub Actions, DockerHub         |
| Hosting          | Docker Compose, NGINX, Certbot    |
| Security         | HTTPS (Let's Encrypt)             |

---

## 🛠️ Core Packages

### Python Backend
- `fastapi`
- `uvicorn[standard]`
- `snowflake-connector-python`
- `databricks-sql-connector`
- `pydantic`
- `python-dotenv`

### React Frontend
- `react`
- `recharts`
- `axios`
- `tailwindcss`

---

## 🧠 Future Enhancements
- User authentication and role-based access control
- Per-model eval scoring with version comparison
- Slack/Teams alerting for KPI drops
- RAG and prompt engineering eval support
- Real-time anomaly detection via WebSockets

---

## 📎 Project Philosophy
> *“Software in hand beats documentation on paper.”*

This project follows agile principles: rapid iteration, working MVPs, and metrics-first thinking. It aims to help organizations reduce AI uncertainty and make better decisions, faster.

---

## 👨‍💻 Created By
**Lindon Thomas**  
AI Product & Program Management Leader  
🔗 [linkedin.com/in/lindonthomas](https://linkedin.com/in/lindonthomas)  
🔗 [theinfinitemachine.net](https://www.theinfinitemachine.net)
