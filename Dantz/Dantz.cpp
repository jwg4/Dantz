// Dantz.cpp : Defines the entry point for the console application.
//

#include <array>

#include "DataObject.h"
#include "TableFactory.h"

int main(int argc, char* argv[])
{
	bool row0[] = { 0, 0, 1, 0, 1, 1, 0 };
	bool row1[] = { 1, 0, 0, 1, 0, 0, 1 };
	bool row2[] = { 0, 1, 1, 0, 0, 1, 0 };
	bool row3[] = { 1, 0, 0, 1, 0, 0, 0 };
	bool row4[] = { 0, 1, 0, 0, 0, 0, 1 };
	bool row5[] = { 0, 0, 0, 1, 1, 0, 1 };
	bool **table = new bool*[6]{
		row0, row1, row2, row3, row4, row5
	};

	std::vector<std::string> names = { "1", "2", "3", "4", "5", "6", "7" };
	TableFactory* tf = new TableFactory(table, names, 7, 6);
	TableHeader* th = tf->createTable();
	th->search(0);

	return 0;
}

