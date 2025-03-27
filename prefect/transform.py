import os

from prefect_dbt.cli.commands import DbtCoreOperation

from prefect import task

folder_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(folder_path, "..", "dbt"))


@task
def transform() -> str:
    result = DbtCoreOperation(
        commands=["pwd", "dbt debug", "dbt run"],
        project_dir=project_path,
        profiles_dir=project_path,
    ).run()
    return result


if __name__ == "__main__":
    transform()
