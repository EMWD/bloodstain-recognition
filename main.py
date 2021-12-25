
import cv2
import numpy as np
from matplotlib import pyplot as plt
from icecream import ic
from math import sqrt
  
# Читаем картинку
# img = cv2.imread('data/gunshots/Hf73.jpg')
img = cv2.imread('images/shapes_init.png')
# img = cv2.imread('images/test4.jpg')
  
# Делаем картинку чёрно-белой(так надо)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Устанавливаем порог для серой картинки
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
  
# используем findContours() для нахождения контуров
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Длинна контура(контур в данном контексте это контур вокруг одной распозанной фигуры)
# for contour in contours:
#     ic(cv2.arcLength (contour, True ))
# exit(1)

i = 0
# Проходимся по всем контурам(фигурам) и смотрим, что они  из себя представляют
for contour in contours:
  
    # Игнорируем первую фигуру, т.к первая фигура это вся картинка целиком, а все последующие это уже искомые фигуры
    if i == 0:
        i = 1
        continue
  
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
    cv2.drawContours(img, [contour], 0, (0, 255, 0), 5)

    # finding center point of shape
    M = cv2.moments(contour)

    # Тупые локальные вычисления
    ic(approx)

    print('coords of figure------------------')
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
    ic(x, y)
    print('X and Y (center of figure)------------------')

    # Формула герона для вычисления площади треугольника по координатам
    res = abs( (approx[1][0][0]-approx[0][0][0])*(approx[2][0][1]-approx[0][0][1]) - (approx[2][0][0]-approx[0][0][0])*(approx[1][0][1]-approx[0][0][1]) ) / 2
    ic(res)
  
    # Пишем имя фигуры в центре фигуры
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
    elif len(approx) == 4:
        cv2.putText(img, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    else:
        cv2.putText(img, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
cv2.imwrite('images/res.jpg', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()