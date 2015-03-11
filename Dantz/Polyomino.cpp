#include "Polyomino.h"

Polyomino::Polyomino(int w, int h, bool* squares[], std::string name)
	:width_(w), height_(h), name_(name) {
	points_ = new std::vector<std::pair<int, int>>();
	for (int i = 0; i < height_; i++) {
		for (int j = 0; j < width_; j++) {
			if (squares[i][j]) {
				std::pair<int, int> point(i, j);
				points_->push_back(point);
			}
		}
	}
}