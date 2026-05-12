"""
Verify MongoDB Atlas connection before starting up the app
"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings


async def test_connection():
    print(f"Connecting to: {settings.MONGO_URI[:40]}...")  # partial URI, hides password
    print(f"Database: {settings.MONGO_DB_NAME}\n")

    try:
        client = AsyncIOMotorClient(
            settings.MONGO_URI,
            serverSelectionTimeoutMS=5_000,
        )

        # 1. Ping the server
        await client.admin.command("ping")
        print("✓ Ping successful — server is reachable")

        # 2. List databases (confirms auth is working)
        db_names = await client.list_database_names()
        print(f"✓ Auth OK — databases visible: {db_names}")

        # 3. Access the target database and list collections
        db = client[settings.MONGO_DB_NAME]
        collections = await db.list_collection_names()
        if collections:
            print(f"✓ Collections in '{settings.MONGO_DB_NAME}': {collections}")
        else:
            print(
                f"✓ Connected to '{settings.MONGO_DB_NAME}' (empty — collections will be created on first write)"
            )

        # 4. Quick write + read + delete to confirm read/write permissions
        test_col = db["_connection_test"]
        result = await test_col.insert_one({"test": True})
        print(f"✓ Write OK — inserted doc id: {result.inserted_id}")

        doc = await test_col.find_one({"_id": result.inserted_id})
        print(f"✓ Read OK — retrieved: {doc}")

        await test_col.delete_one({"_id": result.inserted_id})
        print("✓ Delete OK — test document cleaned up")

        client.close()
        print("\nAll checks passed — your Atlas connection is working correctly.")

    except Exception as e:
        print(f"\n✗ Connection failed: {e}")
        print("\nThings to check:")
        print("  1. MONGO_URI in your .env is correct")
        print("  2. Your IP is whitelisted in Atlas → Network Access")
        print("  3. The database user credentials are correct")
        print("  4. The cluster is not paused (free tier pauses after inactivity)")


if __name__ == "__main__":
    asyncio.run(test_connection())
