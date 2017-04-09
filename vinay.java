
import java.util.Scanner;

class Person {

 private String name;
 private int age;
 private String DOB;
 private double height;
 private double weight;


 public Person() {


    Scanner ip = new Scanner(System.in);
    System.out.println("Enter Name");
    name = ip.nextLine();


    System.out.println("Enter Height (ft.in)");
    height=ip.nextDouble();



    System.out.print("Enter Date of Birth");
    DOB = ip.nextLine();



    System.out.println("Enter age");
    age = ip.nextInt();


    System.out.println("Enter Weight (XX.X) in kg");
    weight=ip.nextDouble();


 }

 public void displayName() {

  System.out.print(" My name is " + name + ". I was born on " + DOB +".");
  System.out.println(" I am " + age + " years old. I am " + height + " tall and weigh " + weight + " kgs.");

  }

 

}


class Male extends Person{

    private String sex;

   public Male() {

 
    super();

    sex="Male";
   }

 public void displayName() {

  super.displayName();

  System.out.println("My sex is " + sex);
 }



}


class run{


 public static void main(String[] args) {

     Male male = new Male();
     male.displayName();
 }

}




