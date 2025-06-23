import os
from qiling import Qiling
from qiling.const import QL_VERBOSE, QL_INTERCEPT

def try_read_str(ql, ptr):
    try:
        return ql.mem.string(ptr)
    except:
        return f"(unreadable @ {ptr:#x})"

def fake_open(ql, addr, pathname_ptr, flags, mode):
    path = try_read_str(ql, pathname_ptr)
    print(f"[FAKE OPEN] '{path}' → fd 3")
    return 3

def fake_stat(ql, addr, pathname_ptr, statbuf):
    path = try_read_str(ql, pathname_ptr)
    print(f"[FAKE STAT64] '{path}' → success")
    return 0

def fake_access(ql, addr, pathname_ptr, mode):
    path = try_read_str(ql, pathname_ptr)
    print(f"[FAKE ACCESS] '{path}' with mode={mode} → success")
    return 0

def fake_connect(ql, addr, sockfd, sockaddr_ptr, addrlen):
    print("[FAKE CONNECT] → success")
    return 0

def fake_bind(ql, addr, sockfd, sockaddr_ptr, addrlen):
    print("[FAKE BIND] → success")
    return 0

def fake_socket(ql, addr, domain, type, protocol):
    print(f"[FAKE SOCKET] domain={domain}, type={type} → fd 3")
    return 3

def fake_ioctl(ql, addr, fd, request, argp):
    print(f"[FAKE IOCTL] fd={fd}, req={request} → 0")
    return 0

def fake_sleep(ql, addr, req, rem=None):
    print("[FAKE SLEEP] ignored")
    return 0

def fake_unlink(ql, addr, pathname_ptr):
    path = try_read_str(ql, pathname_ptr)
    print(f"[FAKE UNLINK] '{path}' → 0")
    return 0

def hook_all(ql, syscall_id, args):
    name = ql.os.resolve_syscall_name(syscall_id)
    print(f"[SYSCALL] {name}({', '.join(str(a) for a in args)})")


def main():
    elf = os.path.abspath("e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf")
    rootfs = os.path.expanduser("~/qiling_rootfs/arm_uclibc")

    if not os.path.exists(elf):
        print(f"[ERROR] ELF file not found: {elf}")
        return
    if not os.path.isdir(rootfs):
        print(f"[ERROR] Rootfs not found: {rootfs}")
        return

    ql = Qiling([elf], rootfs, verbose=QL_VERBOSE.DEBUG)

    hooks = {
        "open": fake_open,
        "stat64": fake_stat,
        "access": fake_access,
        "connect": fake_connect,
        "bind": fake_bind,
        "socket": fake_socket,
        "ioctl": fake_ioctl,
        "nanosleep": fake_sleep,
        "unlink": fake_unlink,
    }

    for name, func in hooks.items():
        ql.os.set_syscall(name, func, QL_INTERCEPT.CALL)

    ql.os.set_syscall("*", hook_all, QL_INTERCEPT.CALL)

    def fake_uclibc_main(ql, a, b, c, d, e):
        print("[FAKE SYMBOL] __uClibc_main() → Skipping to user main()")
        return 0

    ql.set_api("__uClibc_main", fake_uclibc_main)

    ql.add_fs_mapper("/dev", "/dev")
    ql.add_fs_mapper("/proc", "/proc")
    ql.add_fs_mapper("/etc", "/etc")

    print(f"[INFO] Running malware in deception mode → {elf}")
    try:
        ql.run()
    except Exception as e:
        print(f"[CRASH] Emulation stopped: {e}")
