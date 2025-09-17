import streamlit as st

st.title("Ứng dụng tương tác - Profile & Điểm")

st.write("Ứng dụng nhỏ giúp luyện tập text_input, number_input, selectbox và slider")


name = st.text_input("Nhập tên của bạn:")
age = st.number_input("Nhập tuổi của bạn:", min_value=0, max_value=120, value=16)

subject = st.selectbox("Chọn môn học yêu thích:", ["Toán", "Văn", "Anh", "Tin"])

score = st.slider("Chọn điểm kiểm tra (0 - 10)", min_value=0.0, max_value=10.0, value=7.5)

if st.button("Xem kết quả"):
    if name:
        st.write("Xin chào!", name)
    else:
        st.write("Xin chào! Bạn chưa nhập tên")
    st.write("Bạn", age, "tuổi, thích môn", subject, "và điểm kiểm tra là:", score)

    if score >= 8.0:
        st.write("Giỏi quá!")
    elif score >= 5.0 and score < 8.0:
        st.write("Ổn rồi, cố gắng thêm nhé")
    elif score < 5.0:
        st.write("Cố lên nhé! Mình tin bạn làm được")

    if age < 18:
        st.write("Bạn là học sinh nhé!")
    elif age >= 18:
        st.write("Chúc bạn học tốt làm tốt!")

    st.markdown("<span style='color:blue'>Giỏi quá!</span>", unsafe_allow_html=True)
    st.markdown("<span style='color:red'>Cố lên nhé!</span>", unsafe_allow_html=True)