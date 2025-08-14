# Step‑by‑Step (Layman Friendly)

> Replace `KunalGautam` everywhere with your real name and pick `AD` = `DE`, `ML`, or `AD`.

---
## A. Project Setup & GitHub (15%)

1. **Create GitHub Repo**
   - Go to github.com → New → Repository name: `foundry-sandbox-KunalGautam` → Create.
   - Copy the **SSH/HTTPS URL**.

2. **Clone & Push (on your laptop)**
   ```bash
   git clone <your-repo-url>
   cd foundry-sandbox-KunalGautam
   # Copy the starter kit into this folder, then:
   git add .
   git commit -m "chore: init Palantir Foundry sandbox starter"
   git push
   ```

3. **Foundry Project**
   - In Foundry: Create Project named `Hash_AD_KunalGautam_Sandbox`.
   - Inside it, create a folder `Personal/KunalGautam` → this is your **personal sandbox**.

4. **Code Repository in Foundry**
   - Add a **Code Repository** in the project.
   - Connect it to your GitHub repo (mirror/sync).
   - Verify files appear in Foundry Code Repos.

✅ **You’re done when**: Repo exists on GitHub, linked in Foundry, and you see all files.

---
## B. Data Ingestion (10%)

Choose one public CSV (simple is fine):
- City service requests (e.g., “311” data), air quality, weather history, or sales sample CSV.

1. **Create Dataset (Raw)**
   - In Foundry: Datasets → New → Upload.
   - Name: `Hash_AD_KunalGautam_Raw_FoundryTraining` (e.g., `Raw_311`).
   - Upload your CSV.

2. **Document Source**
   - Open `docs/03_ingestion_log.md` and note: source URL, columns, refresh frequency.

✅ **You’re done when**: Raw dataset exists and `03_ingestion_log.md` is filled.

---
## C. Transform & Clean (15%)

1. **Open Notebook**
   - Open `notebooks/EDA_template.ipynb` in Foundry Notebook.
   - Run all cells: you’ll see profiles, missing values, and sample charts.

2. **Create Clean Dataset via PySpark**
   - Add a **PySpark Transform** node in Foundry pipeline canvas.
   - Use code from `transforms/clean_pyspark.py` (paste it into the transform).
   - Output dataset name: `Hash_AD_KunalGautam_Clean_FoundryTraining`.

3. **Log Choices**
   - Update `docs/04_transformation_notes.md` to explain what you cleaned and why.

✅ **You’re done when**: Clean dataset exists and notes explain decisions.

---
## D. Analytical Dashboard (15%)

1. **Create a Report (Dashboard)**
   - Foundry → Reports (or equivalent analytics module).
   - Name: `Hash_AD_KunalGautam_Report_FoundryTraining`.

2. **Add Visuals**
   - KPIs (counts, averages).
   - A time series chart.
   - A bar chart by a category.
   - A table with filters (date range, category).

3. **Describe the Dashboard**
   - Update `docs/05_dashboard_doc.md` with purpose, visuals, and who should use it.

✅ **You’re done when**: Report opens with 2–4 charts and interactive filters.

---
## E. Automated Data Pipeline (20%)

1. **Connect Steps**
   - In the pipeline canvas, connect: **Raw → Clean → Metrics → Dashboard**.
   - “Metrics” can be a small SQL/PySpark node that computes aggregates.

2. **Schedule**
   - Set schedule to **daily 06:00** (or any time you choose).
   - Enable notifications on failure.

3. **Error Handling & Logging**
   - Ensure transforms write a small **status dataset** (ok/error, rows processed).
   - Turn on **logs**. Use try/except in code to catch and log issues.

4. **Document Pipeline**
   - Update `docs/06_pipeline_doc.md` with a diagram, schedule, and monitoring steps.

✅ **You’re done when**: Pipeline runs end‑to‑end on schedule and sends alerts on failure.

---
## F. Deployment (10%)

1. **Publish Dashboard**
   - Share with stakeholders (read permissions).
   - Add a short usage guide.

2. **Access Instructions**
   - Update `ACCESS_INSTRUCTIONS.md` with the link/path and who has access.

✅ **You’re done when**: Others can open and use your dashboard without you.

---
## G. Documentation & Reporting (15%)

- Keep all docs current in the `docs/` folder.
- Use the `07_final_report_template.md` to summarize outcomes, limits, and next steps.

---
## Naming Cheat‑Sheet

- Project: `Hash_AD_KunalGautam_Sandbox`
- Raw Dataset: `Hash_AD_KunalGautam_Raw_FoundryTraining`
- Clean Dataset: `Hash_AD_KunalGautam_Clean_FoundryTraining`
- Metrics Dataset: `Hash_AD_KunalGautam_Metrics_FoundryTraining`
- Report: `Hash_AD_KunalGautam_Report_FoundryTraining`
- Pipeline: `Hash_AD_KunalGautam_Pipe_FoundryTraining`
