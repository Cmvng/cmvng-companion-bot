"""
CMVNG SIGNALVAULT — COMPANION BOT
Runs alongside your existing signal bot.
Handles: user registration, subscriptions, tier-gated signal delivery.

Your existing bot calls /broadcast on this server when a signal fires.
This bot then sends it to each registered user based on their plan.
"""

from flask import Flask, request, jsonify
import requests
import os
import json
import threading
import time
from datetime import datetime, timezone

app = Flask(__name__)

# ─── Config ───────────────────────────────────────────────────

COMPANION_BOT_TOKEN = os.environ.get("COMPANION_BOT_TOKEN", "")
PAYMENT_API = os.environ.get("PAYMENT_API", "https://cmvng-payment-api-production.up.railway.app")
CHECKOUT_URL = os.environ.get("CHECKOUT_URL", "https://cmvng-checkout-3.vercel.app")

# Store registered user IDs (in production, use a database)
USERS_FILE = "registered_users.json"

# ─── User Storage ─────────────────────────────────────────────

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def register_user(user_id, username="", first_name=""):
    users = load_users()
    user_id = str(user_id)
    if user_id not in users:
        users[user_id] = {
            "username": username,
            "first_name": first_name,
            "registered_at": datetime.now(timezone.utc).isoformat()
        }
        save_users(users)
        return True
    return False

# ─── Telegram Helpers ─────────────────────────────────────────

def send_message(chat_id, text, parse_mode="HTML"):
    if not COMPANION_BOT_TOKEN:
        print("No bot token set!")
        return
    url = "https://api.telegram.org/bot{}/sendMessage".format(COMPANION_BOT_TOKEN)
    try:
        r = requests.post(url, json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": True
        }, timeout=10)
        if not r.json().get("ok"):
            print("Telegram error for {}: {}".format(chat_id, r.json()))
    except Exception as e:
        print("Send error to {}: {}".format(chat_id, e))

def check_user_plan(user_id):
    """Ask the payment API what plan this user is on"""
    try:
        r = requests.get("{}/can-send?user_id={}".format(PAYMENT_API, user_id), timeout=5)
        return r.json()
    except:
        return {"allowed": True, "tier": 0, "tier_name": "Free"}

def mark_signal_sent(user_id):
    """Tell the payment API a signal was sent to this user"""
    try:
        requests.post("{}/signal-sent".format(PAYMENT_API),
                      json={"user_id": str(user_id)}, timeout=5)
    except:
        pass

