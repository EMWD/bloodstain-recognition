import cv2

# Читаем искомую картинку
img = cv2.imread('data/gunshots/gs_5.jpg')

# Делаем картинку чёрно-белой(так надо)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Устанавливаем порог для серой картинки
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# используем findContours() для нахождения контуров
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
_centers = []
# Проходимся по всем контурам(фигурам) и смотрим, что они  из себя представляют
for contour in contours:
    # Игнорируем первую фигуру, т.к первая фигура это вся картинка целиком, а все последующие это уже искомые фигуры
    if i == 0:
        i = 1
        continue

    # Выделяем прямоугольнки
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # cv2.approxPloyDP() Выделяем полный контур(непрмоугольная обводка)
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)

    # Используем drawContours()
    cv2.drawContours(img, [contour], 0, (0, 255, 0), 5)

    # Находим центры
    M = cv2.moments(contour)

    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    _centers.append([x, y])

# Сохраняем картинку
cv2.imwrite('images/res.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
