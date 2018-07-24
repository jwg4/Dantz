#include <array>

#include "DataObject.h"
#include "TableFactory.h"

extern "C" void solve_exact_cover(bool**, char**, int, int);

void solve_exact_cover(bool** rows, char** names, int width, int count) {
    std::vector<std::string> namev = {};
    for (int i = 0; i < width; i++) {
        std::string s(names[i]);
        namev.push_back(s);
    }

    TableFactory* tf = new TableFactory(rows, namev, width, count);
    TableHeader* th = tf->createTable();
}
