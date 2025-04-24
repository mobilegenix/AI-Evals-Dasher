from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import snowflake.connector
import os

# Optional: Import for Databricks
import databricks.sql

app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EvalMetric(BaseModel):
    timestamp: str
    accuracy: float
    latency: float
    cost: float
    optOutRate: float

# Snowflake connection parameters (replace with actual secrets or environment variables)
SNOWFLAKE_CONFIG = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA')
}

# Databricks connection parameters
DATABRICKS_CONFIG = {
    'server_hostname': os.getenv('DATABRICKS_HOST'),
    'http_path': os.getenv('DATABRICKS_HTTP_PATH'),
    'access_token': os.getenv('DATABRICKS_TOKEN')
}

@app.get("/api/evals-data", response_model=List[EvalMetric])
def get_evals_data(source: str = 'snowflake'):
    query = """
    SELECT 
        TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') AS timestamp,
        accuracy,
        latency,
        cost,
        opt_out_rate AS optOutRate
    FROM ai_eval_metrics
    ORDER BY timestamp DESC
    LIMIT 100
    """

    if source == 'databricks':
        with databricks.sql.connect(
            server_hostname=DATABRICKS_CONFIG['server_hostname'],
            http_path=DATABRICKS_CONFIG['http_path'],
            access_token=DATABRICKS_CONFIG['access_token']
        ) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
    else:
        with snowflake.connector.connect(**SNOWFLAKE_CONFIG) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

    evals_data = [
        EvalMetric(
            timestamp=row[0],
            accuracy=row[1],
            latency=row[2],
            cost=row[3],
            optOutRate=row[4]
        ) for row in rows
    ]

    return evals_data
