# Hệ thống nhận diện thư rác (spam identification system)
- Đây là hệ thống nhận diện thư rác được xây bằng [Streamlit](https://streamlit.io/), khi bạn nhập một văn bản email (tiếng anh) sau đó nhấn nút Predict. Hệ thống sẽ cho qua kết quả Spam (thư rác) hay Not Spam (không phải là thư rác).
- Hệ thống sử dụng model **Random Forest**, được huấn luyện với bộ dữ liệu hơn **4000 dòng**, dữ liệu có **57 đặc trưng** ([xem chi tiết dữ liệu](https://www.openml.org/search?type=data&sort=runs&status=active&id=44)). Model có **Accuracy ≈ 95,5%**.
- Có thể thay thế Model khác bằng cách lưu đồ Model của bạn lại, sau đó thay đổi đường dẫn tới Model của bạn trong file main.py
- Bạn thấy hữu ích cho mình cho 1 Start nhé!! 🐱🐱

## Demo
![Demo GIF](./assists/demo-vid_spam_.gif)

## Cài đặt
1. Tải kho lưu trữ này về
```bash
git clone https://github.com/phanminhtai23/spam-identification.git
cd spam-identification
```
2. Tải các thư viện cần thiết
```bash
pip install -r requirements.txt
```
3. Khởi chạy hệ thống (streamlit run <đường dẫn đến file hệ thống>)
```bash
streamlit run main.py
```


