import streamlit as st
import pandas as pd
from joblib import load
import re
import os
import time

# os.system('cls')

feature_result = []
dict_features_1To57 = {}

feature_1To48 = ['make', 'address', 'all', '3d', 'our', 'over', 'remove', 'internet', 'order', 'mail', 'receive', 'will', 'people', 'report', 'addresses', 'free', 'business', 'email', 'you', 'credit', 'your', 'font',
                 '000', 'money', 'hp', 'hp1', 'george', '650', 'lab', 'labs', 'telnet', '857', 'data', '415', '85', 'technology', '1999', 'parts', 'pm', 'direct', 'cs', 'meeting', 'original', 'project', 're', 'edu', 'table', 'conference']
feature_49To54 = [';', '(', '[', '!', '$', '#']


def get_bagOfWords(email):
    # Thay thế tất cả các ký tự không phải chữ cái và khoảng trắng bằng khoảng trắng
    cleaned_text = re.sub(r'[^A-Za-z\s]', ' ', email)
    # Tách chuỗi thành các từ
    BagOfWords = cleaned_text.split()
    return BagOfWords


def get_feature(email):
    feature_temp = []
    bag_of_words = get_bagOfWords(email)
    total_words = len(bag_of_words)

    # 1 -> 48
    for element in feature_1To48:
        count_word = email.lower().count(element.lower())
        if total_words == 0:
            calculator = 0
        else:
            calculator = round((float)((count_word/total_words)*100), 2)
        dict_features_1To57['word_freq_' + element] = calculator
        feature_temp.append(calculator)
    # 49 -> 54
    for element in feature_49To54:
        totals_char = len(email)
        count_char = email.lower().count(element.lower())
        calculator = round((float)((count_char/totals_char)*100), 2)
        dict_features_1To57['char_freq_' + element] = calculator
        feature_temp.append(calculator)

    count_upper = 0
    Capital_run_length_longest_56 = 1
    total_length_word_upper = 0
    Capital_run_length_total_57 = 0

    # 55 -> 57
    for word in bag_of_words:
        for char in word:
            if char.isupper():
                Capital_run_length_total_57 += 1  # 57

        if word.isupper():
            count_upper = count_upper + 1
            total_length_word_upper += len(word)
            # 56
            if len(word) > Capital_run_length_longest_56:
                Capital_run_length_longest_56 = len(word)
    # 55
    if count_upper == 0:
        Capital_run_length_average_55 = 1
    else:
        Capital_run_length_average_55 = round(
            (float)(total_length_word_upper/count_upper), 2)

    feature_temp.append(Capital_run_length_average_55)
    feature_temp.append(Capital_run_length_longest_56)
    feature_temp.append(Capital_run_length_total_57)

    dict_features_1To57['Capital_run_length_average'] = Capital_run_length_average_55
    dict_features_1To57['Capital_run_length_longest'] = Capital_run_length_longest_56
    dict_features_1To57['Capital_run_length_total'] = Capital_run_length_total_57

    feature_result.append(feature_temp)

    # for key, value in dict_features_1To57.items():
    #     print(f"{key}: {value}")
    # print(feature_result)

    return dict_features_1To57, feature_result


def show_table_feature(dict_feature):
    data = {}
    # Chuyển dữ liệu thành DataFrame
    df = pd.DataFrame(data)
    for key, value in dict_feature.items():
        df[key] = [value]

    st.markdown("<h2 style='text-align: center;'>The results extracted 57 features 🔍</h2>",
                unsafe_allow_html=True)
    st.dataframe(df)

# Hiển thị kết quả
def showResult(result):
    st.title(
        "------------Predicted Results------------")
    if len(result) == 1:
        if result[0] == '1':
            st.header('→ Spam 😾')
        elif result[0] == '0':
            st.header('→ Not Spam 😸')


# Hàm chính
def main():
    loaded_model = load('Random_Forest.joblib')
    st.markdown("<h1 style='text-align: center;'>SPAM IDENTIFICATION SYSTEM ✉️</h1>",
                unsafe_allow_html=True)
    st.write("Algorithm: **Random Forest**")
    st.markdown(
            "Training Data: [**see here**](https://www.openml.org/search?type=data&sort=runs&status=active&id=44)")

    uploaded_email = st.text_area(
        "Enter the email you want to identify in the box below!", height=200, key="text_area")
    convert_button = st.button("Predict")

    if convert_button:
        if uploaded_email == '':
            st.warning(
                "Please enter the email text in the box to identify spam!"
            )
        else:
            # Bắt đầu đo thời gian
            start_time = time.time()

            # Hiển thị thanh tiến trình
            progress_bar = st.progress(0)
            # Sử dụng st.spinner để hiển thị thông báo đang chạy
            with st.spinner('The model is predicting...'):
                time.sleep(0.5)
                dict, feature = get_feature(uploaded_email)
                progress_bar.progress(30)
                time.sleep(0.5)

                result = loaded_model.predict(feature)
                progress_bar.progress(100)
                time.sleep(0.5)
                st.success('Prediction completed! ✔️')

                show_table_feature(dict)
                showResult(result)

            # Kết thúc đo thời gian
            end_time = time.time()
            execution_time = end_time - start_time
            print("Totals time: ", execution_time)

if __name__ == "__main__":
    main()
