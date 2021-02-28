package PathFinding;

import java.io.*;
import java.util.*;

public class AStarAlg {

	public static void main(String[] args) throws IOException {
		int[][] graph = load("C:\\Allan\\intermediate\\testGraph.csv");
		int[][] nearest= load("C:\\Allan\\intermediate\\nearestGraph.csv");

		Grid last = findPath(489, 402, 569, 313, graph, nearest);
		
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
		
		double totalDist = Math.abs(sx-ex) + Math.abs(sy-ey);
		double maxNearest = 10.0;
		
		double WDIST = 0.5;
		double WNEAR = 0.3;
		double WTURN = 0.2;
		
		Comparator<Grid> comparator = new GridComparator();
		PriorityQueue<Grid> pq = new PriorityQueue<>(10, comparator);
		pq.add(new Grid(sx, sy, ' ', 0, 0, null));
		
		boolean[][] visited = new boolean[630][1030];
		while(pq.size() > 0) {
			Grid curr = pq.poll();
			if(visited[curr.x][curr.y]) continue;
			if(curr.x == ex && curr.y == ey) return curr;
			visited[curr.x][curr.y] = true;
			
			if(curr.x > 0 && !visited[curr.x-1][curr.y] && grid[curr.x-1][curr.y] == 0) {
				int manDist = Math.abs(curr.x-1-ex) + Math.abs(curr.y-ey);
				int turn = 0;
				if(curr.dir=='U'||curr.dir=='D') turn = 1;
//				double nextScore = ((manDist+curr.dist+1.0)/(totalDist*2))*WDIST + ((maxNearest-nearest[curr.x-1][curr.y])/maxNearest)*WNEAR + turn*WTURN;   
				double nextScore = ((curr.dist+1.0)/totalDist)/2 + ((manDist/totalDist)*WDIST + ((maxNearest-nearest[curr.x-1][curr.y])/maxNearest)*WNEAR + turn*WTURN)/2;
				pq.add(new Grid(curr.x-1, curr.y, 'L', nextScore, curr.dist+1, curr));
			}
			
			if(curr.x+1 < grid.length && !visited[curr.x+1][curr.y] && grid[curr.x+1][curr.y] == 0) {
				int manDist = Math.abs(curr.x+1-ex) + Math.abs(curr.y-ey);
				int turn = 0;
				if(curr.dir=='U'||curr.dir=='D') turn = 1;
//				double nextScore = ((manDist+curr.dist+1.0)/(totalDist*2))*WDIST + ((maxNearest-nearest[curr.x+1][curr.y])/maxNearest)*WNEAR + turn*WTURN;
				double nextScore = ((curr.dist+1.0)/totalDist)/2 + ((manDist/totalDist)*WDIST + ((maxNearest-nearest[curr.x+1][curr.y])/maxNearest)*WNEAR + turn*WTURN)/2;
				pq.add(new Grid(curr.x+1, curr.y, 'R', nextScore, curr.dist+1, curr));
			}
			
			if(curr.y > 0 && !visited[curr.x][curr.y-1] && grid[curr.x][curr.y-1] == 0) {
				int manDist = Math.abs(curr.x-ex) + Math.abs(curr.y-1-ey);
				int turn = 0;
				if(curr.dir=='L'||curr.dir=='R') turn = 1;
//				double nextScore = ((manDist+curr.dist+1.0)/(totalDist*2))*WDIST + ((maxNearest-nearest[curr.x][curr.y-1])/maxNearest)*WNEAR + turn*WTURN;
				double nextScore = ((curr.dist+1.0)/totalDist)/2 + ((manDist/totalDist)*WDIST + ((maxNearest-nearest[curr.x][curr.y-1])/maxNearest)*WNEAR + turn*WTURN)/2;
				pq.add(new Grid(curr.x, curr.y-1, 'D', nextScore, curr.dist+1, curr));
			}
			
			if(curr.y+1 < grid[0].length && !visited[curr.x][curr.y+1] && grid[curr.x][curr.y+1] == 0) {
				int manDist = Math.abs(curr.x-ex) + Math.abs(curr.y+1-ey);
				int turn = 0;
				if(curr.dir=='L'||curr.dir=='R') turn = 1;
//				double nextScore = ((manDist+curr.dist+1.0)/(totalDist*2))*WDIST + ((maxNearest-nearest[curr.x][curr.y+1])/maxNearest)*WNEAR + turn*WTURN;
				double nextScore = ((curr.dist+1.0)/totalDist)/2 + ((manDist/totalDist)*WDIST + ((maxNearest-nearest[curr.x][curr.y+1])/maxNearest)*WNEAR + turn*WTURN)/2;
				pq.add(new Grid(curr.x, curr.y+1, 'U', nextScore, curr.dist+1, curr));
			}
		}
		
		return null;
	}
	
	static public class GridComparator implements Comparator<Grid> {
	    @Override
	    public int compare(Grid x, Grid y) {
	    	if(x.score < y.score) return -1;
	    	if(x.score > y.score) return 1;
	    	return 0;
	    }
	    
	}
	
	static class Grid {
		int x,y;
		char dir;
		double score;
		int dist;
		Grid prev;
		
		public Grid(int xx, int yy, char d, double s, int di, Grid p) {
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