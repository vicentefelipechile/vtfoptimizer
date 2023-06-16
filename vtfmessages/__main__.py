from messages import *


"""
    Diccionario
"""

CODES: dict = {
    FILE_REDUCE_SIZE: "Reduce el tamaño del archivo (Bajando la resolucion o cambiando el formato a DXT1)",
    FILE_CHANGE_FORMAT: "Cambia el formato del archivo a DXT1 o DXT5",
    FILE_ADD_MIPMAPS: "Añade Mipmaps a la textura para reducir la carga de CPU",
    FILE_REDUCE_RESOLUTION: "La resolucion puede ser demasiado grande para la textura, cambialo a resolucion 1024x1024 o 512x512",
    FILE_REMOVE_BUMPMAP: "Elimina el Bumpmap del vmt para aumentar el rendimiento de la CPU",
    FILE_REMOVE_ENVMAP: "Elimina el Envmap para aumentar el rendimiento de la CPU",

    TOO_HEAVY: "El archivo pesa demasiado, lo recomendable es que pese entre 1MB a 5MB, como minimo debe pesar 10MB",
    TOO_MANY_FILES: "La carpeta contiene demasiadas texturas o archivos vmt",
    TOO_MANY_UNUSED_FILES: "La carpeta contiene demasiados archivos sin utilizar en los VMT",
    TOO_MANY_PARAMETERS: "El archivo VMT tiene demasiados parametros para la textura",
    TOO_MANY_UNUSED_PARAMETERS: "El archivo VMT tiene muchos parametros sin utilizar"
}