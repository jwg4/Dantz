#include "Polyomino.h"

public PolyominoSearch::PolyominoSearch(int w, int h, std::vector<Polyomino>polyominos) : width(w), height(h), polyominos(polyominos) {
}

TableFactory PolyominoSearch::TableFactory() {
  char buffer[50];
  int col_num = w * h + polyominos.size();
  vector<string> names(col_num);
  int offset;
  for (int i=0; i < w; i++) {
    for (int j=0; j < h; j++) {
      offset = i + w * j;
      names[offset] = snprintf(buffer, 50, "Sq (%d, %d)", i, j);
    }
  }
  for (int i=0; i < polyominos.size(); i++) {
    names[w*h + i] = strcat("Po ", polyominos[i].name_);
  }
  bool* table[];
  table = malloc(4 * w * h * polyominos.size() * sizeof(bool*));
  int row_p = 0;
  for (int i=0; i < polyominos.size(); i++) {
    Polyomino p = polyominos[i];
    std::vector<std::vector<CoordinatePair>> footprints;
    footprints = p.footprints();
    for (int j=0; j < footprints.size(); j++) {
      std::vector<CoordinatePair> footprint = footprints[j];
      for (int x=0; x < w; x++) {
	for (int y=0; y < h; y++) {
	  bool set[col_num];
	  for (int k=0; k < set.size(); k++) {
	    set[k] = 0;
	  }
	  for (int t=0; t < footprint.size(); t++) {
	    fx = footprint[t].first + x;
	    fy = footprint[t].second + y;
	    if (fx > w || fy > h) {
	      goto new_position;
	    }
	    set[fx + w * fy] = 1;
	  }
	  set[w * h + i] = 1;
	  table[row_p++] = &set;
	  new_position:
	}
      }
    }
  }
  return TableFactory(table, names, col_num, row_p);
}
