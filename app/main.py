import os, threading, time, logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# ── ① ヘルスチェック用エンドポイント ──────────
@app.get("/")
def health():
    return jsonify(status="ok"), 200

# ── ② リール生成ループ ここに既存処理を呼び出す ─
def reel_generator_loop():
    while True:
        try:
            logging.info("▶ リール生成バッチ開始")
            # ★ 既存の reel_auto 処理関数を呼び出す
            # generate_reel()
            logging.info("✅ リール生成バッチ完了")
        except Exception as e:
            logging.exception("❌ リール生成失敗: %s", e)
        time.sleep(30 * 60)        # 30 分ごとに実行

threading.Thread(target=reel_generator_loop, daemon=True).start()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
