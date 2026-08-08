class Solution {
    public int getSum(int a, int b) {
        //do this by yourself in java

        // tryna add two numbers together using bitwise operations you're going to use XOR for just adding the bits and then 
        //goign to use the & operator for carrying a bit we also shift to the left as well when we & to be able to to simulate how a carry woudl be 
//         0001
//         0001 ^ 
//         0000
// 0001 - shift to left
//         0010
//         0010 - 2 
//         do all of this in loop fashion and it is constant time becyase the nunber are not arbiutrality large numbers 
        // while loop checking if the condition for carry is still 1

        while(b != 0) { 
            int temp = (a & b) << 1;
            a = a ^ b; 
            b = temp;
        }
        return a;
        //in java an int is 32 bit singned integer but with python there arbiutrry precision integers and they dont have a fixed limit 
        //they cna grow as large as hte computerd memory allows


        //carry bit can just keep getting shifted in python making it larger and larger since it dosen't have a fixed size  


    }
}
