
if __name__ == "__main__":
    import os
    from server.database.creator import create_database

    if not os.path.isfile("./server/database/data.db"):
        print("Creating database")
        create_database("server/database/data.db")
    import uvicorn
    from server.app import app

    uvicorn.run(app)
