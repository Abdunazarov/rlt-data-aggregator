from pymongo import MongoClient
from datetime import datetime
from settings import MONGODB_URI, DB_NAME, COLLECTION_NAME

class DataAggregator:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def aggregate_data(self, dt_from, dt_upto, group_type):
        dt_from_parsed = datetime.fromisoformat(dt_from.rstrip("Z"))
        dt_upto_parsed = datetime.fromisoformat(dt_upto.rstrip("Z"))

        # Определение формата группировки
        group_format = {"hour": "%Y-%m-%dT%H", "day": "%Y-%m-%d", "month": "%Y-%m"}.get(group_type, "%Y-%m-%d")

        # Создание агрегационного пайплайна
        pipeline = [
            {"$match": {"dt": {"$gte": dt_from_parsed, "$lte": dt_upto_parsed}}},
            {
                "$group": {
                    "_id": {"$dateToString": {"format": group_format, "date": "$dt"}},
                    "total_value": {"$sum": "$value"},
                }
            },
            {"$sort": {"_id": 1}},
        ]

        # Выполнение агрегации
        result = list(self.collection.aggregate(pipeline))
        dataset = [entry["total_value"] for entry in result]
        
        # Формирование меток в зависимости от типа агрегации
        if group_type == "month":
            labels = [f"{label}-01T00:00:00" for label in [entry["_id"] for entry in result]]
        else:
            labels = [entry["_id"] for entry in result]

        return {"dataset": dataset, "labels": labels}
