#include <iostream>
#include "TableFactory.h"

TableFactory::TableFactory(bool* table[], std::vector<std::string> names, int w, int h)
	: table(table), names(names), w(w), h(h) {}

TableHeader* TableFactory::createTable(){
	TableHeader* th = new TableHeader();
	ColumnHeader* last = th;
	DataObject** end = new DataObject*[w];
	ColumnHeader** heads = new ColumnHeader*[w];
	for (int i = 0; i < w; i++){
		ColumnHeader* ch = new ColumnHeader(names[i]);
		ch->left = last;
		last->right = ch;
		last = ch;
		end[i] = ch;
		heads[i] = ch;
	}
	last->right = th;
	th->left = last;
	for (int j = 0; j < h; j++){
		DataObject* last_row = NULL;
		DataObject* first_row = NULL;
		for (int k = 0; k < w; k++){
			if (table[j][k]){
				DataObject* dobj = new DataObject(heads[k]);
				if (first_row == NULL){
					first_row = dobj;
				}
				else {
					last_row->right = dobj;
					dobj->left = last_row;
				}
				last_row = dobj;
				dobj->up = end[k];
				end[k]->down = dobj;
				end[k] = dobj;
			}
		}
		last_row->right = first_row;
		first_row->left = last_row;
	}
	for (int i = 0; i < w; i++){
		end[i]->down = heads[i];
		heads[i]->up = end[i];
	}
	return th;
}
