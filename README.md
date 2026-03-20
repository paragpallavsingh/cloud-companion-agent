# ☁️ Cloud Companion: The AI Senior TA

**Cloud Companion** is a multi-agent mentorship system built for the Hack2Skill Track 1. It bridges the gap between complex Google Cloud documentation and student understanding by "translating" technical facts into friendly, analogy-driven guidance.

---

## 🚀 Key Features
* **Multi-Agent Architecture:** Uses a Sequential Workflow (Researcher → Mentor).
* **Technical Accuracy:** Powered by Gemini 1.5 Flash via Vertex AI.
* **Serverless Deployment:** Hosted on Google Cloud Run for high scalability.

---

## 🛠️ Technical Stack
* **LLM:** Gemini 1.5 Flash
* **Framework:** Google ADK (Agent Development Kit)
* **Infrastructure:** Google Cloud Run (asia-south1)
* **Containerization:** Docker

---

## 💻 Essential Commands Reference

### 1. Local Development & Setup
```bash
# Install the Google ADK
pip install google-adk

# Initialize the project
adk init
```

### 2. Deployment to Cloud Run
```bash
# Deploy with a built-in Web UI
uvx --from google-adk==1.14.0 adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=asia-south1 \
  --service_name=cloud-companion-mentor \
  --with_ui .
```

### 3. Management & Cleanup
```bash
# List running services to get the URL
gcloud run services list --platform managed --region asia-south1

# Check build logs if deployment fails
gcloud builds list --limit 5

# Delete service to stop costs
gcloud run services delete cloud-companion-mentor --region asia-south1
```

---

## 🏗️ The Agent Flow
The system follows a **Sequential Pipeline**:
1. **Greeter Agent:** Routes the user query.
2. **Tech Researcher:** Fetches precise GCP/Python syntax.
3. **Student Mentor:** Adds persona, analogies, and encouragement.

