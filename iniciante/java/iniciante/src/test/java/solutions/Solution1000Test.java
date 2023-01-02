package solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;

import beecrowd.solutions.Solution1000;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import org.junit.jupiter.api.Test;

public class Solution1000Test {

  @Test
  void shouldReturnHelloWorld() throws IOException {
    final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    System.setOut(new PrintStream(outContent));

    String[] args = {};
    Solution1000.main(args);
    assertEquals("Hello World!\n", outContent.toString());
  }

}
