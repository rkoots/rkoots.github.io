import os
import yaml
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key is not set in environment variables")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

input_structure = {
    "nifty": {
        "value": None,
        "change": None
    },
    "banknifty": {
        "value": None,
        "change": None
    },
    "vix": None,
    "pcr": None,
    "fibonacci_retracement": None,
    "fii_flow": None,
    "dii_flow": None,
    "news": [None, None],
    "ai_outlook": None,
    "gainers": [
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
    ],
    "losers": [
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
        {"symbol": None, "name": None, "change": None, "percent": None},
    ],
}

prompt = f"""Analyze today's financial market outlook in depth with data available with you. Provide:
- Nifty (current value and change)
- Bank Nifty (current value and change)
- VIX
- Put-Call Ratio
- FII Flow
- DII Flow
- Fibonacci Retracement Level
- Market News
- Gainers (at least 6 stocks with their symbol, name, price change, percent change)
- Losers (at least 6 stocks with their symbol, name, price change, percent change)
- An in-depth, 4-5 paragraph Market Outlook
Output the data in YAML format following this structure:

{yaml.dump(input_structure, default_flow_style=False)}
"""

ai_response = model.generate_content(prompt)
generated_report = ai_response.text.strip()

with open("generated_report.yaml", "w") as f:
    f.write(generated_report)

print("Generated report successfully saved to generated_report.yaml")