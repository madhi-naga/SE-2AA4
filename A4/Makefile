
JFLAGS = -g
JCLASS = -cp ./src:.:$(CLASSPATH).:./src/junit-4.5.jar
#JCLASS = -cp ./src:.:$(CLASSPATH):/usr/share/java/junit4-4.5.jar # on mills
JC = javac
JVM = java
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $(JCLASS) $*.java

CLASSES = \
	src/ColourT.java \
	src/Dots.java \
	src/DotsController.java \
	src/DotsView.java \
	src/DotsEngine.java \
	src/TestDots.java \

TEST = TestDots

default: classes

classes: $(CLASSES:.java=.class)

doc:
	doxygen doxConfig
	cd latex && $(MAKE)

test: src/$(TEST).class
	$(JVM) $(JCLASS) org.junit.runner.JUnitCore $(TEST)

expt: src/DotsEngine.java
	$(JC) $(JCLASS) $(JFLAGS) src/DotsEngine.java
	$(JVM) $(JCLASS) DotsEngine

clean:
	rm -rf html
	rm -rf latex
	cd src
	rm **/*.class
