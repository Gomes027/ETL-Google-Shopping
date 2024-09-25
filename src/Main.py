import os
import asyncio
from dotenv import load_dotenv
from DataExtractor import ProductExtractor
from DB_Manager import DBManager

load_dotenv()

async def main():
    search_query = '"placa de vídeo asus" rtx "4060"'
    connection_string = f'DRIVER=SQL Server;SERVER={os.getenv("DB_SERVER")};DATABASE={os.getenv("DB_DATABASE")};'

    extractor = ProductExtractor(search_query)
    produtos = await extractor.extract()

    db_manager = DBManager(connection_string)
    db_manager.insert_products(produtos)

if __name__ == '__main__':
    asyncio.run(main())
