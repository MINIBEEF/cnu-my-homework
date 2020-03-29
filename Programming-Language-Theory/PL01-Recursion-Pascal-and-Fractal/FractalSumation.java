import java.util.*;

/* @class fraction �м��� ǥ���� ��ü */
class Fraction {
	int mother; // �и�
	int son; // ����

	public Fraction() { // 1/1�� ����
		this.mother = 1;
		this.son = 1;
	}
	
	public void setSon(int son) { // setter
		this.son = son;
	}
	
	public void setMother(int mother) { // settr
		if(mother == 0) // divide by zero exception
			System.out.println("cannot divide by zero");
		else
			this.mother = mother;
	}
	@Override
	public String toString() { // ��� ��� ��
		return "(" + this.son + "/" + this.mother + ")L";
	}
}

public class FractalSumation {
	/* ���� Ǯ�� ��� �Լ� */
	/* ��ȭ�� = (3^n / 2^(n-1)) */
	static Fraction run(int n, Fraction ret) {
		if(n < 2) { // base case
			ret.setSon(ret.son * 3);
			return ret;
		} else {
			ret.setSon(ret.son * 3);
			ret.setMother(ret.mother * 2);
			return run(n - 1, ret); // recursion calling
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Fraction frac = new Fraction();
		
		Scanner s = new Scanner(System.in);
		System.out.print("input : ");
		int n = s.nextInt();
		
		Fraction frac_ret = run(n, frac);
		
		System.out.println("S" + n + " = " + frac_ret);
		
	}

}
