-- Example SQL to build a metrics dataset from the clean table
-- Replace `schema.clean_table` with your clean dataset reference if applicable.

-- Example: daily counts by category
SELECT
  CAST(date_col AS DATE) AS dt,
  category,
  COUNT(*) AS n_records
FROM clean_table
GROUP BY CAST(date_col AS DATE), category
ORDER BY dt, category;
