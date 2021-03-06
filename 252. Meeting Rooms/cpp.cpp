<<<<<<< HEAD
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), compare);
        int n = intervals.size();
        for (int i = 0; i < n - 1; i++)
            if (overlap(intervals[i],intervals[i+1]))
                return false;
        return true;
    }
private:
    static bool compare(Interval& o1, Interval& o2) {
        return o1.start < o2.start;
    }
    bool overlap(Interval& o1, Interval& o2){
        return o1.end > o2.start;
    }
=======
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), compare);
        int n = intervals.size();
        for (int i = 0; i < n - 1; i++)
            if (overlap(intervals[i],intervals[i+1]))
                return false;
        return true;
    }
private:
    static bool compare(Interval& o1, Interval& o2) {
        return o1.start < o2.start;
    }
    bool overlap(Interval& o1, Interval& o2){
        return o1.end > o2.start;
    }
>>>>>>> eb4f20642d79ed3df07dab1830859263475bf5e5
};