# 1. Para descargar el archivo con los datos del curso

#	Se usa echo -e para incluir caracteres especiales como \n (newline)
echo -e "Descargar el archivo con los datos\n"
wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv

# 2. Para mostrar los estudiantes de matematicas
echo -e "Estos son los estudiantes de matematicas\n"
grep MATEMA 01_notas.tsv

# 3. Para contar los estudiantes de matematicas
echo -e "\nel curso tiene"
grep MATEMA 01_notas.tsv | wc -l
echo -e "estudiantes de matematicas.\n"

# 4. Para contar el numero de estudiantes de matematicas y que pasaron la materia
echo -e "el curso tiene"
awk '{if($3=="MATEMA" && ($4+$5+$6)>=9) print $0}' 01_notas.tsv | wc -l
echo -e "estudiantes de matematicas y que aprobaron la materia.\n"

# 4. OTRA FORMA Para contar el numero de estudiantes de matematicas y que pasaron la materia
echo -e "el curso tiene"
awk '{if( $4+$5+$6>=9) print $0}' 01_notas.tsv | grep MATEMA | wc -l
echo -e "estudiantes de matematicas y que aprobaron la materia.\n"

# 5. Para borrar el archivo de datos
rm 01_notas.tsv
