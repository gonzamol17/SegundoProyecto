# SegundoProyecto
para ejecutar un test por consola:
1) pytest -v -s nombredelTest.py
2) pytest nombredelTest.py -v -s --html=nombredelreporte.html
3) Estando parado sobre el path del proyecto ejecuto:
python -m pytest (esto ejecuta todos los test)
4) sino python -m pytest -k "sanity" (solo ejecuta
los test que tengan el tag Sanity
5) sino en el path general del proyecto
y escribo pytest test o sino pytest -v "Test"
ese último es el nombre del test o del directorio donde 
están todos los test cases