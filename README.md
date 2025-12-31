Bài toán dự đoán tình trạng sức khỏe dựa trên chỉ số sức khỏe toàn diện và lối sống
Bộ dữ liệu này được thiết kế để mô phỏng và phân tích mối quan hệ giữa các thói quen lối sống hàng ngày (như tập thể dục, giấc ngủ, dinh dưỡng) và chỉ số sức khỏe tổng thể. Nó rất hữu ích cho các bài toán Hồi quy (Regression), Phân loại (Classification) hoặc Phân tích dữ liệu khám phá (EDA)
Link Dataset: https://www.kaggle.com/datasets/miadul/holistic-health-and-lifestyle-score-dataset/data
Nguồn: Kaggle
Gồm 11 cột dữ liệu
*   Physical_Activity: Số phút hoạt động thể chất
*   Nutrition_Score: Điểm dinh dưỡng
*   Strees_Level: Mức độ căng thẳng
*   Mindfulness: Thời gian dành chánh niệm
*   Sleep_Hours: Số giờ ngủ trung bình mỗi đêm
*   Hydration: Lít nước tiêu thụ mỗi ngày (0,5–5,0)
*   BMI: Chỉ số khối cơ thể (18–40)
*   Alcohol: Đơn vị rượu mỗi tuần (0–20)
*   Smoking: Thuốc lá mỗi ngày (0–30)
*   Overall_Health_Score: Điểm số sức khỏe
*   Health_Status: Trạng thái sức khỏe
Tiền xử lý bao gồm : Xử lý dữ liệu mất cân bằng, Chuẩn hóa dữ liệu continuous
B1: Chia dữ liệu cho tập train và test (80% train, 20% test)
B2: Áp dụng chuẩn hóa StandardScaler()
B3: Áp dụng SMOTE() xử lý dữ liệu mất cân bằng
Mô hình sử dụng mô hình RandomForest và SVM
Lý do chọn mô hình: Hai mô hình đều xử lý tốt cho bài toán Multiclass classification
Kết quả:
    RF (chưa áp dụng SMOTE()):
                  precision    recall  f1-score
        Average    0.84      0.84      0.84
        Good       0.94      0.97      0.95
        Poor       0.94      0.43      0.59
    RF (áp dụng SMOTE()):
                  precision    recall  f1-score
        Average    0.83      0.89      0.86  
        Good       0.97      0.94      0.95      
        Poor       0.79      0.74      0.76
    SVM (áp dụng SMOTE()):
                 precision    recall  f1-score
        Average    0.97      0.99      0.98      
        Good       1.00      0.99      0.99     
        Poor       0.94      1.00      0.97      
    SVM (chưa áp dụng SMOTE()):
                 precision    recall  f1-score
        Average    0.99      1.00      0.99     
        Good       1.00      1.00      1.00
        Poor       1.00      0.97      0.99      
Cách chạy train: vào ./app/BTL_ML.ipynb sau đó nhấn Run All
Cách chạy demo: trên terminal ta nhập " cd demo" sau đó nhập tiếp "streamlit run demo.py"
TÁC GIẢ: Nguyễn Quốc Bảo, 10123033, 12423TN
