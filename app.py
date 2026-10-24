import streamlit as st
import re

st.set_page_config(
    page_title="SafeCall AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ SafeCall AI")
st.subheader("Phát hiện dấu hiệu lừa đảo trực tuyến")

message = st.text_area(
    "Dán tin nhắn cần kiểm tra:",
    placeholder="Ví dụ: Tài khoản bị khóa, cung cấp OTP ngay..."
)

def analyze_message(text):
    rules = {
        "Yêu cầu mã OTP hoặc mật khẩu":
            r"\botp\b|mật khẩu|mã xác minh",
        "Đe dọa khóa tài khoản":
            r"khóa tài khoản|bị khóa|ngừng hoạt động",
        "Thúc giục hành động":
            r"ngay lập tức|khẩn cấp|ngay",
        "Có đường link":
            r"https?://|www\."
    }

    found = []
    for name, pattern in rules.items():
        if re.search(pattern, text, re.IGNORECASE):
            found.append(name)

    return found

if st.button("Phân tích tin nhắn"):
    if not message.strip():
        st.info("M hãy nhập tin nhắn trước nhé.")
    else:
        signs = analyze_message(message)

        if signs:
            st.error("Phát hiện một số dấu hiệu đáng ngờ!")
            for sign in signs:
                st.write("- " + sign)
            st.write("Số dấu hiệu phát hiện:", len(signs))
        else:
            st.success(
                "Chưa phát hiện dấu hiệu theo các quy tắc hiện có."
            )

        st.caption(
            "Đây là bộ quy tắc từ khóa, chưa phải mô hình AI "
            "được huấn luyện. Tin nhắn lừa đảo vẫn có thể lọt qua."
)
st.divider()
st.header("🎥 Phân tích video bằng AI")

video = st.file_uploader(
    "Tải video cần kiểm tra lên",
    type=["mp4", "mov", "avi", "webm"]
)

if video is not None:
    st.video(video)

    st.info(
        "Video đã được tải lên. "
        "Chức năng phân tích nội dung video "
        "bằng AI sẽ được tích hợp ở bước tiếp theo."
    )
