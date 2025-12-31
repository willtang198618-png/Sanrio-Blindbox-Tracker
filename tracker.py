# -*- coding: utf-8 -*-
"""
Blindbox Market Tracker（链路测试版）
作用：
- 从 GitHub Actions 运行
- 给你的 Telegram 机器人发一条消息
"""

import os
import requests
from datetime import datetime


def send_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    r = requests.post(url, json=payload, timeout=20)
    r.raise_for_status()


def main():
    bot_token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")

    if not bot_token:
        raise RuntimeError("缺少 TG_BOT_TOKEN（GitHub Secrets 未设置）")
    if not chat_id:
        raise RuntimeError("缺少 TG_CHAT_ID（GitHub Secrets 未设置）")

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    message = (
        "✅ Blindbox Tracker 已成功运行\n\n"
        f"时间：{now}\n"
        "状态：Telegram 推送链路已打通\n\n"
        "下一步将接入市场热度数据。"
    )

    send_telegram(bot_token, chat_id, message)


if __name__ == "__main__":
    main()
