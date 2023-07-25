import pytest
# from ..schemes import Category
from tasks.schemes import Category

@pytest.fixture
def category() -> Category:
    return Category(name="Book FastAPI")

def test_event_name(category: Category) -> None:
    assert category.name == "Book FastAPI"