# ─── Telegram Webhook (handles user commands) ─────────────────

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    if not data or "message" not in data:
        return "ok"

    message = data["message"]
    chat_id = message["chat"]["id"]
    user_id = str(message["from"]["id"])
    username = message["from"].get("username", "")
    first_name = message["from"].get("first_name", "")
    text = message.get("text", "").strip()

    # Register user on any interaction
    register_user(user_id, username, first_name)

    # ── /start (with optional deep link: /start pro, /start elite, etc.) ──
    if text == "/start" or text.startswith("/start "):
        parts = text.split(" ", 1)
        deep_link = parts[1].lower().strip() if len(parts) > 1 else ""

        # If deep link is a plan name, send payment link
        plan_prices = {"pro": 15, "elite": 50, "institutional": 150}

        if deep_link in plan_prices:
            plan_name = deep_link.capitalize()
            price = plan_prices[deep_link]
            pay_url = "{}?tgid={}&tier={}&price={}".format(CHECKOUT_URL, user_id, deep_link, price)

            register_user(user_id, username, first_name)

            msg = (
                "👋 <b>Welcome to Cmvng SignalVault!</b>\n\n"
                "You selected the <b>{}</b> plan — {} USDC/month.\n\n"
                "To activate, pay with USDC on Arc Testnet:\n\n"
                "💳 <a href='{}'>👉 Open Payment Page</a>\n\n"
                "<i>Need testnet USDC? Get it free at faucet.circle.com</i>\n\n"
                "━━━━━━━━━━━━━━━━━━━\n"
                "Want a different plan? /subscribe"
            ).format(plan_name, price, pay_url)
            send_message(chat_id, msg)
            return "ok"

        if deep_link == "free":
            register_user(user_id, username, first_name)
            msg = (
                "👋 <b>Welcome to Cmvng SignalVault!</b>\n\n"
                "You're on the <b>Free</b> plan.\n"
                "You'll receive <b>2 signals per day</b> on random profitable pairs.\n\n"
                "Signals will start arriving automatically.\n\n"
                "⚡ /subscribe — Upgrade for unlimited signals\n"
                "📊 /status — Check your plan"
            )
            send_message(chat_id, msg)
            return "ok"

        # Normal /start without deep link
        plan = check_user_plan(user_id)
        tier_name = plan.get("tier_name", "Free")

        if plan.get("tier", 0) >= 1:
            welcome = (
                "👋 <b>Welcome to Cmvng SignalVault!</b>\n\n"
                "You're on the <b>{}</b> plan.\n"
                "You'll receive all signals automatically.\n\n"
                "📊 /status — Check your plan\n"
                "📈 /pairs — See your pairs"
            ).format(tier_name)
        else:
            welcome = (
                "👋 <b>Welcome to Cmvng SignalVault!</b>\n\n"
                "You're on the <b>Free</b> plan.\n"
                "You'll receive <b>2 signals per day</b> on random profitable pairs.\n\n"
                "⚡ /subscribe — Upgrade for unlimited signals\n"
                "📊 /status — Check your plan\n"
                "📈 /pairs — See available pairs"
            )
        send_message(chat_id, welcome)

    # ── /subscribe ──
    elif text == "/subscribe":
        url = "{}?tgid={}".format(CHECKOUT_URL, user_id)
        msg = (
            "⚡ <b>Upgrade your Cmvng SignalVault plan</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━\n\n"
            "<b>Pro — 15 USDC/mo</b>\n"
            "• T1 + T2 real-time signals\n"
            "• All profitable forex & crypto pairs\n"
            "• Entry, SL & TP levels\n"
            "• Signal history & win-rate stats\n\n"
            "<b>Elite — 50 USDC/mo</b>\n"
            "• Everything in Pro\n"
            "• T1 priority delivery\n"
            "• All pairs unlocked\n"
            "• Multi-TP scaling targets\n"
            "• VIP Telegram group\n\n"
            "<b>Institutional — 150 USDC/mo</b>\n"
            "• Everything in Elite\n"
            "• Signal API access (JSON webhook)\n"
            "• Custom pair requests\n"
            "• Portfolio risk allocation\n"
            "• 1-on-1 direct support\n\n"
            "━━━━━━━━━━━━━━━━━━━\n\n"
            "💳 Pay with USDC on Arc Testnet:\n"
            "<a href='{}'>👉 Open Checkout</a>\n\n"
            "<i>Need testnet USDC? Get it free at faucet.circle.com</i>"
        ).format(url)
        send_message(chat_id, msg)

    # ── /status ──
    elif text == "/status":
        try:
            r = requests.get("{}/status?user_id={}".format(PAYMENT_API, user_id), timeout=5)
            data = r.json()
            tier_name = data.get("tier_name", "Free")
            is_paid = data.get("is_paid", False)
            expires = data.get("expires_at", "")
            signals_today = data.get("signals_today", 0)
            daily_limit = data.get("daily_limit", 2)

            if is_paid:
                exp_str = expires[:10] if expires else "—"
                msg = (
                    "📊 <b>Your Plan: {}</b>\n\n"
                    "• Signals: <b>Unlimited</b>\n"
                    "• Expires: <b>{}</b>\n"
                    "• Total paid: <b>{} USDC</b>\n\n"
                    "✅ All signals are active."
                ).format(tier_name, exp_str, data.get("total_paid_usdc", 0))
            else:
                remaining = max(0, daily_limit - signals_today) if daily_limit else 0
                msg = (
                    "📊 <b>Your Plan: Free</b>\n\n"
                    "• Signals today: <b>{} of {}</b>\n"
                    "• Remaining: <b>{}</b>\n\n"
                    "⚡ /subscribe to upgrade for unlimited signals"
                ).format(signals_today, daily_limit, remaining)
            send_message(chat_id, msg)
        except Exception as e:
            send_message(chat_id, "❌ Could not check status. Try again in a moment.")
            print("Status error: {}".format(e))

    # ── /pairs ──
    elif text == "/pairs":
        plan = check_user_plan(user_id)
        tier = plan.get("tier", 0)

        if tier >= 2:
            pairs_msg = (
                "📈 <b>Your Pairs — All Unlocked</b>\n\n"
                "<b>Tier 1 (Forex):</b>\n"
                "XAUUSD · EURJPY · USDJPY · EURUSD\n"
                "GBPJPY · GBPNZD · NZDCAD\n\n"
                "<b>Tier 2 (Forex):</b>\n"
                "XAGUSD · EURCHF · GBPUSD · USDCAD\n"
                "EURNZD · GBPCAD · GBPAUD · CADJPY\n"
                "EURCAD · AUDUSD · NZDUSD\n\n"
                "<b>Crypto:</b>\n"
                "BTCUSD · ETHUSD · SOLUSD · ADAUSD\n"
                "BNBUSD · ZECUSD · MNTUSD · HYPEUSD\n\n"
                "✅ You receive ALL signals on ALL pairs."
            )
        elif tier == 1:
            pairs_msg = (
                "📈 <b>Your Pairs — Pro</b>\n\n"
                "<b>Tier 1 (Forex):</b>\n"
                "XAUUSD · EURJPY · USDJPY · EURUSD\n"
                "GBPJPY · GBPNZD · NZDCAD\n\n"
                "<b>Crypto:</b>\n"
                "BTCUSD · ETHUSD · SOLUSD · ADAUSD\n"
                "BNBUSD · ZECUSD · MNTUSD\n\n"
                "🔒 Tier 2 pairs locked — /subscribe to upgrade to Elite"
            )
        else:
            pairs_msg = (
                "📈 <b>Your Pairs — Free</b>\n\n"
                "You receive signals on <b>2 random profitable pairs</b>\n"
                "(1 forex + 1 crypto, rotates weekly)\n\n"
                "⚡ /subscribe to unlock all pairs"
            )
        send_message(chat_id, pairs_msg)

    # ── /help ──
    elif text == "/help":
        send_message(chat_id,
            "📋 <b>Cmvng SignalVault — Commands</b>\n\n"
            "/start — Welcome & register\n"
            "/subscribe — View plans & upgrade\n"
            "/status — Check your subscription\n"
            "/pairs — See your accessible pairs\n"
            "/help — This message\n\n"
            "Signals are delivered automatically based on your plan."
        )

    # ── Unknown command ──
    elif text.startswith("/"):
        send_message(chat_id, "Unknown command. Try /help")

    return "ok"

