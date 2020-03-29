import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Test {

	public static void main(String[] args) {
		RecursionLinkedList list = new RecursionLinkedList();
		FileReader fr;
		try {
			fr = new FileReader("hw02.txt");
			BufferedReader br = new BufferedReader(fr);
			String inputString = br.readLine();
			for(int i = 0; i < inputString.length(); i++)
				list.add(inputString.charAt(i));
		} catch (IOException e) {
			e.printStackTrace();
		}

		// hw02.txt : abcddcba

		/* (4) toString */
		System.out.println(list.toString());

		/* (1) linkLast */
		list.add(8, 'b');
		System.out.println(list.toString());

		/* (2) node */
		System.out.println(list.get(0));

		/* (3) length */
		System.out.println(list.size());
	}

}
