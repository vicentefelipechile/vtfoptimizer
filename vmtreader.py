import os

def FormatingVMT(ruta_completa, directorio_base):
    ruta_acortada = ruta_completa[len(directorio_base):].lstrip("/")
    return ruta_acortada


def GetVMTFiles(path: str = None) -> list | str:
    if not path:
        return "Error: No se ha especificado un directorio"
        
    if not os.path.isdir(path):
        return "Error: El directorio no es una carpeta"
        
    VMTFiles: list = [ os.path.join(path, archivo).replace("\\", "/")
                        for archivo in os.listdir(path)
                            if archivo.endswith(".vmt") ]

    return VMTFiles


def GetAllVMTFiles(path: str = None) -> list | str:
    if not path:
        return "Error: No se ha especificado un directorio"
        
    if not os.path.isdir(path):
        return "Error: El directorio no es una carpeta"
    
    AllVMTFiles: list = []
    
    for cwd, carpetas, _ in os.walk(path):
        for carpeta in carpetas:
            subcarpeta = os.path.join(cwd, carpeta)
            files = GetAllVMTFiles(subcarpeta)
            print(cwd)

        vmt_files = GetVMTFiles(cwd)
        basefile = [ FormatingVMT( os.path.join(cwd, archivo), path ) for archivo in vmt_files]
        AllVMTFiles.extend(basefile)

    return AllVMTFiles