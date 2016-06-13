// Dantz.cpp : Defines the entry point for the console application.
//

#include <array>
#include <fstream>

#include "DataObject.h"
#include "TableFactory.h"

std::vector<std::string> read_names(char* filename) {
        std::ifstream namefile(filename);
        int n_names;
        namefile >> n_names;
        std::vector<std::string> names(n_names);
        for ( int i = 0; i < n_names; i++) {
               namefile >> names[i];
        }
        return names;
}

bool** read_rows(char* filename, int &n_rows, int n_cols) {
        std::ifstream rowfile(filename);
        rowfile >> n_rows;
        bool **table = new bool*[n_rows];
        for (int i=0; i < n_rows; i++) {
            table[i] = new bool[n_cols];
            for (int j=0; j < n_cols; j++) {
                rowfile >> table[i][j];
            }
        }
        return table;
}
    

int main(int argc, char* argv[])
{
        std::vector<std::string> names = read_names(argv[1]);
        int n_names = names.size();
        int n_rows;
        bool** table = read_rows(argv[2], n_rows, n_names);
	TableFactory* tf = new TableFactory(table, names, n_names, n_rows);
	TableHeader* th = tf->createTable();
	th->search(0);

	return 0;
}

