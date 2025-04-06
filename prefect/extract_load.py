import os

import dlt
import pandera.polars as pa
import polars as pl

from prefect import flow, task

folder_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(folder_path, "..", "duckdb", "warehouse.duckdb"))


@task
def extract() -> pl.DataFrame:
    url = (
        "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
    )
    df = pl.read_csv(url)
    return df


@task
def validate(df: pl.DataFrame) -> pl.DataFrame:
    schema = pa.DataFrameSchema(
        {
            "PassengerId": pa.Column(dtype=int, unique=True),
            "Survived": pa.Column(dtype=int, checks=pa.Check.isin({0, 1})),
            "Pclass": pa.Column(dtype=int, checks=pa.Check.isin({1, 2, 3})),
            "Name": pa.Column(dtype=str, unique=True),
            "Sex": pa.Column(dtype=str, checks=pa.Check.isin({"male", "female"})),
            "Age": pa.Column(
                dtype=float,
                checks=pa.Check.between(min_value=0, max_value=80),
                nullable=True,
            ),
            "SibSp": pa.Column(
                dtype=int, checks=pa.Check.between(min_value=0, max_value=8)
            ),
            "Parch": pa.Column(
                dtype=int, checks=pa.Check.between(min_value=0, max_value=6)
            ),
            "Ticket": pa.Column(dtype=str),
            "Fare": pa.Column(
                dtype=float, checks=pa.Check.between(min_value=0, max_value=513)
            ),
            "Cabin": pa.Column(dtype=str, nullable=True),
            "Embarked": pa.Column(
                dtype=str, checks=pa.Check.isin({"S", "C", "Q"}), nullable=True
            ),
        }
    )
    validated_df = schema(df)
    return validated_df


@task
def load(df: pl.DataFrame) -> None:
    pipeline = dlt.pipeline(
        pipeline_name="titanic_pipeline",
        destination=dlt.destinations.duckdb(db_path),
        dataset_name="raw",
    )
    load_info = pipeline.run(data=df.to_dicts(), table_name="titanic")
    print(load_info)


@flow(log_prints=True)
def extract_load() -> None:
    data = extract()
    validated_data = validate(data)
    load(validated_data)


if __name__ == "__main__":
    extract_load()
