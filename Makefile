SCRIPTS = public/scripts
all: dart jade

dart:
	dart2js -m -o $(SCRIPTS)/backbuffer.dart.js $(SCRIPTS)/backbuffer.dart -v

jade:
	jade index.jade
