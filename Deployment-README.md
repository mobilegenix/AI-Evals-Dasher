# AI-Evals-Dasher
AI Evaluation Dashboard built in React
# 🚀 AI Evals Dashboard Deployment Guide

This guide walks you through deploying the full stack for the AI Evals Dashboard:
- FastAPI backend (Snowflake/Databricks integration)
- React frontend dashboard
- Dockerized deployment
- NGINX reverse proxy with HTTPS (Certbot)

---

## 📁 Project Structure
```
├── backend/               # FastAPI + eval logic
│   ├── evals_backend.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/              # React + Recharts
│   └── (your React app)
├── docker-compose.yml     # For dev orchestration
├── docker-compose-deploy.yml # For production deployment
├── nginx-reverse-proxy.conf
└── .env.template           # Environment variable sample
```

---

## ⚙️ Backend Setup
```bash
# Set environment variables
cp .env.template .env
# Replace values with Snowflake/Databricks credentials

# Run locally
cd backend
uvicorn evals_backend:app --reload
```

## 🐳 Docker Compose (Dev)
```bash
docker-compose up --build
```

## 🐳 Docker Compose (Deploy)
```bash
docker-compose -f docker-compose-deploy.yml up -d
```

---

## 🌐 NGINX + HTTPS
### 1. Install NGINX
```bash
sudo apt update && sudo apt install nginx -y
```

### 2. Deploy config
```bash
sudo cp nginx-reverse-proxy.conf /etc/nginx/sites-available/yourdomain.com
sudo ln -s /etc/nginx/sites-available/yourdomain.com /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx
```

### 3. Get SSL with Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
```

---

## 🔁 Health Check Endpoint
```bash
curl http://yourdomain.com/health
```
Returns:
```json
{
  "status": "ok",
  "snowflake": "connected",
  "databricks": "connected"
}
```

---

## ✅ CI/CD Workflows
- `.github/workflows/ci.yml`: test + lint
- `.github/workflows/docker-deploy.yml`: build + push to Docker Hub

---

## 🧩 Extend This Project
- Add user auth for protected dashboards
- Implement real-time alerting
- Build multi-tenant model eval support

---

_This stack is designed for fast iteration and enterprise integration. Built and maintained by Lindon Thomas._
