import os
from pathlib import Path

QUERIES_PATH = Path(__file__).resolve().parent / 'database' / 'queries.sql'
DB_CONNECT = f"postgresql://postgres:{os.getenv('pgAdmin')}@localhost:5432/hh_parser"
EMPLOYER_MAP = {
    "Компания_Индид": 804242,
    "ProductStar": 5255057,
    "билайн": 4934,
    "KVINT": 4010751,
    "Brand_Analytics": 2548771,
    "ООО_Защищенные_Телекоммуникации": 1234997,
    "МойСклад": 208576,
    "SpectrumData": 3542906,
    "Mindbox": 205152,
    "ООО_Сбер_Бизнес_Софт": 9301808,
}
