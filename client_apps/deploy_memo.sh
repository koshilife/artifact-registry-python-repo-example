gcloud config set project ${GCP_PROJECT}

app_name="artifact-registry-client-example"

# ==============================================================
# App Engine
# refs: https://cloud.google.com/sdk/gcloud/reference/app/deploy

cd appengine
gcloud app deploy --project ${GCP_PROJECT}
gcloud app browse

# ==============================================================
# Cloud Run
# refs: https://cloud.google.com/sdk/gcloud/reference/run/deploy

# deploy
gcloud run deploy ${app_name} \
  --source "cloudrun" \
  --allow-unauthenticated \
  --region asia-northeast1 \
  --max-instances 1 \
  --min-instances 0 \
  --cpu 1 \
  --memory 1Gi \
  --set-env-vars "GCP_PROJECT=${GCP_PROJECT}"

# ==============================================================
# Cloud Functions
# refs: https://cloud.google.com/sdk/gcloud/reference/functions/deploy

# deploy
gcloud functions deploy ${app_name} \
  --source "functions" \
  --entry-point main \
  --runtime python39 \
  --trigger-http \
  --region asia-northeast1 \
  --allow-unauthenticated
  --timeout 120 \
  --memory 128MB \
  --min-instances 0 \
  --max-instances 1 \
  --set-env-vars "GCP_PROJECT=${GCP_PROJECT}"
