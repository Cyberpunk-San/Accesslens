import asyncio
import aiosqlite
import logging
from pathlib import Path
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DatabaseSetup:
    def __init__(self, db_path: str = "./accesslens.db"):
        self.db_path = Path(db_path)
        
    async def setup(self) -> bool:
        logger.info(f"Starting SQLite database setup at {self.db_path}...")
        
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            async with aiosqlite.connect(self.db_path) as db:
                migration_path = Path(__file__).parent.parent / "migrations" / "001_init.sql"
                
                if not migration_path.exists():
                    logger.error(f"Migration file not found: {migration_path}")
                    return False
                
                with open(migration_path, 'r') as f:
                    sql = f.read()
                
                logger.info("Creating database tables...")
                await db.executescript(sql)
                await db.commit()
                
                async with db.execute("SELECT name FROM sqlite_master WHERE type='table'") as cursor:
                    tables = await cursor.fetchall()
                    logger.info(f"Created {len(tables)} tables:")
                    for table in tables:
                        logger.info(f"  - {table[0]}")
            
            logger.info("Database setup completed successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Failed to setup database: {e}")
            return False

async def main():
    from app.core.config import settings
    db_url = settings.database_url
    
    if db_url.startswith("sqlite:///"):
        db_path = db_url.replace("sqlite:///", "")
    else:
        db_path = "./accesslens.db"
        
    setup = DatabaseSetup(db_path)
    success = await setup.setup()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    asyncio.run(main())