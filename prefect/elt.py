from titanic import extract_load
from transform import transform

from prefect import flow


@flow
def elt() -> None:
    state = extract_load(return_state=True)
    assert state.is_completed() is True
    transform()


if __name__ == "__main__":
    elt()
