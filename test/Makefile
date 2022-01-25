# Path to script
M6S = ../scripts/MOM6param_scan.py

TESTS = test1.json test2.json test3.json test3.html test3.text
MD5SUMS = $(foreach t,$(TESTS),$(t).md5sum)
REMOVE_TRAILING_SPACE = sed 's/ $$//'

all: test check

# Put the parameter file inside a tar file
ball.tar: MOM_parameter_doc.all
	tar zcf $@ $^

# Test JSON dump of a parameter file
test1.json: MOM_parameter_doc.all
	$(M6S) $< | $(REMOVE_TRAILING_SPACE) > $@

# Test JSON dump of a parameter file from inside a tar file
test2.json: ball.tar
	$(M6S) $< | $(REMOVE_TRAILING_SPACE) > $@

# Test difference of two files with different values
test3.json: MOM_parameter_doc.all test3.mom6
	$(M6S) -m $^ | $(REMOVE_TRAILING_SPACE) > $@

# Test difference of two files with different values
test3.html: MOM_parameter_doc.all test3.mom6
	$(M6S) -m -fmt html $^ | $(REMOVE_TRAILING_SPACE) > $@

# Test difference of two files with different values
test3.text: MOM_parameter_doc.all test3.mom6
	$(M6S) -m -fmt text $^ | $(REMOVE_TRAILING_SPACE) > $@

# Checksum of JSON output
%.md5sum: %
	md5sum $< > $@

# Invoke each test that results in a JSON file
test:
	make --always-make $(TESTS)
	pytest

# Check the status of the *.md5sum files
check: $(TESTS)
	md5sum -c $(MD5SUMS)

# Target to generate md5 checksum files
regen: $(MD5SUMS)

# Remove all files that cannot be regenerated
clean:
	-rm *.json *.tar $(MD5SUMS)
