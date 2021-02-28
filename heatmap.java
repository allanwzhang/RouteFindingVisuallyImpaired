package PathFinding;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class heatmap {

	public static void main(String[] args) throws IOException{
		int[][] nearest= load("C:\\Allan\\intermediate\\nearestGraph.csv");
		for(int i = 0; i < nearest.length; i++) {
			for(int j = 0; j < nearest[0].length; j++) {
				if(nearest[i][j] == -1) nearest[i][j] = 6;
			}
		}
		
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("C:\\Allan\\intermediate\\showNearest.csv")));
		writeCSV(nearest, out);
	}

	static void writeCSV(int[][] grid, PrintWriter out) throws IOException {
		for(int i = 0; i < grid.length; i++) {
			StringBuilder sb = new StringBuilder(grid[i][0]+"");
			for(int j = 1; j < grid[i].length; j++) {
				sb.append(","+grid[i][j]);
			}
			out.println(sb.toString());
		}
	}
	
	static int[][] load(String dest) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader(dest));
		int[][] grid = new int[630][1030];
		for(int i = 0; i < grid.length; i++) {
			grid[i] = toIntArray(f.readLine().split(","));
		}
		f.close();
		return grid;
	}
	
	static int[] toIntArray(String[] arr) {
		int[] result = new int[arr.length];
		for(int i = 0; i < arr.length; i++) {
			result[i] = Integer.parseInt(arr[i]);
		}
		return result;
	}
}
