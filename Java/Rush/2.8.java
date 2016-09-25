
public class Solution
{
    public static void main(String[] args) 
    {
        System.out.println(minOf3numbers(5,3,6));
        print3("Qwerty");
        print3InOneLine("WERT");
    }
//--------------Методы--------------------------------------------------------
        public static int min (int a, int b){
            if (a < b) return a;
            else return b;
        }

        public static int max (int a, int b){
            if (a > b) return a;
            else return b;
        }

        public static int minOf3numbers (int a, int b, int c){
            int min = a;
            if (b < min) min = b;
            if (c < min) min = c;
            return min;
        }

        public static int minOf4numbers (int a, int b, int c, int d){
            int min = min(a, b);
            int min2 = min(c, d);
            min = min(min, min2);
            return min;
        }

        public static void print3(String s){
            for (int i = 0; i < 3; i++) System.out.println(s);
        }

        public static void print3InOneLine(String s){
            for (int i = 0; i < 3; i++) System.out.print(s+" ");
            System.out.println();
        }
}