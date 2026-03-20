#!/bin/bash

# --- 1. Define Variables ---
# Update these if you change projects or regions
export PROJECT_ID="devops-dashboard-490606"
export LOCATION="asia-south1"
export SERVICE_ACCOUNT="agent-service-account@$PROJECT_ID.iam.gserviceaccount.com"

# --- 2. Re-create the .env file (Ignored by Git) ---
echo "Re-creating .env file..."
cat <<ENV > .env
PROJECT_ID=$PROJECT_ID
LOCATION=$LOCATION
SERVICE_ACCOUNT=$SERVICE_ACCOUNT
ENV

# --- 3. Authenticate with Google Cloud ---
echo "Authenticating with GCP..."
gcloud auth login
gcloud config set project $PROJECT_ID

# --- 4. Install Dependencies ---
echo "Installing UV and Google ADK..."
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
pip install google-adk==1.14.0

echo "-----------------------------------------------"
echo "Setup Complete! Your .env is ready."
echo "You can now run: uvx adk deploy cloud_run ..."
echo "-----------------------------------------------"
