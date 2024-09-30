import os

folder_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(folder_path, "..", "duckdb", "data.db"))
dbt_path = os.path.join(os.path.expanduser("~"), ".dbt")
profile_path = os.path.join(dbt_path, "profiles.yml")

profile = f"""mini_mds:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: {db_path}
"""

# Make .dbt directory if it does not exist
os.makedirs(dbt_path, exist_ok=True)

# Write connection profile
with open(profile_path, "a") as f:
    f.write(profile)
