default: 00 01

dst:
	mkdir -p dst
# basic
00: dst
	dictfile diff src/000person.json src/001person.json > dst/00.diff
	dictfile diff src/000person.json src/001person.json --sort-keys > dst/00.sorted.diff
	dictfile diff src/000person.json src/001person.json -o md > dst/00.md
	dictfile diff src/000person.json src/001person.json -o dict > dst/00.dict
	dictfile diff src/000person.json src/001person.json -o tsv > dst/00.tsv
	dictfile diff src/000person.json src/001person.json -o jsonpatch > dst/00.jsonpatch
	dictfile diff --verbose src/000person.json src/001person.json -o jsonpatch > dst/00.jsonpatch2

# list
01: dst
	dictfile diff src/010people.tsv src/011people.tsv > dst/01.diff
	dictfile diff src/010people.tsv src/011people.tsv --sort-keys > dst/01.sorted.diff
	dictfile diff src/010people.tsv src/011people.tsv -o md > dst/01.md
	dictfile diff src/010people.tsv src/011people.tsv --skip-empty -o md > dst/01.skipped.md
	dictfile diff src/010people.tsv src/011people.tsv --verbose -o jsonpatch > dst/01.jsonpatch

# yaml
02: dst
	dictfile diff src/000person.yaml src/001person.yaml > dst/02.diff
	dictfile diff src/000person.yaml src/001person.yaml --sort-keys > dst/02.sorted.diff
	dictfile diff src/000person.yaml src/001person.yaml -o md > dst/02.md
	dictfile diff src/000person.yaml src/001person.yaml -o dict > dst/02.dict
	dictfile diff src/000person.yaml src/001person.yaml -o tsv > dst/02.tsv
