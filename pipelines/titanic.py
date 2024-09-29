import os

import dlt
import great_expectations as gx
import pandas as pd
from prefect import flow, task

folder_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(folder_path, "..", "data", "duck.db"))

@task
def extract() -> pd.DataFrame:
    titanic_csv = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
    data = pd.read_csv(titanic_csv)
    return data

@task
def validate(data: pd.DataFrame) -> pd.DataFrame:
    context = gx.get_context()
    validator = context.sources.pandas_default.read_dataframe(data)
    validator.expect_column_values_to_be_unique("PassengerId")
    validator.expect_column_values_to_be_in_set("Survived", value_set=(0, 1))
    validator.expect_column_values_to_be_in_set("Pclass", value_set=(1, 2, 3))
    validator.expect_column_values_to_be_unique("Name")
    validator.expect_column_values_to_be_in_set("Sex", value_set=("male", "female"))
    validator.expect_column_values_to_be_between("Age", min_value=0, max_value=80)
    validator.expect_column_values_to_be_between("SibSp", min_value=0, max_value=8)
    validator.expect_column_values_to_be_between("Parch", min_value=0, max_value=6)
    validator.expect_column_values_to_be_of_type("Ticket", type_="object")
    validator.expect_column_values_to_be_between("Fare", min_value=0, max_value=513)
    validator.expect_column_values_to_be_of_type("Cabin", type_="object")
    validator.expect_column_values_to_be_in_set("Embarked", value_set=("S", "C", "Q"))
    validator.save_expectation_suite(discard_failed_expectations=False)
    checkpoint = context.add_or_update_checkpoint(name="gx_checkpoint", validator=validator)
    checkpoint_result = checkpoint.run()
    if not checkpoint_result.success:
        run_results = checkpoint_result.run_results
        raise Exception(f"Validation status: Failed\n{run_results}")
    return data

@task
def load(data: pd.DataFrame) -> None:
    pipeline = dlt.pipeline(
        pipeline_name="titanic_pipeline",
        destination=dlt.destinations.duckdb(db_path),
        dataset_name="raw"
    )
    load_info = pipeline.run(data.to_dict("records"), table_name="titanic")
    print(load_info)

@flow(log_prints=True)
def extract_load() -> None:
    data = extract()
    validated_data = validate(data)
    load(validated_data)

if __name__ == "__main__":
    extract_load()
