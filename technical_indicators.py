"""RSI-14 (Wilder) and SMA20/50 for equity historicals from Robinhood.

Usage:
    python technical_indicators.py <get_equity_historicals_response.json>

Input JSON is the raw response shape returned by the
mcp__robinhood-trading__get_equity_historicals tool:
{"data": {"results": [{"symbol": ..., "bars": [{"close_price": ...}, ...]}, ...]}}
"""
import json
import sys


def wilder_rsi(closes, period=14):
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    gains = [max(d, 0) for d in deltas]
    losses = [max(-d, 0) for d in deltas]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def sma(closes, period):
    if len(closes) < period:
        return None
    return sum(closes[-period:]) / period


def analyze(closes):
    last, first = closes[-1], closes[0]
    s20, s50 = sma(closes, 20), sma(closes, 50)
    rsi14 = wilder_rsi(closes, 14)

    def vs_sma(sma_val):
        if sma_val is None:
            return 'NA'
        return 'above' if last > sma_val else 'below'

    cross = 'NA'
    if s20 is not None and s50 is not None:
        cross = 'golden (20>50)' if s20 > s50 else 'death (20<50)'

    return {
        'n_bars': len(closes),
        'last_close': last,
        'first_close': first,
        'pct_change': (last - first) / first * 100,
        'rsi14': rsi14,
        'sma20': s20,
        'sma50': s50,
        'price_vs_sma20': vs_sma(s20),
        'price_vs_sma50': vs_sma(s50),
        'cross': cross,
    }


def analyze_historicals_json(path):
    data = json.load(open(path, encoding='utf-8'))
    results = {}
    for entry in data['data']['results']:
        closes = [float(b['close_price']) for b in entry['bars']]
        results[entry['symbol']] = analyze(closes)
    return results


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python technical_indicators.py <get_equity_historicals_response.json>')
        sys.exit(1)
    for sym, r in analyze_historicals_json(sys.argv[1]).items():
        print(sym, r)
