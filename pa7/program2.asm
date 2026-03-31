.section .text
main:
    LI s0, 0
    LI s1, 0
l_prompt:
    LA t0, 0x10000000
    PUTS t0
    GETI s0
    LI t5, 0
    BGE t5, s0, l_prompt
l_collatz:
    LI t0, 1
    BGE t0, s0, l_end
    PUTI s0
    LI t0, 2
    DIV t1, s0, t0
    MUL t1, t1, t0
    SUB t1, s0, t1
    LI t5, 0
    BEQ t1, t5, l_even
l_odd:
    LI t0, 3
    MUL s0, s0, t0
    ADDI s0, s0, 1
    ADDI s1, s1, 1
    J l_collatz
l_even:
    LI t0, 2
    DIV s0, s0, t0
    ADDI s1, s1, 1
    J l_collatz
l_end:
    PUTI s0
    PUTI s1
    HALT

.section .strings
0x10000000 "Please enter a positive integer\n"
