#include <string>
#include <utility>
#include <vector>

class Polyomino {
public:
	Polyomino(int w, int h, bool* squares[], std::string name);
	int width_;
	int height_;
	std::vector<std::pair<int, int >> Points(int direction);
	std::string name_;
private:
	std::vector<std::pair<int, int >>* points_;
};

