#include <string>
#include <vector>
#include <iostream>
#include "DataObject.h"

TableHeader::TableHeader()
	: ColumnHeader("") {
}

ColumnHeader* TableHeader::nextColumn(){
        ColumnHeader* bestColumn;
        int min = -1;
        for (DataObject* r = this->right; r != this; r = r->right){
            int m = ((ColumnHeader*)r)->countRows();
            if (min == -1 || m < min) {
                min = m;
                bestColumn = (ColumnHeader*)r;
            }
        }
	return bestColumn;
}

void TableHeader::print_solution(){
	for (std::vector<DataObject*>::iterator o = O.begin(); o != O.end(); o++){
		if (*o != NULL){
			std::cout << (*o)->column->name << " ";
			for (DataObject* r = (*o)->right; r != *o; r = r->right){
				std::cout << r->column->name << " ";
			}
			std::cout << std::endl;
		}
	}
}

void TableHeader::search(int k){
	if (this->right == this) {
		print_solution();
		return;
	}
	ColumnHeader* c = this->nextColumn();
	c->cover();
	O.resize(k+1);
	for (DataObject* r = c->down; r != c; r = r->down){
		O[k] = r;
		for (DataObject* j = r->right; j != r; j = j->right){
			j->column->cover();
		}
		this->search(k + 1);
		r = O[k];
		for (DataObject* j = r->left; j != r; j = j->left){
			j->column->uncover();
		}
	}
	c->uncover();
	return;
}

void TableHeader::store_solution(){
        std::vector<std::vector<std::string>>* myResult = new std::vector<std::vector<std::string>>();
	for (std::vector<DataObject*>::iterator o = O.begin(); o != O.end(); o++){
                std::vector<std::string>* ss = new std::vector<std::string>();
		if (*o != NULL){
                        ss->push_back((*o)->column->name);
			for (DataObject* r = (*o)->right; r != *o; r = r->right){
                                ss->push_back(r->column->name);
			}
		}
                myResult->push_back(*ss);
	}
        result.push_back(*myResult);
}

void TableHeader::search_store(int k){
	if (this->right == this) {
		store_solution();
		return;
	}
	ColumnHeader* c = this->nextColumn();
	c->cover();
	O.resize(k+1);
	for (DataObject* r = c->down; r != c; r = r->down){
		O[k] = r;
		for (DataObject* j = r->right; j != r; j = j->right){
			j->column->cover();
		}
		this->search_store(k + 1);
		r = O[k];
		for (DataObject* j = r->left; j != r; j = j->left){
			j->column->uncover();
		}
	}
	c->uncover();
	return;
}

ColumnHeader::ColumnHeader(std::string name)
	: name(name), DataObject(NULL) {
}

int ColumnHeader::countRows(){
        int c = 0;
	for (DataObject* i = this->down; i != this; i = i->down) {
            c++;
	}
        return c;
}
void ColumnHeader::cover(){
	left->right = this->right;
	right->left = this->left;
	for (DataObject* i = this->down; i != this; i = i->down) {
		for (DataObject* j = i->right; j != i; j = j->right) {
			j->hide();
		}
	}
}

void ColumnHeader::uncover(){
	left->right = this;
	right->left = this;
	for (DataObject* i = this->up; i != this; i = i->up) {
		for (DataObject* j = i->left; j != i; j = j->left) {
			j->unhide();
		}
	}
}

DataObject::DataObject(ColumnHeader* column)
	: column(column){
}

void DataObject::hide() {
	up->down = this->down;
	down->up = this->up;
	column->size--;
}

void DataObject::unhide() {
	up->down = this;
	down->up = this;
	column->size++;
}
