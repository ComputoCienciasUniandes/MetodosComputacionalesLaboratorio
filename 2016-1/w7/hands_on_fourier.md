# Hands-on Fourier
02-03-2016

Vamos a hacer procesamiento de archivos de sonido con la ayuda de la Transformada Discreta de Fourier. 

- Descargue de http://download.wavetlan.com/SVV/Media/HTTP/http-wav.htm el archivo Test 7 (Media Convert Files) y Test 8 (SUPER Files). Escúchelos.
- En un IPython notebook, abra cada archivo como un array de NumPy. Para esto se usa la función read del módulo wavfile de scipy.io. ¿Qué información aparece? ¿Cuántos canales de audio hay?
- Genere un array llamado t que contenga la información temporal del archivo de audio
- Con las funciones fft y fftfreq de scipy.fftpack obtenga y grafique el resultado de la transformada discreta de Fourier sobre el primer canal de audio.
- Filtre las frecuencias superiores a 5000 Hz, y con ayuda de la función ifft de scipy.fftpack, genere un array con la transformada inversa. Con la función write de wavfile cree un nuevo archivo de audio con los resultados de la transformada inversa. Escúchelo.
- Repita el paso anterior, filtrando las frecuencias inferiores a 5000 Hz.