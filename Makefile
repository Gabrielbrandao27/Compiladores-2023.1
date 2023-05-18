run-generator-scanner:
	python scanner/gerador_scanner.py
	python scanner/runner_scanner.py

run-scanner:
	python scanner/runner_scanner.py

run-parser:
	python Parser/parser.py

run-generator-scanner-parser:
	python scanner/gerador_scanner.py
	python scanner/runner_scanner.py
	python parser/parser.py