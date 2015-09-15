#include <vector>
#include "TableFactory.h"
#include "Polyomino.h"

class PolyominoSearch {
public:
	PolyominoSearch(int w, int h, std::vector<Polyomino>);
	TableFactory SetupSearch();
 private:
	int width;
	int height;
	std::vector<Polyomino> polyominos;
};
