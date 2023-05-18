run-generator-scanner:
	python scanner/gerador_scanner.py
	python scanner/runner_scanner.py

run-scanner:
	python scanner/runner_scanner.py

run-parser:
	python Parser/parser_mini_c.py

run-generator-scanner-parser:
	python scanner/gerador_scanner.py
	python scanner/runner_scanner.py
	python Parser/parser_mini_c.py