# ─── Broadcast Endpoint (your existing bot calls this) ────────
#
# When your existing bot fires a signal, it also calls:
#   POST /broadcast
#   {
#     "message": "<the full signal message in HTML>",
#     "pair": "XAUUSD",
#     "category": "Tier 1",
#     "direction": "BUY"
#   }
#
# This endpoint then sends it to every registered user
# who is allowed to receive it based on their plan.

@app.route("/broadcast", methods=["POST"])
def broadcast():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message"}), 400

    message = data["message"]
    pair = data.get("pair", "")
    category = data.get("category", "")

    users = load_users()
    sent_count = 0
    skipped_count = 0

    for user_id in users:
        try:
            # Check if user can receive signals
            plan = check_user_plan(user_id)

            if not plan.get("allowed", False):
                skipped_count += 1
                continue

            # Send the signal
            send_message(int(user_id), message)
            mark_signal_sent(user_id)
            sent_count += 1

            # If free user just hit their limit, notify them
            remaining = plan.get("remaining")
            if remaining is not None and remaining <= 1:
                send_message(int(user_id),
                    "━━━━━━━━━━━━━━━━━━━\n"
                    "⏸️ <b>That's your last free signal for today.</b>\n\n"
                    "Upgrade for unlimited signals on all pairs.\n"
                    "→ /subscribe\n"
                    "━━━━━━━━━━━━━━━━━━━"
                )

        except Exception as e:
            print("Broadcast error for {}: {}".format(user_id, e))

    print("Broadcast: sent to {}, skipped {} (limit reached)".format(sent_count, skipped_count))
    return jsonify({"ok": True, "sent": sent_count, "skipped": skipped_count})

