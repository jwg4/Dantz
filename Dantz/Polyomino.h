#include <string>
#include <utility>
#include <vector>

class Polyomino {
public:
	Polyomino(int w, int h, bool* squares[], std::string name);
	int width;
	int height;
	std::vector<std::pair<int, int >> Points(int direction);
	std::string name;
};

