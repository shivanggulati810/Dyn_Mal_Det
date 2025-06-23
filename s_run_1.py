from qiling import Qiling
from qiling.const import QL_VERBOSE

malware_path = "/home/sg/Downloads/e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf"
rootfs_path = "/home/sg/qiling_rootfs/arm_linux"

ql = Qiling([malware_path], rootfs_path, verbose=QL_VERBOSE.DEFAULT)
ql.run()

# sg@sg:~/Desktop/Dyn_An$ python3 run_malware_qiling.py 
# [=] 	brk(inp = 0x0) = 0x1f000
# [=] 	uname(buf = 0x7ff3ca68) = 0x0
# [=] 	access(path = 0x47d8f64, mode = 0x0) = -0x1 (EPERM)
# [=] 	mmap2(addr = 0x0, length = 0x3000, prot = 0x3, flags = 0x22, fd = 0xffffffff, pgoffset = 0x0) = 0x90000000
# [=] 	access(path = 0x47d7fb8, mode = 0x4) = -0x1 (EPERM)
# [=] 	open(filename = 0x47d9df0, flags = 0x80000, mode = 0x1) = -0x1 (EPERM)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = 0x0
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = -0x2 (ENOENT)
# [=] 	open(filename = 0x7ff3c5f8, flags = 0x80000, mode = 0x47eb960) = -0x1 (EPERM)
# [=] 	stat64(path = 0x7ff3c5f8, buf_ptr = 0x7ff3c690) = 0x0
# /home/sg/Downloads/e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf: error while loading shared libraries: libc.so.0: cannot open shared object file: Operation not permitted
# [=] 	writev(fd = 0x2, vec = 0x7ff3c4c0, vlen = 0xa) = 0xc2
# [=] 	exit_group(code = 0x7f) = ?
# [x] 	CPU Context:
# [x] 	r0	: 0xfde0
# [x] 	r1	: 0x1
# [x] 	r2	: 0x7ff3c700
# [x] 	r3	: 0x8ce0
# [x] 	r4	: 0x7ff3cfa8
# [x] 	r5	: 0x7ff3cb28
# [x] 	r6	: 0x47d9048
# [x] 	r7	: 0xf8
# [x] 	r8	: 0x7ff3cb40
# [x] 	r9	: 0x47d89bc
# [x] 	r10	: 0x47eb960
# [x] 	r11	: 0x0
# [x] 	r12	: 0x1c150
# [x] 	sp	: 0x7ff3c6f0
# [x] 	lr	: 0x1c0b4
# [x] 	pc	: 0x0
# [x] 	cpsr	: 0x600001d3
# [x] 	c1_c0_2	: 0xf00000
# [x] 	c13_c0_3	: 0x0
# [x] 	fpexc	: 0x40000000
# [x] 	d0	: 0x0
# [x] 	d1	: 0x0
# [x] 	d2	: 0x0
# [x] 	d3	: 0x0
# [x] 	d4	: 0x0
# [x] 	d5	: 0x0
# [x] 	d6	: 0x0
# [x] 	d7	: 0x0
# [x] 	d8	: 0x0
# [x] 	d9	: 0x0
# [x] 	d10	: 0x0
# [x] 	d11	: 0x0
# [x] 	d12	: 0x0
# [x] 	d13	: 0x0
# [x] 	d14	: 0x0
# [x] 	d15	: 0x0
# [x] 	d16	: 0x0
# [x] 	d17	: 0x0
# [x] 	d18	: 0x0
# [x] 	d19	: 0x0
# [x] 	d20	: 0x0
# [x] 	d21	: 0x0
# [x] 	d22	: 0x0
# [x] 	d23	: 0x0
# [x] 	d24	: 0x0
# [x] 	d25	: 0x0
# [x] 	d26	: 0x0
# [x] 	d27	: 0x0
# [x] 	d28	: 0x0
# [x] 	d29	: 0x0
# [x] 	d30	: 0x0
# [x] 	d31	: 0x0
# [x] 	fpscr	: 0x0
# [x] 	q0	: 0x0
# [x] 	q1	: 0x0
# [x] 	q2	: 0x0
# [x] 	q3	: 0x0
# [x] 	q4	: 0x0
# [x] 	q5	: 0x0
# [x] 	q6	: 0x0
# [x] 	q7	: 0x0
# [x] 	q8	: 0x0
# [x] 	q9	: 0x0
# [x] 	q10	: 0x0
# [x] 	q11	: 0x0
# [x] 	q12	: 0x0
# [x] 	q13	: 0x0
# [x] 	q14	: 0x0
# [x] 	q15	: 0x0
# [x] 	s0	: 0x0
# [x] 	s1	: 0x0
# [x] 	s2	: 0x0
# [x] 	s3	: 0x0
# [x] 	s4	: 0x0
# [x] 	s5	: 0x0
# [x] 	s6	: 0x0
# [x] 	s7	: 0x0
# [x] 	s8	: 0x0
# [x] 	s9	: 0x0
# [x] 	s10	: 0x0
# [x] 	s11	: 0x0
# [x] 	s12	: 0x0
# [x] 	s13	: 0x0
# [x] 	s14	: 0x0
# [x] 	s15	: 0x0
# [x] 	s16	: 0x0
# [x] 	s17	: 0x0
# [x] 	s18	: 0x0
# [x] 	s19	: 0x0
# [x] 	s20	: 0x0
# [x] 	s21	: 0x0
# [x] 	s22	: 0x0
# [x] 	s23	: 0x0
# [x] 	s24	: 0x0
# [x] 	s25	: 0x0
# [x] 	s26	: 0x0
# [x] 	s27	: 0x0
# [x] 	s28	: 0x0
# [x] 	s29	: 0x0
# [x] 	s30	: 0x0
# [x] 	s31	: 0x0
# [x] 	PC = 0x00000000 (unreachable)

