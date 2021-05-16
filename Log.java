import java.io.BufferedWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class Log {
	String path;

	Log() {
		path = "C:\\Users\\Admin\\Desktop\\";
	}

	void write(String type, String content) {
		// type : Error, Info, Warn

		SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
		SimpleDateFormat dateFormat2 = new SimpleDateFormat("HH-mm-ss");
		String date = dateFormat.format(Calendar.getInstance().getTime());
		String time = dateFormat2.format(Calendar.getInstance().getTime());

		Path path = Paths.get(this.path + date + ".log");

		try (BufferedWriter writer = Files.newBufferedWriter(path, StandardCharsets.UTF_8, StandardOpenOption.APPEND,
				StandardOpenOption.CREATE)) {

			String str = "[" + time + "][" + type + "]-" + content;
			writer.append(str);
			writer.newLine();

		} catch (Exception e) {
			// TODO: handle exception
		}

	}

}
