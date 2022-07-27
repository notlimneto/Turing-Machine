# Turing-Machine
This is a Universal Turing Machine I made for my Theory of Computation class.
It receives a binary machine and computes a string according to the given binary machine.

-Beggining and end of the machine: "000"  
-Division of transition rules: "00"

#### Example: Add two unary numbers ####
Unary numbers: 0 -> 1; 1 -> 11; 2 -> 111; 3 -> 1111; ...; n -> 1 n+1 times

B111B111B (2+2) -> B11111BBB (4)  
B1B1B (0+0) -> B1BBB (0)

Turing Machine for execution:
0001011101101110110011011101110110110011011011011011001110111011110111010011101101110110110011110110111110111010011111011011111101110100111111011011111101101000

Turing Machine for comprehension:

00010111011011101100  
110111011101101100  
1101101101101100  
11101110111101110100  
111011011101101100  
111101101111101110100  
11111011011111101110100  
111111011011111101101000  

Non-binary from the example above:

(q0, B)→(q1, B, R)  
(q1, B)→(q2, 1, R)  
(q1, 1)→(q1, 1, R)  
(q2, B)→(q3 , B, L)  
(q2, 1)→(q2, 1, R)

(q3, 1) →(q4 , B, L)

(q4,1)→(q5, B, L)

(q5, 1)→(q5, 1, L)


