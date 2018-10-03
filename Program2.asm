.data
T: .word 20
best_matching_score: .word -1

best_matching_count: .word -1

Pattern_Array: .word 10, 10, 17, 18, 19, -20, 21, 21, 21, 30, 31, 32, 50, 60, -10, -12, -50, -1, -4, -80

.text
	addi $8, $0, 0x2000 #assigning addresses to registers
	addi $9, $0, 0x2004
	addi $10, $0, 0x2008
	addi $16, $0, 32
	addi $17, $0, 0 #counter 
	addi $18, $0, 20 #number of words in Print_Array
	addi $19, $0, 1 #counter for best_matching_count, will always have at least 1
	lw $11, ($8) #storing T into $11
	
	addi $12, $10, 4 #counter for moving through addresses
	addi $21, $0, 0x205C #starting address of the next empty memory
	
next:	lw $13, ($12) #gets word from Pattern_Array
	xor $14, $11, $13 #compares each bit of the word with T to find what doesn't match
shift:	and $15, $14, 1 #will see how many bits don't match
	add $17,$17, $15 #$17 holds total number of bits that don't match 
	srl $14, $14, 1 #shifts to the right to check next bit
	beq $14, $0, sub
	j shift
	
sub:	sub $20, $16, $17 #subtracts 32 by $17 to get best_matching_score
	addi $17, $0, 0
	j save
	
save:	sw $20, ($21) #stores best_matching_score into Print_Array
	addi $12, $12, 4 #move to next word in array
	addi $21, $21, 4 #move to next empty memory
	addi $18, $18, -1 #decrement counter
	beq $18, $0, check #checks if more words need to be checked in array
	j next

check:	addi $21, $10, 80 #starts looking at beginning of Print_Array containing the best matching scores
	addi $13, $10, 84
	addi $18, $0, 20
	
compare:lw $14, ($12)
	lw $15, ($13)
loop:	addi $18, $18, -1
	beq $18, $0, end
	slt $16, $14, $15 #compares the best_matching_score of the words 
	beq $16, $0, greateq #goes to greateq if greater or equal
	sw $15, ($9) #storing the highest best_matching_score into 0x2004
	addi $19, $0, 1 #reset best_matching_count to 1
	j next2
	
greateq:sw $14, ($9) #storing the highest best_matching_score into 0x2004
	beq $14, $15, equal
	j next2
	
equal:	addi $19, $19, 1 #increment best_matching_count
	j next2
	
next2:	lw $14, ($9) #keeping $14 as the best_matching_score
	addi $13, $13, 4 
	lw $15, ($13) #move to next word
	j loop
	
end:	sw $19, ($10)
exit:	j exit #dead loop