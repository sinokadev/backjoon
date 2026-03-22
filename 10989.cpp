#include <iostream>
#include <algorithm>
#include <vector>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int lenlen, number;

  std::cin >> lenlen;
  std::vector<int> numbers;
  numbers.reserve(lenlen);

  for (int i=0; i < lenlen; i++) {
    std::cin >> number;
    numbers.push_back(number);
  }

  std::sort(numbers.begin(), numbers.end());

  for (const int i : numbers) {
      std::cout << i << '\n';
  }
}
