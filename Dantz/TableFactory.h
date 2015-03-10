#pragma once

#include <string>
#include <vector>
#include "DataObject.h"

class TableFactory {
public:
	TableHeader* createTable();
	TableFactory(bool* table[], std::vector<std::string>, int, int);
private:
	bool** table;
	std::vector<std::string> names;
	int w, h;
};