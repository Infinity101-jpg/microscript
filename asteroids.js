
new::pos::2

;;led.plot(0, pos)

forever
	new::ast::4
	if::pos::===::5
		change::pos::0
	end

	if::pos::===::-1
		change::pos::4
	end

	;;function bta() {
		if::btn_a
			change::pos::pos+1;
			;;led.unplot(0, pos - 1)
		end
	end

	;;function btb() {
		if::btn_b
			change::pos::pos-1
			;;led.unplot(0, pos + 1)
		end
	end

	new::rand::randint(0, 4)
	loop::5

		if::pos::===::rand
			
			if::ast::===::0
				printf::"game over"

				forever
					printf::" "
				end
			end


		end

		;;bta()
		;;btb()
		change::ast::ast-1
		;;led.plot(0, pos)
		;;led.plot(ast + 1, rand)
		;;basic.pause(160)
		;;led.unplot(ast + 2, rand)
		;;led.unplot(0, rand)
	end
end
