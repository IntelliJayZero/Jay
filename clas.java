import java.util.Scanner;

interface Information {
    public void info();
    abstract void end();
}
abstract class Up {
    abstract int update();
    public Up() {
        System.out.println("up up up!");
    }
}
class Jay implements Information {
    String name;
    int score;
    int rank;
    public Jay(String name, int score, int rank) {
        this.name = name;
        this.score = score;
        this.rank = rank;
    }
    public void info() {
        System.out.println("name: " + name + " score: " + score + " rank: " + rank);
    }
    public void end() {
        System.out.println("done!");
    }
}
class Mark extends Up {
    double mark;
    int location;
    public Mark(double mark, int location) {
        this.mark = mark;
        this.location = location;
    }
    public int update() {
        this.location -= 1;
        return this.location;
    }
}
class Faulty extends Exception {
    public Faulty(String m) {
        super(m);
    }
}
class RunningMan extends Thread {
    String name;
    int t;
    public RunningMan(String name, int t) {
        this.name = name;
        this.t = t;
        System.out.println(this.name + " prepared!");
    }
    @Override
    public void run() {
        for (int i = 0; i < t; i++) {
            System.out.println("Running " + this.name + " " + (i+1) + " times");
        }
    }
}
class Sell implements Runnable {
    String name;
    int stuff = 5;
    public Sell(String name) {
        this.name = name;
        System.out.println(this.name + " is on work!");
    }
    @Override
    public void run() {
        // if (stuff > 0) {
        //     stuff -= 1;
        //     System.out.println(this.name + " sell, now:" + stuff);
        // }
        // else {
        //     System.out.println(this.name + " can't sell!");
        // }
        while (stuff > 0) {
            stuff--;
            System.out.println(this.name + " sell, now:" + stuff);
        }
    }
}
public class clas {
    public static void good(int a) throws Faulty {
        if (a < 0) {
            System.out.println(a);
            throw new Faulty("!!!<0!!!");
        }
    }
    public static void main(String[] args) {
        Jay j = new Jay("wwvc", 4, 0);
        j.info();
        j.end();
        Mark m = new Mark(98.234, 3);
        System.out.println(m.update());
        try {
            good(8);
            good(-2);
        } catch (Faulty e) {
            System.err.println(e);
            e.getMessage();
            e.printStackTrace();
        }
        int a = 4, b = 2, c = 3;
        Scanner sc = new Scanner(System.in);
        System.out.print("Den:");
        if (sc.hasNextInt())
            a = sc.nextInt();
        System.out.print("He:");
        if (sc.hasNextInt())
            b = sc.nextInt();
        System.out.print("Kai:");
        if (sc.hasNextInt())
            c = sc.nextInt();
        RunningMan den = new RunningMan("Den Chao", a);
        RunningMan he = new RunningMan("Chen He", b);
        RunningMan kai = new RunningMan("Zheng Kai", c);
        kai.start();
        den.start();
        he.start();
        Sell s = new Sell("Xie");
        Sell w = new Sell("Wo");
        new Thread(s).start();
        new Thread(w).start();
        // new Thread(s).start();
        // new Thread(w).start();
        // new Thread(s).start();
        // new Thread(w).start();
        // new Thread(s).start();
        // new Thread(w).start();
        // new Thread(s).start();
        // new Thread(w).start();
        // new Thread(s).start();
        // new Thread(w).start();
        sc.close();
        StringBuilder bb = new StringBuilder();
        bb.append("yya");
        System.out.println(bb);
    }
}