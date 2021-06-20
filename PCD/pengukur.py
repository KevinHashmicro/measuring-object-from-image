import cv2
import imutils
import numpy as np
from imutils import contours
from imutils import perspective
from scipy.spatial import distance as dist
from PCD.konvolusi import konvolusi, gaussian, borderFill


def midpoint(titikA, titikB):
    return (titikA[0] + titikB[0]) * 0.5, (titikA[1] + titikB[1]) * 0.5


# memuat citra dan lebar object paling kiri dengan satuan cm
image = cv2.imread("asset/test2.jpg")
width = 2.7

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (7, 7), 0)

# konversi citra ke grayscale
gray = np.around(np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]), 0).astype(int)

# memberikan efek gaussian blur dengan 2 kali perulangan
grayGaussian = konvolusi(gray, gaussian)
grayGaussian = konvolusi(grayGaussian, gaussian)

# mengisi nilai array ujung citra dengan nilai terdekat
# dengan tujuan agar tidak terdeteksi sebagai tepi suatu object
ggfill = borderFill(grayGaussian)

# print(ggfill)

# melakukan deteksi tepi, dilanjutkan dengan dilation + erosion untuk mengecilkan gaps diantara objek
edged = cv2.Canny(ggfill, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)


# mencari kontur pada ujung map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# mengurutkan kontur dari ujung kiri ke kanan
# 'pixels per metric' sebagai patokan
(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

# perulangan pada setiap kontur
hasil = image.copy()
for c in cnts:
    # mengabaikan ukuran kontur yang terlalu besar
    if cv2.contourArea(c) < 100:
        continue

    # menghitung ukuran box dari kontur tersebut
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")

    # mengurutkan titik pada kontur
    box = perspective.order_points(box)
    cv2.drawContours(hasil, [box.astype("int")], -1, (0, 255, 0), 2)

    # perulangan untuk menggambar titik
    for (x, y) in box:
        cv2.circle(hasil, (int(x), int(y)), 5, (0, 0, 255), -1)

    # unpack
    (tl, tr, br, bl) = box

    # menghitung  lebar
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)

    # menghitung  panjang
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)

    # menggambar garis box
    cv2.circle(hasil, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    cv2.circle(hasil, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    cv2.circle(hasil, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    cv2.circle(hasil, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

    # menggambar garis antara titik tengah keempat sisi
    cv2.line(hasil, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
    cv2.line(hasil, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)

    # menghitung jarak Euclidean antara titik tengah
    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

    # jika patokan masih belum ada, maka akan diambil dari inputan lebar diatas
    if pixelsPerMetric is None:
        pixelsPerMetric = dB / width

    # menghitung ukuran objek berdasarkan patokan
    dimA = dA / pixelsPerMetric
    dimB = dB / pixelsPerMetric

    # menggambar text berisi ukuran objek
    cv2.putText(hasil, "{:.2f}cm".format(dimA), (int(tltrX - 15), int(tltrY - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
    cv2.putText(hasil, "{:.2f}cm".format(dimB), (int(trbrX - 150), int(trbrY - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
