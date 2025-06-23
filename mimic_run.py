from qiling import Qiling
from qiling.const import QL_VERBOSE
import os

def fake_open(ql, addr, pathname_ptr, flags, mode):
    try:
        path = ql.mem.string(pathname_ptr)
        print(f"[FAKE OPEN] '{path}' -> returning dummy fd 3")
    except:
        print("[FAKE OPEN] unreadable path")
    return 3 

def fake_stat(ql, addr, pathname_ptr, statbuf):
    try:
        path = ql.mem.string(pathname_ptr)
        print(f"[FAKE STAT64] '{path}' -> success")
    except:
        print("[FAKE STAT64] unreadable path")
    return 0 

def fake_access(ql, addr, pathname_ptr, mode):
    try:
        path = ql.mem.string(pathname_ptr)
        print(f"[FAKE ACCESS] '{path}' with mode={mode} -> success")
    except:
        print("[FAKE ACCESS] unreadable path")
    return 0  

def fake_connect(ql, addr, sockfd, sockaddr_ptr, addrlen):
    print(f"[FAKE CONNECT] -> pretending socket connected")
    return 0  

def fake_bind(ql, addr, sockfd, sockaddr_ptr, addrlen):
    print(f"[FAKE BIND] -> pretending bind succeeded")
    return 0

def fake_socket(ql, addr, domain, type, protocol):
    print(f"[FAKE SOCKET] socket(domain={domain}, type={type}, protocol={protocol}) = 3")
    return 3  

def fake_ioctl(ql, addr, fd, request, argp):
    print(f"[FAKE IOCTL] ioctl(fd={fd}, request={request}, arg={argp}) = 0")
    return 0

def fake_sleep(ql, addr, req, rem=None):
    print("[FAKE SLEEP] nanosleep skipped")
    return 0

def fake_unlink(ql, addr, pathname_ptr):
    try:
        path = ql.mem.string(pathname_ptr)
        print(f"[FAKE UNLINK] '{path}' -> pretending deleted")
    except:
        print("[FAKE UNLINK] unreadable path")
    return 0

def hook_all(ql, syscall_id, args):
    name = ql.os.resolve_syscall_name(syscall_id)
    print(f"[SYSCALL] {name}({', '.join(str(a) for a in args)})")

def main():
    elf_path = "e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf"
    rootfs_path = "/home/sg/qiling_rootfs/arm_linux"

    ql = Qiling([elf_path], rootfs_path, verbose=QL_VERBOSE.DEFAULT)

    ql.os.set_syscall("open", fake_open)
    ql.os.set_syscall("stat64", fake_stat)
    ql.os.set_syscall("access", fake_access)
    ql.os.set_syscall("connect", fake_connect)
    ql.os.set_syscall("bind", fake_bind)
    ql.os.set_syscall("socket", fake_socket)
    ql.os.set_syscall("ioctl", fake_ioctl)
    ql.os.set_syscall("nanosleep", fake_sleep)
    ql.os.set_syscall("unlink", fake_unlink)

    ql.os.set_syscall("*", hook_all)

    ql.add_fs_mapper("/dev", "/dev")
    ql.add_fs_mapper("/proc", "/proc")
    ql.add_fs_mapper("/etc", "/etc")

    try:
        print("[INFO] Running malware in deception mode...")
        ql.run()
    except Exception as e:
        print(f"[CRASH] Emulation error: {e}")

if __name__ == "__main__":
    main()
