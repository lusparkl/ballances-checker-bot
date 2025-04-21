from bot.webhook_server import app
import os

if __name__ == "__main__":
    print("Webhook server is running...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


