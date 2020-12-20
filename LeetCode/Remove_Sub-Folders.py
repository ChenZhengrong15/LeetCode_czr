# coding:UTF-8
# 移除folder列表中的子目录


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result, sub = [], ''
        for f in sorted(folder):
            if not f.startwith(sub):
                result.append(f)
                sub = f + '/'
        return result
