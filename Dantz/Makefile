OBJS=Dantz.o DataObject.o Polyomino.o TableFactory.o

all: Dantz

Dantz: $(OBJS)
	g++ $(OBJS) -o Dantz

%.o: %.cpp
	g++ -c --std=c++0x $< -o $@

clean:
	rm *.o
	rm Dantz
 