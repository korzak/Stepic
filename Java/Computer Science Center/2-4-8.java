/*
Реализуйте метод, вычисляющий факториал заданного натурального числа.

Факториал N вычисляется как 1*2*…*N

Поскольку это очень быстро растущая функция, то даже для небольших N вместимости типов int и long очень скоро не хватит. Поэтому будем использовать BigInteger.
*/

//Код(рекурсия) :

public static BigInteger factorial(int value) {
    if (value == 0) return new BigInteger("1");
    BigInteger x = BigInteger.valueOf(value);
    return x.multiply(factorial(value - 1));
}



//Супер код:

 public static BigInteger factorial(int value) {
  return  value == 0 ? BigInteger.ONE : BigInteger.valueOf(value).multiply(factorial (value-1));
}
