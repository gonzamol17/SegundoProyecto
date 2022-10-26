import unittest
import xlrd
import time


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Esta parte toma todas las filas y columnas del archivo excel
        path = "/Datos/Users.xlsx"
        inputWorkbook = xlrd.open_workbook(path)
        inputWorksheet = inputWorkbook.sheet_by_index(0)
        row = inputWorksheet.nrows
        col = inputWorksheet.ncols
        print("\n")
        print("números de filas: "+str(row))
        print("números de columnas: "+str(col))
        # con esto imprimo el valor de la fila 2, columna 1
        print(inputWorksheet.cell_value(1, 1))
        print(inputWorksheet.cell_value(1, 2))


if __name__ == '__main__':
    unittest.main()
