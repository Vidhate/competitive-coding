# https://leetcode.com/contest/biweekly-contest-77/problems/count-unguarded-cells-in-the-grid/

from typing import List
class Solution:

    def closest(self, anchor, options):
        if options is None:
            return None, None
        less, more = [anchor-op for op in options if op<=anchor], [op-anchor for op in options if op>anchor]
        mini = None if len(less)==0 else min(less)
        maxi = None if len(more)==0 else min(more)
        res = [mini, maxi]
        if not mini is None:
            res[0] = anchor-res[0]
        if not maxi is None:
            res[1]-=anchor

        return res

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        guards_row, guards_col = {}, {}
        walls_row, walls_col = {}, {}

        for guard in guards:
            if guards_row.get(guard[0], None) is None:
                guards_row[guard[0]] = [guard[1]]
            else:
                guards_row[guard[0]].append(guard[1])

            if guards_col.get(guard[1], None) is None:
                guards_col[guard[1]] = [guard[0]]
            else:
                guards_col[guard[1]].append(guard[0])

        for wall in walls:
            if walls_row.get(wall[0], None) is None:
                walls_row[wall[0]] = [wall[1]]
            else:
                walls_row[wall[0]].append(wall[1])

            if walls_col.get(wall[1], None) is None:
                walls_col[wall[1]] = [wall[0]]
            else:
                walls_col[wall[1]].append(wall[0])

        count = 0
        for row in range(m):
            for col in range(n):

                if row in guards_row.keys() and col in guards_row[row]:
                    continue
                if row in walls_row.keys() and col in walls_row[row]:
                    continue


                guards_in_row, guards_in_col = guards_row.get(row, None), guards_col.get(col, None)
                walls_in_row, walls_in_col = walls_row.get(row, None), walls_col.get(col, None)

                lg, rg = None, None if guards_in_row is None else self.closest(col, guards_in_row)
                ug, dg = None, None if guards_in_col is None else self.closest(row, guards_in_col)
                lw, rw = None, None if walls_in_row is None else self.closest(col, walls_in_row)
                uw, dw = None, None if walls_in_col is None else self.closest(col, walls_in_col)

                if lg is None and rg is None and ug is None and dg is None:
                    count+=1
                    continue

                if ((lg is None) or (not lg is None and not lw is None and lw>lg)) and ((rg is None) or (not rg is None and not rw is None and rw<rg)) and ((ug is None) or (not ug is None and not uw is None and uw>ug)) and ((dg is None) or (not dg is None and not dw is None and dw<dg)):
                    count+=1

        return count

s = Solution()
print(s.countUnguarded(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]]))