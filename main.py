import vtfmessages
import vmtreader

def PrintMessage(mensaje: str = "Nada"):
    print("====================================================")
    print(f"\t{mensaje}")



vmts = vmtreader.GetAllVMTFiles("G:/Mi unidad/dev/garrysmod/addons/vicente_server_darkrp_v4/materials")

for a in vmts:
    print(a)