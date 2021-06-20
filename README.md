# tubes-pcd
Mengukur panjang suatu object dengan menggunakan citra

## keterangan proses pengolahan
- mengubah citra ke grayscale:
  dilakukan secara manual dengan bantuan np.array yang mengalikan nilai RGB suatu citra dengan [0.2989, 0.5870, 0.1140] kemudian dijumlahkan menjadi citra grayscale
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
