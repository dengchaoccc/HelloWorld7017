'''
2025年10月23日
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true
'''

#统计每个字符串里，每个字符出现的次数
'''
知识点：如果一个类里定义的函数，你要调用同类中函数，需要使用self.xxxxx()调用
不能直接写函数
'''
def count_alpha(input_str, output_ditc):
    for char in input_str:
        if output_ditc.get(char, 0) == 0:
            output_ditc[char] = 1
        else:
            output_ditc[char] += 1

    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
def canConstruct(ransomNote, magazine):

    ransom_dic = {}
    magazine_dic = {}

    #知识点：如果想要调用类里定义的函数，需要这么写self.count_alpha()
    count_alpha(ransomNote, ransom_dic)
    count_alpha(magazine, magazine_dic)

    for key, value in ransom_dic.items():
        #确认每个在magazine里的字符，都可以在ransom里找到对应的个数
        if magazine_dic.get(key, 0) < value:
            return False

    return True

def test_two_strings():
    ransomNote = "aa"
    magazine = "aab"
    result = canConstruct(ransomNote,magazine)
    print(f"ransoNoed = {ransomNote}, magazine={magazine}, result={result}")

test_two_strings()