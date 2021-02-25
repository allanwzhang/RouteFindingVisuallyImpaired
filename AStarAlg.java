package PathFinding;

import java.io.*;
import java.util.*;

public class AStarAlg {

	public static void main(String[] args) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader("C:\\Allan\\intermediate\\cutGraph.csv"));
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("C:\\Allan\\intermediate\\testGraph.csv")));
		int[][] grid = new int[630][1030];
		for(int i = 0; i < grid.length; i++) {
			grid[i] = toIntArray(f.readLine().split(","));
		}
		
		boolean[][] visited = new boolean[630][1030];
		
		for(int i = 0; i < grid.length; i++) {
			for(int j = 0; j < grid[i].length; j++) {
				if(grid[i][j] == 0) grid[i][j] = -1;
			}
		}
		
		Deque<int[]> points = new ArrayDeque<>();
		points.add(new int[] {303, 245});
		
		while(points.size()>0) {
			int[] curr = points.removeFirst();
			for(int x = curr[0]-1; x <= curr[0]+1; x++) {
				for(int y = curr[1]-1; y <= curr[1]+1; y++) {
					if(x!=curr[0]&&y!=curr[1]) continue;
					if(x>=0&&y>=0&&x<grid.length&&y<grid[0].length&&!visited[x][y]&&grid[x][y]==-1) {
						visited[x][y] = true;
						points.add(new int[] {x,y});
					}
				}
			}
			grid[curr[0]][curr[1]] = 0;
			visited[curr[0]][curr[1]] = true;
		}
		
		writeCSV(grid, out);
		out.close();
		f.close();
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
	
	static int[] toIntArray(String[] arr) {
		int[] result = new int[arr.length];
		for(int i = 0; i < arr.length; i++) {
			result[i] = Integer.parseInt(arr[i]);
		}
		return result;
	}	
}
