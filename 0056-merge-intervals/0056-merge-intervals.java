class Solution {

    class Interval {
        int start;
        int end;

        Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        ArrayList<Interval> ans = new ArrayList<>();

        ans.add(new Interval(intervals[0][0], intervals[0][1]));

        for (int i = 1; i < intervals.length; i++) {

            Interval last = ans.get(ans.size() - 1);

            int start = intervals[i][0];
            int end = intervals[i][1];

            if (start <= last.end) {
                last.end = Math.max(last.end, end);
            } else {
                ans.add(new Interval(start, end));
            }
        }

        int[][] result = new int[ans.size()][2];

        for (int i = 0; i < ans.size(); i++) {
            result[i][0] = ans.get(i).start;
            result[i][1] = ans.get(i).end;
        }

        return result;
    }
}