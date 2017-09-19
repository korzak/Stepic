package aboutStatic;

class Vehicle{
    public static void kmToMiles(int km){
        System.out.println("Внутри родительского класса/статического метода");
    } }

class Car extends Vehicle{
    public static void  kmToMiles(int km){

    }
}

