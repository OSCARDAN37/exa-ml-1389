# Reporte de Análisis de Datos - Museos (Pandas)

`Oscar Flores Machine Learning pandas, NC 1389`

## 1. DataFrame Convertido
```text
                  Museo  Salas  Visitantes_anio
0          Antropología     23          2500000
1                Tamayo     12           800000
2               Soumaya     20          1500000
3  Palacio Bellas Artes     15          1200000
4            San Carlos     18           400000
5                Amparo     16           350000
```

## 2.1 Primeras Filas (head)
```text
          Museo  Salas  Visitantes_anio
0  Antropología     23          2500000
1        Tamayo     12           800000
```

## 2.2 Últimas Filas (tail)
```text
        Museo  Salas  Visitantes_anio
4  San Carlos     18           400000
5      Amparo     16           350000
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Museo                str
Salas              int64
Visitantes_anio    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   Museo            6 non-null      str  
 1   Salas            6 non-null      int64
 2   Visitantes_anio  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de 'Salas' y 'Visitantes_anio'
```text
           Salas  Visitantes_anio
count   6.000000     6.000000e+00
mean   17.333333     1.125000e+06
std     3.881580     8.085481e+05
min    12.000000     3.500000e+05
25%    15.250000     5.000000e+05
50%    17.000000     1.000000e+06
75%    19.500000     1.425000e+06
max    23.000000     2.500000e+06
```

## 4. Ordenar Ascendente por Salas
```text
                  Museo  Salas  Visitantes_anio
1                Tamayo     12           800000
3  Palacio Bellas Artes     15          1200000
5                Amparo     16           350000
4            San Carlos     18           400000
2               Soumaya     20          1500000
0          Antropología     23          2500000
```

## 5. Ordenar Descendente por Visitantes por Año
```text
                  Museo  Salas  Visitantes_anio
0          Antropología     23          2500000
2               Soumaya     20          1500000
3  Palacio Bellas Artes     15          1200000
1                Tamayo     12           800000
4            San Carlos     18           400000
5                Amparo     16           350000
```

`Oscar Flores Machine Learning pandas, NC 1389`