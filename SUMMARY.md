# Summary

- Menentukan tujuan perbandingan dokumen (kata, kalimat, atau paragraf).
- Memuat kedua file dokumen sebagai input.
- Melakukan mapping dokumen untuk menyamakan struktur (paragraf ke paragraf).
- Menggunakan library python-docx untuk membaca isi dokumen.
- Mengekstrak teks dari setiap paragraf atau run.
- Melakukan proses perbandingan antar teks yang sudah dipetakan.
- Mengidentifikasi perbedaan (kata hilang, tambahan, atau berubah).
- Menghitung jumlah perbedaan pada tiap dokumen.
- Menyajikan hasil perbandingan dalam bentuk yang mudah dibaca (teks atau laporan).
## Tech Stack

- python-docx (from docx import Document)
    >Digunakan untuk membaca dan memproses file DOCX, termasuk paragraf dan runs, sehingga memudahkan ekstraksi dan mapping struktur dokumen.
- re (Regular Expression)
    >Digunakan untuk pembersihan teks dan pencocokan pola (misalnya normalisasi kata, penghapusan karakter khusus, atau validasi format teks) sebelum proses perbandingan.

- logging
    >Digunakan untuk mencatat proses eksekusi program, error, dan informasi debugging agar lebih mudah melakukan troubleshooting dan monitoring.

- os
> Digunakan untuk mengelola file dan direktori, seperti validasi path dokumen, pengecekan keberadaan file, dan pengelolaan environment sistem.

- time
> Digunakan untuk mengukur waktu eksekusi proses perbandingan dokumen atau memberi jeda (delay) pada proses tertentu jika diperlukan.

## Challenges

Kendala utama yang ditemukan selama proses pengerjaan adalah hasil perbandingan dokumen tidak selalu muncul sesuai harapan. Pada beberapa kasus, dokumen yang dibandingkan tidak menghasilkan output, meskipun struktur kode sudah sesuai. Hal ini kemungkinan disebabkan oleh pendekatan problem solving yang belum optimal, terutama pada proses pemetaan dan pembacaan isi dokumen. Akibatnya, saat program dijalankan, data tidak terbaca dengan baik sehingga hasil perbandingan bernilai None atau dokumen tidak dapat dipindai (scan) secara menyeluruh.

## Solutions

Solusi yang diterapkan untuk mengatasi kendala selama pengembangan program ini adalah dengan menyesuaikan proses perbandingan agar lebih tahan terhadap perbedaan struktur dokumen. Perbandingan dilakukan hanya pada jumlah paragraf yang sejajar menggunakan batas minimum untuk mencegah error, serta ditambahkan try-except pada setiap fungsi agar program tidak gagal saat menemukan format dokumen yang tidak konsisten. Nilai properti dokumen yang bernilai None, seperti line spacing dan indent, ditangani dengan pengecekan kondisi dan pemberian nilai default agar tetap dapat diproses. Selain itu, deteksi bullet dan numbering dilakukan menggunakan regular expression langsung dari teks paragraf, dan perbedaan efek cetak (bold, italic, underline) dianalisis pada level run untuk memastikan hasil perbandingan lebih akurat.

## Blockers

Tugas yang belum dapat diselesaikan hingga saat ini adalah pendeteksian typo pada dokumen. Hal ini terjadi karena proses analisis kata membutuhkan pendekatan yang berbeda dibandingkan perbandingan format dokumen, seperti tokenisasi teks, pengelolaan tanda baca, serta penyelarasan jumlah dan posisi kata antar dokumen. Selain itu, perbedaan struktur kalimat dan pengulangan kata pada dokumen menyebabkan hasil perbandingan menjadi tidak akurat, sehingga fitur deteksi typo belum dapat diimplementasikan secara stabil dan konsisten pada tahap pengembangan saat ini.
