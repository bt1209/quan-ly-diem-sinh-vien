
import streamlit as st
import pandas as pd

# =========================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# =========================
# 2. DỮ LIỆU 10 SINH VIÊN
# =========================
data = {
    "Họ tên": [
        "Nguyễn Minh Anh",
        "Trần Hoàng Nam",
        "Lê Thu Hà",
        "Phạm Gia Huy",
        "Võ Ngọc Mai",
        "Đặng Quốc Bảo",
        "Bùi Khánh Linh",
        "Đỗ Thành Đạt",
        "Hoàng Yến Nhi",
        "Phan Đức Minh"
    ],
    "Chuyên cần": [9.0, 8.0, 10.0, 7.0, 9.0, 6.0, 8.5, 9.0, 7.5, 8.0],
    "Giữa kỳ": [8.5, 7.0, 9.0, 6.5, 8.0, 5.5, 8.0, 9.5, 7.0, 8.5],
    "Cuối kỳ": [9.0, 7.5, 9.5, 7.0, 8.5, 6.0, 8.5, 9.0, 7.5, 9.0]
}

df = pd.DataFrame(data)

# =========================
# 3. TÍNH ĐIỂM TỔNG KẾT
# Công thức mẫu:
# Chuyên cần 10%, giữa kỳ 30%,
# cuối kỳ 60%.
# =========================
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.10
    + df["Giữa kỳ"] * 0.30
    + df["Cuối kỳ"] * 0.60
).round(2)

# =========================
# 4. XẾP LOẠI SINH VIÊN
# =========================
def xep_loai(diem):
    if diem >= 9:
        return "Xuất sắc"
    elif diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Không đạt"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# =========================
# 5. HIỂN THỊ BẢNG ĐIỂM
# =========================
st.subheader("1. Bảng điểm của 10 sinh viên")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# =========================
# 6. THỐNG KÊ ĐIỂM CỦA LỚP
# =========================
st.subheader("2. Thống kê kết quả học tập")

diem_trung_binh = df["Tổng kết"].mean()
so_sinh_vien_dat = int((df["Tổng kết"] >= 5).sum())

sinh_vien_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sinh_vien_thap_nhat = df.loc[df["Tổng kết"].idxmin()]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Điểm trung bình lớp",
    f"{diem_trung_binh:.2f}"
)

col2.metric(
    "Số sinh viên đạt",
    f"{so_sinh_vien_dat}/{len(df)}"
)

col3.metric(
    "Tổng số sinh viên",
    len(df)
)

col4, col5 = st.columns(2)

with col4:
    st.success(
        f"Điểm cao nhất: {sinh_vien_cao_nhat['Họ tên']} "
        f"({sinh_vien_cao_nhat['Tổng kết']:.2f} điểm)"
    )

with col5:
    st.warning(
        f"Điểm thấp nhất: {sinh_vien_thap_nhat['Họ tên']} "
        f"({sinh_vien_thap_nhat['Tổng kết']:.2f} điểm)"
    )

# =========================
# 7. SELECTBOX TRA CỨU SINH VIÊN
# =========================
st.subheader("3. Tra cứu điểm sinh viên")

ten_sinh_vien = st.selectbox(
    "Chọn một sinh viên:",
    df["Họ tên"].tolist()
)

sinh_vien = df[
    df["Họ tên"] == ten_sinh_vien
].iloc[0]

st.write(f"### Kết quả học tập: {sinh_vien['Họ tên']}")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Chuyên cần",
    f"{sinh_vien['Chuyên cần']:.1f}"
)

c2.metric(
    "Giữa kỳ",
    f"{sinh_vien['Giữa kỳ']:.1f}"
)

c3.metric(
    "Cuối kỳ",
    f"{sinh_vien['Cuối kỳ']:.1f}"
)

c4.metric(
    "Tổng kết",
    f"{sinh_vien['Tổng kết']:.2f}"
)

c5.metric(
    "Xếp loại",
    sinh_vien["Xếp loại"]
)

# =========================
# 8. BIỂU ĐỒ CỘT ĐIỂM TỔNG KẾT
# =========================
st.subheader("4. Biểu đồ cột điểm tổng kết")

chart_data = df.set_index("Họ tên")[["Tổng kết"]]

st.bar_chart(
    chart_data,
    y="Tổng kết",
    use_container_width=True
)

# =========================
# 9. THÔNG TIN NGƯỜI TẠO
# =========================
st.divider()

st.caption(
    "Người tạo ứng dụng: [đào trần bảo thịnh] "
    "| MSSV: [MÃ 068208001475]"
)
