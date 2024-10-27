class Solution {
public:
  string multiply(string num1, string num2) {
    if (num2.length() < num1.length()) return multiply(num2, num1);

    if (num1 == "0" || num2 == "0") return "0";

    string product = "";

    vector<int> nums(num1.size() + num2.size(), 0);

    for (int i = num1.length() - 1; i > -1; --i) {
      for (int j = num2.length() - 1; j > -1; --j) {
        nums[i + j + 1] += (num1[i] - '0') * (num2[j] - '0');
        nums[i + j] += nums[i + j + 1] / 10;
        nums[i + j + 1] %= 10; 
      }
    }

    for (int num : nums) {
      product += to_string(num);
    }

    if (product.length() > 1 && product[0] == '0') {
      return product.substr(1);
    }
    return product;
  }
}
