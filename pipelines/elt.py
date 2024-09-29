from prefect import flow

from transform import transform
from titanic import extract_load

@flow
def elt() -> None:
    state = extract_load(return_state=True)
    assert state.is_completed() is True
    transform()

if __name__ == "__main__":
    elt()
