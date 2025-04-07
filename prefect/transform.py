from pathlib import Path

from prefect_dbt.cli.commands import DbtCoreOperation

from prefect import task


@task
def transform() -> str:
    project_path = Path(__file__).parent.parent / "dbt"
    result = DbtCoreOperation(
        commands=["pwd", "dbt debug", "dbt run"],
        project_dir=project_path,
        profiles_dir=project_path,
    ).run()
    return result


if __name__ == "__main__":
    transform()
