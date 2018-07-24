#include <array>

#include "DataObject.h"
#include "TableFactory.h"

extern "C" void solve_exact_cover(bool**, char**, int, int);

void solve_exact_cover(bool** rows, char** names, int width, int count) {
    std::vector<std::string> namev = {"a", "b", "c", "d", "e", "f", "g"};

    TableFactory* tf = new TableFactory(rows, namev, width, count);
    TableHeader* th = tf->createTable();
}
