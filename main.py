import streamlit as st
from datetime import datetime

# ページのタイトルを設定する
st.set_page_config(page_title="掲示板アプリ")

# ページにタイトルを表示する
st.title("掲示板アプリ")

# メッセージを入力するテキストボックスを表示する
message = st.text_area("メッセージを入力してください")

# メッセージを保存するリスト
messages = []

# 「投稿する」ボタンがクリックされた場合に実行される処理
if st.button("投稿する"):
    # メッセージが入力されている場合は、掲示板に投稿する
    if message:
        messages.append({
            "id": len(messages) + 1,
            "date": datetime.now(),
            "message": message
        })
        st.success("メッセージを投稿しました。")
    # メッセージが入力されていない場合は、エラーメッセージを表示する
    else:
        st.error("メッセージが入力されていません。")

# メッセージを表示する
if messages:
    st.write("----- メッセージ一覧 -----")
    sorted_messages = sorted(messages, key=lambda x: x["date"], reverse=True)
    for i, message in enumerate(sorted_messages):
        st.write(f"{i+1}. ID:{message['id']} / 日付:{message['date'].strftime('%Y-%m-%d %H:%M:%S')} / メッセージ:{message['message']}")
else:
    st.write("投稿されたメッセージはありません。")
