# Paste this into a Foundry PySpark transform (or run in a Notebook with Spark session)
# Input: Hash_AD_KunalGautam_Raw_FoundryTraining
# Output: Hash_AD_KunalGautam_Clean_FoundryTraining

from pyspark.sql import functions as F, types as T

# Replace 'input_df' with your actual input DataFrame variable in Foundry (often 'df' or named port)
df = input_df

# 1) Standardize column names
for c in df.columns:
    df = df.withColumnRenamed(c, c.strip().lower().replace(' ', '_'))

# 2) Trim strings
string_cols = [f.name for f in df.schema.fields if isinstance(f.dataType, T.StringType)]
for c in string_cols:
    df = df.withColumn(c, F.trim(F.col(c)))

# 3) Handle missing values (example strategies)
# - Fill empty strings with None, then impute simple defaults
for c in string_cols:
    df = df.withColumn(c, F.when(F.col(c) == '', None).otherwise(F.col(c)))

numeric_cols = [f.name for f in df.schema.fields if isinstance(f.dataType, (T.IntegerType, T.DoubleType, T.LongType, T.FloatType))]
for c in numeric_cols:
    df = df.withColumn(c, F.when(F.isnan(F.col(c)) | F.col(c).isNull(), None).otherwise(F.col(c)))

# Example imputations (tweak per dataset)
for c in numeric_cols:
    mean_val = df.select(F.mean(F.col(c)).alias('m')).collect()[0]['m']
    if mean_val is not None:
        df = df.fillna({c: float(mean_val)})

# 4) Deduplicate if you have a natural key (edit keys list)
keys = []  # e.g., ['ticket_id']
if keys:
    df = df.dropDuplicates(keys)

# 5) Add audit columns
df = df.withColumn('run_id', F.lit(F.current_timestamp()))
df = df.withColumn('record_hash', F.sha2(F.concat_ws('||', *[F.col(c).cast('string') for c in df.columns]), 256))

# Assign output
output_df = df
