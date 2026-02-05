import pandas as pd
from fastmcp import FastMCP
import os

mcp = FastMCP("Heart Data Server")

DATA_PATH = os.path.join(os.path.dirname(__file__), "heart.csv")
df = pd.read_csv(DATA_PATH)

@mcp.tool()
def get_age(age: int) -> str:
    """Get all rows for a specific age."""
    result = df[df["age"] == age]
    return result.to_json(orient="records")


@mcp.tool()
def get_sex(sex: int) -> str:
    """Get all rows for a specific sex (0=female, 1=male)."""
    result = df[df["sex"] == sex]
    return result.to_json(orient="records")


if __name__ == "__main__":
    mcp.run()
