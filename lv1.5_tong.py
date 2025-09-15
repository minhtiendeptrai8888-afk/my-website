import streamlit as st

st.title("Chào mừng đến với ứng dụng python đầu tiên")

st.header("Ứng dụng này được tạo bởi Tiến. Đây là sản phẩm đầu tay dùng streamlit.")


st.title("Sự khác nhau giữa text và write")

st.text("Đây là text: Chỉ in ra văn bản thôi")

st.write("Đây là write: có thể in đậm **nè** hoặc *nghiêng* luôn")


st.title("Demo Markdown")

st.markdown("### Đây là tiêu đề cấp 3")

st.markdown("- Học python cơ bản\n- Học Streamlit\n- Làm bài tập vui")

st.markdown("Tôi **rất** *thích* lập trình.")

st.markdown("<span style='color:blue'>Dòng này màu xanh dương</span>", unsafe_allow_html=True)


st.title("Hiển thị Code & Công thức")

st.code("""
a = 5
b = 3
hieu = a - b
print("Hiệu là:", hieu)
""", language='python')

st.latex(r"5 - 3 = 2")

st.latex(r"\frac{a+b}{2}")

st.latex(r"\sqrt{16} = 4")


st.title("Thử thách cho bạn")

a = 5
b = 6
c = 7
ket_qua = a * b * c 

st.write("Kết quả:", ket_qua)

st.text("Cảm ơn bạn đã xem app này")

st.markdown("<span style='color:red'>Kết thúc chương trình</span>", unsafe_allow_html=True)

