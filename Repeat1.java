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

		
		//배열(array)복습
		//1) Array 만들기
		int[] intArray = new int[100];//크기가 100인 배열 생성
		for(int i = 1 ; i<=100; i++) {
			intArray[i-1] = i;
		}
		System.out.println(Arrays.toString(intArray));
		System.out.println(intArray[1]);
		intArray[1]=1;
		System.out.println(intArray[1]);
		
		//리스트 만들기
		List<Integer> intList = new ArrayList<Integer>();
		for(int i = 0; i <100; i++) {
			intList.add(i);
		}
		System.out.println(intList);
		intList.get(0);//리스트에서 인덱스로 값 받아오기
		intList.set(0, 1);//리스트에서 인덱스로 값 바꾸기
		
		//set만들기
		Set<Integer> intSet = new HashSet<Integer>();
		intSet.add(1);
		intSet.add(1);
		intSet.add(1);
		intSet.add(1);
		System.out.println(intSet);
		//map만들기
		Map<Integer, Integer> intMap = new HashMap<Integer, Integer>();
		intMap.put(1, 2);
		System.out.println(intMap.get(1));
		
		
		
		
		
		
	}

}
