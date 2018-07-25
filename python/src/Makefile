all: dantz.so

dantz.so: DataObject.cpp TableFactory.cpp dantz.cpp
	g++ -shared -o dantz.so -std=gnu++11 -fPIC DataObject.cpp TableFactory.cpp dantz.cpp
