// Write a java program to print the smallest element in array.

public class SmallestElement {
   public static void main(String[] args) {
        int[] arr = new int[]{5,3,2,0};
        int min = arr[0];
        for(int i=0; i<arr.length;i++){
            if(arr[i]<min)
                min=arr[i];
        } 
        System.out.println("Smallest element of array: "+ min);
    }
}