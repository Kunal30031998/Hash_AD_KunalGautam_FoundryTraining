# Palantir Sandbox Environment Guidelines (Training)

## Data Usage and Security
- **No sensitive data** (PII, client data, financials, proprietary info).
- **Data classification** before upload. Use automated checks to detect PII.

## Access Control
- **RBAC**: grant only what is required.
- **POLP**: least privilege everywhere.

## Resource Management
- Be mindful of **compute guardrails** and quotas.
- Keep a clean **project structure**: separate raw, clean, analytics, and docs.

## Environment Usage
- **Sandbox only** for training & development. No production/live data.
- Use **personal sandbox folders** for each user.

## Compliance & Monitoring
- **Audit trails** are enabled; assume everything is logged.
- **Regular reviews** of access, structure, and data classifications.

## Collaboration & Communication
- Bring in **stakeholders** early (dev, IT, risk).
- Continuous **training and awareness**.

## Naming Rule (Major Ask)
Prefix everything with: `Hash_AD_KunalGautam_...` where AREA ∈ {DE, ML, AD}.
Example: `Hash_AD_JaneDoe_ServiceName`.
