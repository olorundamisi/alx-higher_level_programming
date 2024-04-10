#!/usr/bin/python3
# 100-main.py
# Olorundamisi Dunmade <github.com/olorundamisi>

matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

ma = [[5, 6], [7, 8]]
mb = [[5, 6, 1], [7, 8]]
print(matrix_mul(ma, mb))
