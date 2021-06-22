# Tugas Besar Pengolahan Citra Digital Kel. 1
Mengukur panjang suatu object dengan menggunakan citra dengan menggunakan ukuran benda paling kiri sebagai patokan

## Anggota Kelompok
- Aishiela Ayu Permatasari (11181006)
- Kevin Refinaldi Berlin (11181042)
- Glen Zacharias (11191026)
- Rani Meliyana Putri (11191062)

## Keterangan proses pengolahan
- mengubah citra ke grayscale:
  dilakukan secara manual dengan bantuan np.dot yang mengalikan nilai RGB suatu citra dengan [0.2989, 0.5870, 0.1140] kemudian dijumlahkan menjadi citra grayscale
- menambahkan efek gaussian blur pada citra :
  dilakukan secara manual dengan menggunakan fungsi konvolusi buatan sendiri dan mask dengan kernel size 3 x 3
- mengisi nilai border (ujung) citra yang bernilai 0 efek dari fungsi konvolusi:
  menggunakan fungsi buatan sendiri dengan mengambil nilai array terdekat yang bernilai tidak nol
- edge detection (deteksi tepi):
  masih menggunakan bantuan cv2, dalam proses menggunakan fungsi buatan sendiri
- find contours (kontur) : 
  masih menggunakan bantuan cv2, dalam proses menggunakan fungsi buatan sendiri
- draw dot, line, text :
  menggunakan bantuan cv2

## Screenshots
![image](https://user-images.githubusercontent.com/75470102/122679224-9c695c80-d21c-11eb-8dd2-baf87382094a.png)
![WhatsApp Image 2021-06-20 at 22 27 03 (1)](https://user-images.githubusercontent.com/75470102/122679105-236a0500-d21c-11eb-9d32-cddb646350b5.jpeg)
![WhatsApp Image 2021-06-20 at 22 27 03](https://user-images.githubusercontent.com/75470102/122679106-24029b80-d21c-11eb-846a-6ecb18f95917.jpeg)
