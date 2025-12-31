# import streamlit as st
# import pandas as pd
# import joblib

# # Cấu hình Ứng dụng
# st.set_page_config(page_title="Demo Model SVM", layout="centered")

# # Tải Mô hình và các thành phần tiền xử lý
# model = joblib.load('svm.pkl')
# scaler = joblib.load('scaler.pkl')

# # Xây dựng Giao diện Người dùng (Input Sidebar)
# st.title('Ứng dụng dự đoán tình trạng sức khỏe toàn diện sử dụng SVM')
# st.markdown('### Nhập dữ liệu dự đoán')


# Physical_Activity = st.sidebar.slider(
#     'Physical_Activity (Hoạt động thể chất)', 
#     min_value=0, max_value=120, value=60
# )
# Nutrition_Score = st.sidebar.slider(
#     'Nutrition_Score (Điểm dinh dưỡng)', 
#     min_value=0, max_value=10, value=5
# )

# Stress_Level = st.sidebar.slider(
#     'Strees_Level (Mức độ căng thẳng)', 
#     min_value=0, max_value=10, value=5
# )

# Mindfulness = st.sidebar.slider(
#     'Mindfulness (Thời gian dành chánh niệm)', 
#     min_value=0, max_value=55, value=25
# )

# Sleep_Hours = st.sidebar.slider(
#     'Sleep_Hours (Số giờ ngủ trung bình mỗi đêm)', 
#     min_value=0, max_value=10, value=5
# )


# Hydration = st.sidebar.slider(
#     'Hydration (Lít nước tiêu thụ mỗi ngày)', 
#     min_value=0, max_value=10, value=5
# )
# Alcohol = st.sidebar.slider(
#     'Alcohol (Đơn vị rượu mỗi tuần)', 
#     min_value=0, max_value=20, value=5
# )
# bmi = st.sidebar.slider(
#     'BMI (Chỉ số khối cơ thể)', 
#     min_value=0, max_value=40, value=5
# )
# Smoking = st.sidebar.slider(
#     'Smoking (Số điếu thuốc mỗi ngày)', 
#     min_value=0, max_value=30, value=5
# )

# st.sidebar.markdown('---')
# st.sidebar.subheader('Dữ liệu Phân loại & Nhị phân')


# if st.button('Dự đoán sức khỏe toàn diện'):
    
#     # Tạo DataFrame từ đầu vào
#     data = {
#         'Physical_Activity': Physical_Activity,
#         'Nutrition_Score': Nutrition_Score,
#         'Stress_Level': Stress_Level,
#         'Mindfulness': Mindfulness,
#         'Sleep_Hours': Sleep_Hours,
#         'Hydration': Hydration,
#         'Alcohol': Alcohol,
#         'BMI': bmi,
#         'Smoking': Smoking
#     }
    
#     input_df = pd.DataFrame([data])
    
#     st.subheader('Dữ liệu sức khỏe toàn diện đã nhập')
#     st.dataframe(input_df, hide_index=True)

#     # Chuẩn hóa (Scaling) dữ liệu số liệu
#     numerical_cols = ['Physical_Activity','Nutrition_Score','Stress_Level','Mindfulness','Sleep_Hours','Hydration','BMI','Alcohol','Smoking']
#     df_num_raw = input_df[numerical_cols]
#     scaled_data = scaler.transform(df_num_raw)
#     df_num_scaled = pd.DataFrame(scaled_data, columns=numerical_cols)


#     features = df_num_scaled.values 
        
#     # Dự đoán xác suất
#     predict = model.predict(features)

#     st.markdown('---')
#     st.subheader(f'Kết quả dự đoán: {predict}')


import streamlit as st
import pandas as pd
import joblib

# Cấu hình ứng dụng
st.set_page_config(page_title="Demo Model SVM", layout="centered")

# Tải mô hình và scaler
model = joblib.load('svm.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Ứng dụng Dự đoán Sức khỏe Toàn diện sử dụng SVM")


with st.sidebar:
    st.header("Nhập thông tin sức khỏe")
    st.markdown("Chỉnh các thanh trượt bên dưới:")

    Physical_Activity = st.slider(
        'Hoạt động thể chất (phút/ngày)', min_value=0, max_value=120, value=60
    )
    Nutrition_Score = st.slider(
        'Điểm dinh dưỡng (0–10)', min_value=0, max_value=10, value=5
    )
    Stress_Level = st.slider(
        'Mức độ căng thẳng (0–10)', min_value=0, max_value=10, value=5
    )
    Mindfulness = st.slider(
        'Thời gian chánh niệm (phút/ngày)', min_value=0, max_value=55, value=25
    )
    Sleep_Hours = st.slider(
        'Giờ ngủ trung bình (giờ/đêm)', min_value=0, max_value=10, value=7
    )
    Hydration = st.slider(
        'Nước tiêu thụ (lít/ngày)', min_value=0, max_value=10, value=2
    )
    Alcohol = st.slider(
        'Rượu bia (đơn vị/tuần)', min_value=0, max_value=20, value=2
    )
    bmi = st.slider(
        'BMI (Chỉ số khối cơ thể)', min_value=0, max_value=40, value=22
    )
    Smoking = st.slider(
        'Số điếu thuốc (điếu/ngày)', min_value=0, max_value=30, value=0
    )

    st.markdown("---")


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button(" Dự đoán Sức khỏe Toàn diện")

if predict_button:
    data = {
        'Physical_Activity': Physical_Activity,
        'Nutrition_Score': Nutrition_Score,
        'Stress_Level': Stress_Level,
        'Mindfulness': Mindfulness,
        'Sleep_Hours': Sleep_Hours,
        'Hydration': Hydration,
        'Alcohol': Alcohol,
        'BMI': bmi,
        'Smoking': Smoking
    }

    input_df = pd.DataFrame([data])
    numerical_cols = ['Physical_Activity','Nutrition_Score','Stress_Level','Mindfulness','Sleep_Hours','Hydration','BMI','Alcohol','Smoking']
    df_num_raw = input_df[numerical_cols]
    scaled_data = scaler.transform(df_num_raw)
    df_num_scaled = pd.DataFrame(scaled_data, columns=numerical_cols)


    features = df_num_scaled.values 
    predict = model.predict(features)

    st.markdown('---')
    st.subheader(f'Kết quả dự đoán: {predict}')
