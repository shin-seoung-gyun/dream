package repeat1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Repeat1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		//�迭(array)����
		//1) Array �����
		int[] intArray = new int[100];//ũ�Ⱑ 100�� �迭 ����
		for(int i = 1 ; i<=100; i++) {
			intArray[i-1] = i;
		}
		System.out.println(Arrays.toString(intArray));
		System.out.println(intArray[1]);
		intArray[1]=1;
		System.out.println(intArray[1]);
		
		//����Ʈ �����
		List<Integer> intList = new ArrayList<Integer>();
		for(int i = 0; i <100; i++) {
			intList.add(i);
		}
		System.out.println(intList);
		intList.get(0);//����Ʈ���� �ε����� �� �޾ƿ���
		intList.set(0, 1);//����Ʈ���� �ε����� �� �ٲٱ�
		
		//set�����
		Set<Integer> intSet = new HashSet<Integer>();
		intSet.add(1);
		intSet.add(1);
		intSet.add(1);
		intSet.add(1);
		System.out.println(intSet);
		//map�����
		Map<Integer, Integer> intMap = new HashMap<Integer, Integer>();
		intMap.put(1, 2);
		System.out.println(intMap.get(1));
		
		
		
		
		
		
	}

}
