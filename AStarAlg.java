package PathFinding;

import java.io.*;
import java.util.*;

public class AStarAlg {

	public static void main(String[] args) throws IOException {
		int[][] graph = load("C:\\Allan\\intermediate\\testGraph.csv");
		int[][] nearest= load("C:\\Allan\\intermediate\\nearestGraph.csv");
		
		Grid last = findPath(13, 19, 607, 1010, graph, nearest);
		
		PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("C:\\Allan\\intermediate\\Path.csv")));
		int count = 0;
		while(last.prev != null) {
			count++;
			out.println(last.y+","+last.x);
			last = last.prev;
		}
		System.out.println(count);
		
		out.close();
	}
	
	static Grid findPath(int sx, int sy, int ex, int ey, int[][] grid, int[][] nearest) {
		if(grid[sx][sy] != 0 || grid[ex][ey] != 0) return null;
		
		PriorityQueue<Grid> pq = new PriorityQueue<>(10, (Grid a, Grid b) -> a.score - b.score);
		pq.add(new Grid(sx, sy, ' ', 0, 0, null));
		
		boolean[][] visited = new boolean[630][1030];
		while(pq.size() > 0) {
			Grid curr = pq.poll();
			if(visited[curr.x][curr.y]) continue;
			if(curr.x == ex && curr.y == ey) return curr;
			visited[curr.x][curr.y] = true;
			
			if(curr.x > 0 && !visited[curr.x-1][curr.y] && grid[curr.x-1][curr.y] == 0) {
				int eucDist =(int) Math.sqrt(Math.pow(ex-(curr.x-1), 2)+Math.pow(ey-curr.y, 2));
				int nextScore = eucDist + curr.dist+1 + 100*(10-nearest[curr.x-1][curr.y]);
				//change this ratio ^
				if(curr.dir=='U'||curr.dir=='D') nextScore += 100;
				pq.add(new Grid(curr.x-1, curr.y, 'L', nextScore, curr.dist+1, curr));
			}
			
			if(curr.x+1 < grid.length && !visited[curr.x+1][curr.y] && grid[curr.x+1][curr.y] == 0) {
				int eucDist =(int) Math.sqrt(Math.pow(ex-(curr.x+1), 2)+Math.pow(ey-curr.y, 2));
				int nextScore = eucDist + curr.dist+1 + 100*(10-nearest[curr.x+1][curr.y]);
				//change this ratio ^
				if(curr.dir=='U'||curr.dir=='D') nextScore += 100;
				pq.add(new Grid(curr.x+1, curr.y, 'R', nextScore, curr.dist+1, curr));
			}
			
			if(curr.y > 0 && !visited[curr.x][curr.y-1] && grid[curr.x][curr.y-1] == 0) {
				int eucDist =(int) Math.sqrt(Math.pow(ex-curr.x, 2)+Math.pow(ey-(curr.y-1), 2));
				int nextScore = eucDist + curr.dist+1 + 100*(10-nearest[curr.x][curr.y-1]);
				//change this ratio ^
				if(curr.dir=='L'||curr.dir=='R') nextScore += 100;
				pq.add(new Grid(curr.x, curr.y-1, 'D', nextScore, curr.dist+1, curr));
			}
			
			if(curr.y+1 < grid[0].length && !visited[curr.x][curr.y+1] && grid[curr.x][curr.y+1] == 0) {
				int eucDist =(int) Math.sqrt(Math.pow(ex-curr.x, 2)+Math.pow(ey-(curr.y+1), 2));
				int nextScore = eucDist + curr.dist+1 + 100*(10-nearest[curr.x][curr.y+1]);
				//change this ratio ^
				if(curr.dir=='L'||curr.dir=='R') nextScore += 100;
				pq.add(new Grid(curr.x, curr.y+1, 'U', nextScore, curr.dist+1, curr));
			}
		}
		
		return null;
	}
	
	static class Grid {
		int x,y;
		char dir;
		int score;
		int dist;
		Grid prev;
		
		public Grid(int xx, int yy, char d, int s, int di, Grid p) {
			x=xx;
			y=yy;
			dir=d;
			score=s;
			dist=di;
			prev=p;
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