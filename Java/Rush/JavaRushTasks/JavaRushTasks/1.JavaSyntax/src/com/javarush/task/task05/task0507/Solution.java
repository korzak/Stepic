package com.javarush.task.task05.task0507;
import java.io.*;

/* 
Среднее арифметическое
*/

public class Solution {
    public static void main(String[] args) throws Exception {


        int i = 0;
        int count = 0;
        int sum = 0;

        while (i != -1) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String numa = reader.readLine();
            int num = Integer.parseInt(numa);

            if (num == -1) {
                System.out.println((double) sum / count );
                break;
            } else {
                count += 1;
                sum += num;
            }
        }

    }
}

