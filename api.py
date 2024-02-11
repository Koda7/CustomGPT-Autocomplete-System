from fastapi import FastAPI, Query
import json
import pandas as pd

app = FastAPI()


@app.get("/query")
async def search(
    query: str = Query(..., min_length=1),  # Min length validation for query
    count: int = Query(10, ge=1),  # Range validation for count
):
    if query not in lookup:
        return [""]
    possibleQueries = lookup[query][-count:]
    possibleQueries.reverse()
    results = [data["Query"][index] for _, index in possibleQueries]
    return results


# Start the server
if __name__ == "__main__":
    with open("lookup.json", "r") as f:
        lookup = json.load(f)
    data = pd.read_csv("data.csv")
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
