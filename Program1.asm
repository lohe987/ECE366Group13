.data
P: .word 1005
R: .word -1

.text
	addi $8, $0, 0x2000 #stores address of P into $8
	addi $9, $0, 0x2004 #stores address of R into $9
	lw $10, ($8) #stores the value of P the size of a word into $10
	addi $11, $0, 1 #$11 will hold the mod of every iteration
	addi $12, $0, 5 #loop counter for sum
	addi $13, $0, 17 #loop counter for mod
	addi $14, $0, 1 #holds sum of numbers for sum loop

loop:	beq $10, $0, end #ends once 6^P mod 17 is calculated 
sum:	beq $12, $0, mod #goes to mod once $14 * 6 is calculated
	add $14, $14, $11 #loop keeps adding in order to do $11 times 6
	addi $12, $12, -1 #decrement $10
	j sum
	
mod:	slt $15, $14, $13 #once difference is less than 17, that will give mod 
	bne $15, $0, lower
	sub $14, $14, $13 #subtracts $14 every time by 17
	j mod

lower:	addi $10, $10, -1 #decrement P to determine how many loops to make
	addi $12, $0, 5 #reset counter for sum
	add $11, $0, $14 #next number that will needed to be multiplied by 6
	j loop
	
end:	sw $14, ($9) #stores the value of $14 into R
exit:	j exit #dead loop