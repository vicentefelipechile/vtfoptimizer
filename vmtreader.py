import os


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
    
    AllVMTFiles = []
    
    for cwd, carpetas, _ in os.walk(path):
        for carpeta in carpetas:
            subcarpeta = os.path.join(cwd, carpeta)
            files = GetAllVMTFiles(subcarpeta)
            AllVMTFiles.extend(files)

        vmt_files = GetVMTFiles(cwd)
        AllVMTFiles.extend(vmt_files)

    return AllVMTFiles