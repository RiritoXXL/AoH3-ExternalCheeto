import pymem as p
import ctypes
import pymem.process as proc

def Main():
    plap_aoh3 = p.Pymem("javaw.exe")
    handle_aoh3_javaw = plap_aoh3.process_handle
    module_handle_jvm = proc.module_from_name(handle_aoh3_javaw, "jvm.dll").lpBaseOfDll # --> This is You're Module For JVM(Java Virtual Machine) :D
    read_str = plap_aoh3.read_string(module_handle_jvm  + 0x338)
    print(str(read_str))

if __name__ == "__main__":
    Main()