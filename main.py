from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
        Function which returns a simple dictionary

        Returns:
            dict
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: str = None):
    """
        Function which returns a simple dictionary

        Returns:
            dict
    """
    return {"item_id": item_id, "query": query}
