package com.javarush.task.task05.task0502;

/* 
Реализовать метод fight
*/

public class Cat {
    public String name;
    public int age;
    public int weight;
    public int strength;


    public Cat() {
    }

    public boolean fight(Cat anotherCat) {

        if ((this.strength + this.age + this.weight) > (anotherCat.strength + anotherCat.weight + anotherCat.age)) return true;
        else return false;
    }


    public static void main(String[] args) {

        Cat cat2 = new Cat();
        Cat cat1 = new Cat();

        cat1.age = 12;
        cat1.name = "Mik";
        cat1.weight = 4;
        cat1.strength = 5;

        cat2.age = 12;
        cat2.name = "Mik";
        cat2.weight = 4;
        cat2.strength = 7;

        System.out.println(cat1.fight(cat2));
        System.out.println("--------------");
        System.out.println(cat2.fight(cat1));

    }
}
