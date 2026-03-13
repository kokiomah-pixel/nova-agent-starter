import requests

API_URL = "https://api.novaos.ai"

def nova_context(asset="ETH", intent="trade", size=10000):
    response = requests.get(
        f"{API_URL}/v1/context",
        params={
            "asset": asset,
            "intent": intent,
            "size": size
        }
    )

    return response.json()

def main():
    ctx = nova_context()

    regime = ctx.get("regime")
    guardrail = ctx.get("guardrail", {}).get("severity")

    print("Nova Regime:", regime)
    print("Guardrail Severity:", guardrail)

    if regime == "Stress":
        print("Action: Reduce risk")

    elif guardrail == "high":
        print("Action: Adjust position")

    else:
        print("Action: Execute strategy")

if __name__ == "__main__":
    main()
