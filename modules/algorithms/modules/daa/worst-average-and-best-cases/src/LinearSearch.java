public class LinearSearch {

  static int search(int arr[], int arrSize, int element)
  {
    int i;
    for(i = 0; i < arrSize; i++)
      if(arr[i] == element)
        return i;
    return -1;
  }

  public static void main(String[] args)
  {
    int arr[] = {1, 10, 30, 15};
    int element = 30;
    int arrSize = arr.length;

    System.out.printf("%d is present at index %d", element, search(arr, arrSize, element));
  }
}
