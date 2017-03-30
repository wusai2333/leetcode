public class Solution {
	public String removeKdigits(String num, int k)
	{
		int digits = num.length() - k;

		char[] stk = new char[digits];
		int top = 0;
		// k keeps track of how many characters we remove;
		// if the previous character in stk is larger than the current one
		// then removing it will get a smaller number
		// but we can only do it when k is larger than 0
		for (int i = 0; i < num.length(); i++)
		{
			char c = num.charAt(i);
			while (top > 0 && k > 0 && stk[top-1] > c)
			{
				k -= 1;
				top -= 1;
			}
			stk[top++] = c;
		}
		// find the index of the first non-zero value
		int idx = 0;
		while (idx < digits && stk[idx] == '0') { idx++; }
		return (idx == digits ? "0" : new String(stk, idx, digits - idx));
	}
}
