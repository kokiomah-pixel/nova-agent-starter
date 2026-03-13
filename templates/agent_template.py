import requests
import os

API_URL = os.getenv("NOVA_API_URL", "https://api.novaos.ai")
API_KEY = os.getenv("NOVA_API_KEY", "")

def nova_context(asset, intent, size, venue=None, strategy=None):
    headers = {}

    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"

    params = {
        "asset": asset,
        "intent": intent,
        "size": size
    }

    if venue:
        params["venue"] = venue

    if strategy:
        params["strategy"] = strategy

    response = requests.get(
        f"{API_URL}/v1/context",
        params=params,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    ctx = nova_context(asset="ETH", intent="trade", size=10000)

    print("Regime:", ctx.get("regime"))
    print("Guardrail:", ctx.get("guardrail", {}).get("advisory"))
    print("Memory Context:", ctx.get("memory_context"))
