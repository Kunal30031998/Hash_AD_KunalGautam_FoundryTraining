# Pipeline Documentation

- **Pipeline Name:** `Hash_AD_KunalGautam_Pipe_FoundryTraining`
- **Flow:** Raw → Clean → Metrics → Dashboard
- **Schedule:** Daily at 06:00 (example)
- **Notifications:** On failure (email/teams)
- **Monitoring:** Check last run status, row counts, freshness
- **Error Handling:** try/except + status dataset with run_id, status, message
