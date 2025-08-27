global _start

_start:
    mov rax, qword [0x404000]
    add qword [0x404000], 0x1337
