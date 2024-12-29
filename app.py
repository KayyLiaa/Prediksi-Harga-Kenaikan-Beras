import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve inputs from the form
        i = float(request.form['i'])  # Frekuensi
        p = float(request.form['p'])  # Jumlah
        
        # Validasi input
        if p <= 0:
            raise ValueError("Jumlah (p) harus lebih besar dari nol.")
        
        # Perhitungan
        probabilitas = i / p
        kumulatif = probabilitas  # Dalam contoh ini, kumulatif sederhana
        interval = [0, probabilitas]  # Rentang interval probabilitas
        nilai_acak = random.random()  # Nilai acak antara 0 dan 1
        
        # Prediksi berdasarkan nilai acak
        prediksi = "Terjadi" if nilai_acak <= probabilitas else "Tidak Terjadi"
        
        # Hasil yang dikembalikan
        result = {
            'probabilitas': f"{probabilitas:.2f}",
            'kumulatif': f"{kumulatif:.2f}",
            'interval': f"[0, {probabilitas:.2f}]",
            'nilai_acak': f"{nilai_acak:.2f}",
            'prediksi': prediksi
        }
        
        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
