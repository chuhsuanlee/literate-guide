from great_expectations.dataset import SqlAlchemyDataset

from configs.config import SQLALCHEMY_DB_URI


def check_row_count_match(table_name: str, row_count: int):

    dataset = SqlAlchemyDataset(connection_string=SQLALCHEMY_DB_URI, table_name=table_name)

    data_expectation = dataset.expect_table_row_count_to_equal(value=row_count, result_format='BOOLEAN_ONLY')

    return data_expectation.get_metric("expect_table_row_count_to_equal.success")