# [x] 	Memory map:
# [x] 	Start        End          Perm    Label                                                                  Image
# [x] 	0000008000 - 0000014000   r-x     e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf   /home/sg/Downloads/e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf
# [x] 	000001c000 - 000001d000   rw-     e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf   /home/sg/Downloads/e2d97525cffd1220bc5427f25dcc24137a0bcc6fd9a54e60fe94b15eba32eaad.elf
# [x] 	000001d000 - 000001f000   rwx     [hook_mem]                                                             
# [x] 	00047ba000 - 00047db000   r-x     ld-uClibc.so.0                                                         /home/sg/qiling_rootfs/arm_linux/lib/ld-uClibc.so.0
# [x] 	00047ea000 - 00047ec000   rw-     ld-uClibc.so.0                                                         /home/sg/qiling_rootfs/arm_linux/lib/ld-uClibc.so.0
# [x] 	007ff0d000 - 007ff3d000   rwx     [stack]                                                                
# [x] 	0090000000 - 0090003000   rw-     [mmap anonymous]                                                       
# [x] 	00ffff0000 - 00ffff1000   rwx     [arm_traps]                                                            
# Traceback (most recent call last):
#   File "/home/sg/Desktop/Dyn_An/run_malware_qiling.py", line 10, in <module>
#     ql.run()
#     ~~~~~~^^
#   File "/home/sg/.local/lib/python3.13/site-packages/qiling/core.py", line 595, in run
#     self.os.run()
#     ~~~~~~~~~~~^^
#   File "/home/sg/.local/lib/python3.13/site-packages/qiling/os/linux/linux.py", line 184, in run
#     self.ql.emu_start(self.ql.loader.elf_entry, self.exit_point, self.ql.timeout, self.ql.count)
#     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/sg/.local/lib/python3.13/site-packages/qiling/core.py", line 769, in emu_start
#     self.uc.emu_start(begin, end, timeout, count)
#     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/sg/.local/lib/python3.13/site-packages/unicorn/unicorn_py3/unicorn.py", line 766, in emu_start
#     raise UcError(status)
# unicorn.unicorn_py3.unicorn.UcError: Invalid memory fetch (UC_ERR_FETCH_UNMAPPED)
# sg@sg:~/Desktop/Dyn_An$ 

