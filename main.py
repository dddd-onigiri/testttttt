import streamlit as st

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
        messages.append(message)
        st.success("メッセージを投稿しました。")
    # メッセージが入力されていない場合は、エラーメッセージを表示する
    else:
        st.error("メッセージが入力されていません。")

# メッセージを表示する
if messages:
    st.write("----- メッセージ一覧 -----")
    for i, message in enumerate(messages):
        st.write(f"{i+1}. {message}")
else:
    st.write("投稿されたメッセージはありません。")