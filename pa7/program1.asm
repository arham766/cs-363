.section .text
main:
    LI s0, 0
    LI s1, 0
    GETI s0
    GETI s1
    BGE s0, s1, a_greater_or_equal
a_less:
    LA t3, 0x10000000
    PUTS t3
    J end
a_greater_or_equal:
    BEQ s0, s1, a_equal
a_greater:
    LA t3, 0x10000008
    PUTS t3
    J end
a_equal:
    LA t3, 0x10000004
    PUTS t3
    J end
end:
    HALT

.section .strings
0x10000000 "a is less than b\n"
0x10000004 "a is equal to b\n"
0x10000008 "a is greater than b\n"
