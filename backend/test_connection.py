from sqlalchemy import text

from app.db.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print(result.fetchone())

    print("✅ Connected to Supabase!")

except Exception as e:
    print("❌ Connection Failed")
    print(e)