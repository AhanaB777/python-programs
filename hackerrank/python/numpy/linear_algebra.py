""" Task: Compute determinant of matrix """
import numpy

n = int(input())
a = [list(map(float , input().split())) for _ in range(n)]

print(round(numpy.linalg.det(a),2))