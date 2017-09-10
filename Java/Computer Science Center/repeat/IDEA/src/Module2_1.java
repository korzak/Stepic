import java.util.Scanner;

public class Module2_1 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        System.out.print("Введите данные: ");
        int input = in.nextInt();
        //System.out.println(leapYearCount(input));*/

       /* int value = 7;
        int index = 4;
        System.out.println(flipBit(value, index)); */

        System.out.println(isPowerOfTwo(input));
    }

    /**
     * Реализуйте метод, возвращающий true, если среди четырех его аргументов ровно два истинны (любые). Во всех остальных случаях метод должен возвращать false.
     */
    public static boolean booleanExpression(boolean a, boolean b, boolean c, boolean d) {
        return (a | b | c | d) && !(a & b & c & d) && !(a ^ b ^ c ^ d);
    }


    /**
     *Реализуйте метод, вычисляющий количество високосных лет с начала нашей эры (первого года)
     * до заданного года включительно. На самом деле Григорианский календарь был введен значительно позже,
     * но здесь для упрощения мы распространяем его действие на всю нашу эру.
     *
     */
    public static int leapYearCount(int year) {
        int count = 0;
        for (int i = 1; i <= year; ++i) {
            System.out.println("i is "+i);
            if (((i % 4 == 0) && (i % 100 !=0)) || (i % 400 ==0)) {
                count++;

            }
        }
        return count;

    }

    /**
     * Реализуйте метод, возвращающий ответ на вопрос: правда ли, что a + b = c?
     * Допустимая погрешность – 0.0001 (1E-4)
     */
    public static boolean doubleExpression(double a, double b, double c) {
        return (Math.abs(c - (a + b)) <= 1E-4);
    }

    /**
     * Flips one bit of the given <code>value</code>.
     *
     * @param value     any number
     * @param bitIndex  index of the bit to flip, 1 <= bitIndex <= 32
     * @return new value with one bit flipped
     */
    public static int flipBit(int value, int bitIndex) {
        return (value ^ (1 << (bitIndex-1)));
    }

    /**
     *Реализуйте метод, который возвращает букву, стоящую в таблице UNICODE после символа "\" (обратный слэш) на расстоянии a.
     */
    public static char charExpression(int a) {
        char symbol = '\\';
        symbol = (char) (symbol+a);
        return symbol;
    }

    /**
     * Checks if given <code>value</code> is a power of two.
     *
     * @param value any number
     * @return <code>true</code> when <code>value</code> is power of two, <code>false</code> otherwise
     */
    public static boolean isPowerOfTwo(int value) {
        boolean is_exp_of_two = false;

        value = Math.abs(value);

        if (value == 1) {

            is_exp_of_two = true;

        } else
        { if (value != 0) {
            is_exp_of_two = ((value & (value - 1)) == 0);
            }
        }

        return is_exp_of_two;
    }

}
