import java.util.*;
public class PascalTri {
	/* 문제 풀이 재귀 함수 */
	static int solve(int i, int j) { // i = row, j = coloum
		if ((j == 1) || (j == i)) return 1; // base cases
		else return solve(i - 1, j - 1) + solve(i - 1, j); // 파스칼 삼각형 점화식
	}
	
	/* 예쁘게 출력하는 함수 */
	static void print(int n, int space, int i, int j) { // i = row, j = coloum
		if (n < 1)	return;// base case
		else if (space != 0) { // 공백 출력
			System.out.print(String.format("%4s", " ")); // 공백 채워주고
			print(n, space - 1, i, j); // recursion call
		} else if (i < j) { // 개행
			System.out.println(); // 한줄 띄고
			space = (n - 1) - 1; // 공백 개수 다시 정해주고
			print(n - 1, space, i + 1, 1); // recursion call
		} else { // 파스칼 삼각형에 맞는 수를 가져옴
			System.out.print(String.format("%8d", solve(i, j)));
			print(n, space, i, j + 1); // recursion call
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		System.out.print("input : ");
		int n = s.nextInt();
		print(n, n - 1, 1, 1); // 실행
	}

}
