.model small
.stack 100h

.data
    msg db 'Hello, World!', '$'     ; MASM strings must end with a '$'

.code
main proc
    ; Initialize data segment
    mov ax, @data
    mov ds, ax

    ; Display the string using DOS interrupt
    mov ah, 09h                     ; Function 09h displays a string
    lea dx, msg                     ; Load address of the string
    int 21h                         ; Call DOS interrupt

    ; Exit program
    mov ah, 4Ch                     ; Function 4Ch terminates program
    int 21h                         ; Call DOS interrupt
main endp
end main
