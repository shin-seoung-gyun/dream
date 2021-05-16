import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DirectoryMake {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// TODO Auto-generated method stub
		List<String> list = new ArrayList<>();
		Map<String, List<String>> regionMap = new HashMap<>();
		List<String> guList = new ArrayList<>();

		Path path = Paths.get("C:\\Users\\Admin\\Desktop\\대전.csv");
		try (BufferedReader reader2 = Files.newBufferedReader(path, StandardCharsets.UTF_8)) {
			String line;
			while ((line = reader2.readLine()) != null) {
				if (!line.isBlank())
					list.add(line);
			}
		} catch (IOException e) {
			System.err.println(e);
		}

		for (int i = 0; i < list.size(); i++) {
			String temp = list.get(i);
			var strAry = temp.split(",", -1);
			if (i == 0) {
				for (var val : strAry) {
					guList.add(val);
					regionMap.put(val, new ArrayList<>());
				}
			} else {
				for (int j = 0; j < guList.size(); j++) {
					var guName = guList.get(j);
					var dongName = strAry[j];
					if (!dongName.isBlank()) {
						regionMap.get(guName).add(dongName);
					}
				}
			}
		}
		System.out.println(regionMap);

		// 대전 폴더 만들기
		String defaultPath = "C:\\Users\\Admin\\Desktop\\";
		String region = "대전";
		Path path2 = Paths.get(defaultPath + region);
		try {
			Files.createDirectories(path2);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		for (var guName : guList) {
			String guPath = defaultPath + region + "\\" + guName;
			path2 = Paths.get(guPath);
			try {
				Files.createDirectories(path2);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

			for (var dongName : regionMap.get(guName)) {
				String dongPath = guPath + "\\" + dongName;
				path2 = Paths.get(dongPath);
				try {
					Files.createDirectories(path2);
					// Files.createTempFile(path2, dongName, ".hwp");
					dongPath += "\\" + dongName + ".txt";
					path2 = Paths.get(dongPath);
					Files.createFile(path2);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}

	}

}
