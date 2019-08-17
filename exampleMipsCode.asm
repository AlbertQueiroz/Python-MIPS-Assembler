LOOP:	addi $t0, $t1 , 4
		lw $t1, 10($s3)
		sw $t1, 15($s4)
		addi $t6, $t4, 4
		add $t2, $t0, $t6
		beq $t0, $t6, EXIT
		j LOOP
EXIT: