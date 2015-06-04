# Taller 2 - Solución
*03-Jun-2015*

## Lotería

1. Escriba  un script de `bash` llamado `loteria.sh` que determine si su taller es afortunado y va a ser revisado. La información necesaria siempre va a estar en el momento adecuado en el archivo [lottery](https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesLaboratorio/master/2015-V/actividades/lottery/lottery.csv). Además de imprimir si el taller va a ser o no revisado también se debe imprimir la primera línea del archivo `csv` que tiene la fecha. Guárdelo en la carpeta de ejecutables de su computador.

```shell
curl -s https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesLaboratorio/master/2015-V/actividades/lottery/lottery.csv > lottery.csv 
head -1 lottery.csv
awk -F"," '{if ($1==cod) print $2}' lottery.csv
rm lottery.csv
```
## Expresiones Regulares

1. Descargue el [archivo](http://www.minhacienda.gov.co/portal/page/portal/HomeMinhacienda/presupuestogeneraldelanacion/ProyectoPGN/2015/Presentacion%20Proyecto%202015.pdf) del Ministerio de Hacienda con información sobre el Presupuesto General de la Nación 2015. Abra el archivo, diríjase a la página 10, haga *copy-paste* los datos de la tabla comenzando en *EDUCACIÓN* y terminando en *100,0*, guárdelos en un archivo llamado `pgn.dat`. Escriba comandos de `sed` que lleven a cabo las siguientes tareas de búsqueda y reemplazo y aplíquelos secuencialmente sobre el archivo `pgn.dat`: 

	* eliminar todos los puntos,

	* cambiar por puntos todas las comas que estén seguidas de algún dígito,

	* cambiar por `tab` todos los espacios en blanco que estén seguidos de algún dígito o por (,

	* eliminar todos los paréntesis derechos,

	* y por último cambiar todos los paréntesis izquierdos por -. El resultado final debe quedar guardado en el archivo `pgn.tsv`.

	* Finalmente usar `sort --field-separator=$'\t' ...`  y `head` para organizar el archivo de acuerdo al cambio porcentual y encontrar el sector con el menor cambio porcentual.

```shell
sed 's/\.//g' pgn.dat | sed 's/,([0-9])/.\1/g' | sed -E 's/ ([0-9]|\()/   \1/g' | sed 's/\)//g' | sed 's/\(/-/g' > pgn.tsv
sort --field-separator=$'\t' --key=4 -n pgn.tsv | head -1
```

## gnuplot

1. Haga con [Saturno](http://nssdc.gsfc.nasa.gov/planetary/factsheet/saturniansatfact.html) lo mismo que hicimos con Júpiter: limpiar el archivo llevándolo a formato `csv` y hacer una gráfica con `gnuplot` que evalúe la tercera ley de Kepler. Hay que tener especial cuidado con la columna para el periodo de rotación.

```shell
sed 's/\(.*\)//g' saturnsatellites.dat | sed 's/^ +//g' | sed 's/ +$//g' | sed 's/,//g' | sed 's/.*Satellites.*//g' | sed '/^$/d' | sed 's/([0-9]) {17}/\1 NA/g' | sed 's/ +/,/g' | sed 's/R,/,/g' > saturnsatellites.csv
gnuplot << EOF
	set datafile separator ","
	quad(x) = x**2
	cube(x) = x**3
	set xlabel "a^3 / SR^3"
	set ylabel "T^2 / days^2"
	unset key
	set title "Kepler's third on Saturn"
	plot "saturnsatellites.csv" using (cube(\$3)):(quad(\$4))
EOF
```