import pickle
import streamlit as st
import numpy as np

# Membaca model
model = pickle.load(open('model.sav','rb'))

# Judul web
st.title('Prediksi Perlakuan Pelanggan')
# Input data dengan contoh angka valid untuk pengujian
Age = st.text_input('Age')
Gender = st.text_input('Gender')
Marital_Status = st.text_input('Marital_Status')
Occupation = st.text_input('Occupation')
Monthly_Income = st.text_input('Monthly_Income')
Educational_Qualifications = st.text_input('Educational_Qualifications')
Family_size = st.text_input('Family_size')
Size = st.text_input('Size')
latitude = st.text_input('latitude')
longitude = st.text_input('longitude')
Pin_code = st.text_input('Pin_code')
Output = st.text_input('Output')
Feedback = st.text_input('Feedback')

prediksi_onlinefood = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(Age), float(Gender), float(Marital_Status), float(Occupation),
                  float(Monthly_Income), float(Educational_Qualifications), float(Family_size), float(Size),
                  float(latitude), float(longitude), float(Pin_code), float(Output), float(Feedback)]])
        # Lakukan prediksi
        prediksi = model.predict(inputs)
        
        if prediksi[0] == 1:
            prediksi_onlinefood = 'Yes'
            st.success(prediksi_onlinefood)
        else:
            Prediksi_Perlakuan_Pelanggan = '<span style="color:red">No</span>'
            st.markdown(Prediksi_Perlakuan_Pelanggan, unsafe_allow_html=True)
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")