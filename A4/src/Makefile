
JFLAGS = -g
JCLASS = -cp ./app:.: #$(CLASSPATH).:./junit4-4.5.jar
#JCLASS = -cp ./app:.:$(CLASSPATH):/usr/share/java/junit4-4.5.jar # on mills
JC = javac
JVM = java
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $(JCLASS) $*.java

CLASSES = \
	app/ColourT.java \
	app/Dots.java \
	app/DotsController.java \
	app/DotsView.java \
	app/DotsEngine.java \
	app/TestDots.java \
	app/DotsApp.java \

TEST = TestDots

default: classes

classes: $(CLASSES:.java=.class)

doc:
	doxygen doxConfig
	cd latex && $(MAKE)

test: app/$(TEST).class
	$(JVM) $(JCLASS) org.junit.runner.JUnitCore $(TEST)

expt: app/DotsApp.java
	$(JC) $(JCLASS) $(JFLAGS) app/DotsApp.java
	$(JVM) $(JCLASS) DotsApp

clean:
	rm -rf html
	rm -rf latex
	cd app
	rm **/*.class
