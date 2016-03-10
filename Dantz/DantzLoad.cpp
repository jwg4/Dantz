// Dantz.cpp : Defines the entry point for the console application.
//

#include <array>

#include "DataObject.h"
#include "TableFactory.h"

#include "DantzLoad.h"

int main(int argc, char* argv[])
{
	TableFactory* tf = new TableFactory(table, names, 7, 6);
	TableHeader* th = tf->createTable();
	th->search(0);

	return 0;
}

