from datetime import timedelta

import lancedb
from lancedb.table import Table
from pandas import DataFrame


class LanceDB:

    def __init__(self,
                 vector_storage_path: str = "./lancedb/vector_storage",
                 table_name: str = "knowledge_base"):
        db = lancedb.connect(uri=vector_storage_path)
        import pyarrow as pa
        schema = pa.schema([
            pa.field("content", pa.string()),
            pa.field("page_number", pa.int32()),
            pa.field("pdf_name", pa.string()),
            pa.field("embeddings", pa.list_(pa.float32(), 1024)),
        ])
        try:
            db.create_table(table_name, schema=schema)
            print(f"Table {table_name} created successfully.")
        except Exception as e:
            print(f"Table {table_name} already exists. {e}")
        self.__table: Table = db.open_table(name=table_name)

    def semantic_search(self, vector_query: list[float], n: int = 10, distance_threshold=0.50) -> DataFrame:
        search_results = self.__table.search(vector_query, vector_column_name="embeddings").distance_type(
            "cosine").limit(n).to_pandas()
        print(f"search_results\n\n {search_results}")
        return search_results.loc[search_results["_distance"] <= distance_threshold]

    def get_count(self) -> int:
        return self.__table.count_rows()

    def save(self, df: DataFrame):
        self.__table.add(df)
        print(f"total records in lancedb : {self.__table.count_rows()}")

    def create_index(self):
        try:
            self.__table.create_index(metric="cosine", vector_column_name="embeddings")
        except Exception as e:
            print(f"Seems index already exist {e}")
