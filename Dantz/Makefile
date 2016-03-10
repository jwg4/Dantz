OBJS=DataObject.o Polyomino.o TableFactory.o

all: Dantz

Dantz: Dantz.o $(OBJS)
	g++ $(OBJS) -o Dantz

DantzLoad: DantzLoad.o $(OBJS)
	g++ $(OBJS) -o DantzLoad

%.o: %.cpp
	g++ -c --std=c++0x $< -o $@

clean:
	rm *.o
	rm Dantz
	rm DantzLoad
 
