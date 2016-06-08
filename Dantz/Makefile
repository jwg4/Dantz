OBJS=DataObject.o Polyomino.o TableFactory.o

all: Dantz sample_output

sample_output: DantzLoad
	./DantzLoad > sample_output

Dantz: Dantz.o $(OBJS)
	g++ Dantz.o $(OBJS) -o Dantz

DantzLoad: DantzLoad.o $(OBJS) DantzLoad.h
	g++ DantzLoad.o $(OBJS) -o DantzLoad

DantzLoad.h: SampleDantzLoad.h
	ln -s SampleDantzLoad.h DantzLoad.h

%.o: %.cpp
	g++ -c --std=c++0x $< -o $@

clean:
	rm *.o
	rm Dantz
	rm DantzLoad
 
