OBJS=DataObject.o Polyomino.o TableFactory.o

all: Dantz_output DantzLoad_output DantzCSV_output

Dantz_output: Dantz
	./Dantz > Dantz_output

DantzLoad_output: DantzLoad
	./DantzLoad > DantzLoad_output

DantzCSV_output: DantzCSV rows.txt names.txt
	./DantzCSV > DantzCSV_output

DantzCSV: DantzCSV.o $(OBJS)
	g++ DantzCSV.o $(OBJS) -o DantzCSV

Dantz: Dantz.o $(OBJS)
	g++ Dantz.o $(OBJS) -o Dantz

DantzLoad: DantzLoad.o $(OBJS) DantzLoad.h
	g++ DantzLoad.o $(OBJS) -o DantzLoad

DantzLoad.h: SampleDantzLoad.h
	ln -s SampleDantzLoad.h DantzLoad.h

%.o: %.cpp
	g++ -c --std=c++0x $< -o $@

DantzLoad.o: DantzLoad.h

clean:
	rm *.o
	rm Dantz
	rm DantzLoad
 
