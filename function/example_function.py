from database.example_database import example_database
from infunction.example_infunction import example_infunction


def example_functiion():
    data = example_database() + " " + example_infunction()
    return data
