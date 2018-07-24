#include <array>

#include "DataObject.h"
#include "TableFactory.h"

void solve_exact_cover(bool** rows, std::vector<std::string> names, int width, int count) {
    TableFactory* tf = new TableFactory(rows, names, width, count);
    TableHeader* th = tf->createTable();
    th->search(0);
}
