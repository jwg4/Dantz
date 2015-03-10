#pragma once

#include <string>
#include <vector>

class ColumnHeader;

class DataObject {
public:
	DataObject(ColumnHeader*);
	ColumnHeader* column;
	DataObject* up;
	DataObject* down;
	DataObject* left;
	DataObject* right;
	void hide();
	void unhide();
};

class ColumnHeader : public DataObject {
public:
	ColumnHeader(std::string);
	std::string name;
	int size;
	void cover();
	void uncover();
};

class TableHeader : public ColumnHeader {
	void print_solution();
	std::vector<DataObject*> O;
	ColumnHeader* nextColumn();
public:
	TableHeader();
	void search(int);
};