# ─── Notify Endpoint (checkout page calls this after payment) ─

@app.route("/notify", methods=["POST"])
def notify_payment():
    data = request.get_json()
    if not data or "user_id" not in data:
        return jsonify({"error": "No user_id"}), 400

    user_id = data["user_id"]
    tier_name = data.get("tier_name", "Pro")
    amount = data.get("amount", 0)
    tx_hash = data.get("tx_hash", "")

    tx_short = tx_hash[:10] + "..." if len(tx_hash) > 10 else tx_hash
    tx_link = "https://testnet.arcscan.app/tx/{}".format(tx_hash) if tx_hash else ""

    msg = (
        "✅ <b>Payment Confirmed!</b>\n\n"
        "Your <b>{}</b> plan is now active.\n\n"
        "• Amount: <b>{} USDC</b>\n"
        "• Network: Arc Testnet\n"
        "• Signals: <b>Unlimited</b>\n"
        "• Expires: <b>30 days from now</b>\n"
    ).format(tier_name, amount)

    if tx_link:
        msg += "\n🔗 <a href='{}'>View transaction on ArcScan</a>\n".format(tx_link)

    msg += "\nYour signals are now flowing. Trade well. 📈"

    send_message(int(user_id), msg)
    return jsonify({"ok": True})

# ─── Health Check ─────────────────────────────────────────────

@app.route("/")
def index():
    users = load_users()
    return jsonify({
        "service": "Cmvng SignalVault Companion Bot",
        "status": "running",
        "registered_users": len(users),
        "endpoints": [
            "POST /telegram — Telegram webhook",
            "POST /broadcast — Send signal to all eligible users",
            "GET  /users — List registered users",
        ]
    })

@app.route("/users")
def list_users():
    users = load_users()
    return jsonify({"count": len(users), "users": users})

# ─── Telegram Webhook Setup ──────────────────────────────────
# Call this once to tell Telegram where to send messages

@app.route("/setup-webhook")
def setup_webhook():
    """Visit this URL once after deploying to set up the Telegram webhook"""
    bot_url = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "")
    if not bot_url:
        return jsonify({"error": "Set RAILWAY_PUBLIC_DOMAIN in variables first"})

    webhook_url = "https://{}/telegram".format(bot_url)
    url = "https://api.telegram.org/bot{}/setWebhook?url={}".format(
        COMPANION_BOT_TOKEN, webhook_url)

    try:
        r = requests.get(url, timeout=10)
        result = r.json()
        return jsonify({
            "webhook_url": webhook_url,
            "telegram_response": result
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# ─── Start ────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("")
    print("╔════════════════════════════════════════════╗")
    print("║  Cmvng SignalVault — Companion Bot          ║")
    print("║  Running on port {}                      ║".format(port))
    print("╚════════════════════════════════════════════╝")
    print("")
    app.run(host="0.0.0.0", port=port)
