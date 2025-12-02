public class Sorting {

    public static void bubbleSort(int[] arr) {
        boolean swapped = true;
        int n = arr.length;

        while (swapped) {
            swapped = false;
            for (int i = 1; i < n; i++) {
                if (arr[i - 1] > arr[i]) {
                    int temp = arr[i];
                    arr[i] = arr[i - 1];
                    arr[i - 1] = temp;
                    swapped = true;
                }
            }
            n--;
        }
    }

    public static void printArray(int[] arr) {
        for (int v : arr) System.out.print(v + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        int[] data = {5, 2, 9, 1, 3};

        System.out.println("Before sorting:");
        printArray(data);

        bubbleSort(data);

        System.out.println("After sorting:");
        printArray(data);
    }
}
