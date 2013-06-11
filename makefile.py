all:
	make run
	make test

diff:
	RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.out RunCollatz.tmp
	rm RunCollatz.tmp

doc:
	pydoc -w Collatz

log:
	git log > Collatz.log

run:
	RunCollatz.py < RunCollatz.in

test:
	TestCollatz.py

turnin-list:
	turnin --list bendy cs373pj1

turnin-submit:
	turnin --submit bendy cs373pj1 Collatz.zip

turnin-verify:
	turnin --verify bendy cs373pj1

zip:
	zip -r Collatz.zip makefile                \
	Collatz.html Collatz.log Collatz.py        \
	RunCollatz.in RunCollatz.out RunCollatz.py \
	SphereCollatz.py                           \
	TestCollatz.py TestCollatz.out

clean:
	rm -f *.pyc
	rm -f *.tmp
