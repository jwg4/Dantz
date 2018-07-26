#include <array>

#include <python2.7/Python.h>

#include "DataObject.h"
#include "TableFactory.h"

extern "C" PyObject* solve_exact_cover(bool**, char**, int, int);

PyObject* solve_exact_cover(bool** rows, char** names, int width, int count) {
    std::vector<std::string> namev = {};
    for (int i = 0; i < width; i++) {
        std::string s(names[i]);
        namev.push_back(s);
    }

    TableFactory* tf = new TableFactory(rows, namev, width, count);
    TableHeader* th = tf->createTable();

    th->search_store(0);

    PyObject* results = PyList_New(0);
    for (std::vector<std::vector<std::vector<std::string>>>::iterator it = th->result.begin(); it != th->result.end(); it++) {
        PyObject* result = PyList_New(0);
        for (std::vector<std::vector<std::string>>::iterator jt = it->begin(); jt != it->end(); jt++) {
            PyObject* res_v = PyList_New(0);
            for (std::vector<std::string>::iterator kt = jt->begin(); kt != jt->end(); kt++) {
                PyList_Append(res_v, PyString_FromString(kt->c_str()));
            }
            PyList_Append(result, res_v);
        }
        PyList_Append(results, result);
    }
    return results;
}
