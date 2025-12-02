#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void printArray(const vector<int>& arr) {
    for (int v : arr) cout << v << " ";
    cout << endl;
}

int main() {
    vector<int> data = {8, 4, 5, 2, 7};

    cout << "Before sorting:\n";
    printArray(data);

    insertionSort(data);

    cout << "After sorting:\n";
    printArray(data);

    return 0;
}
