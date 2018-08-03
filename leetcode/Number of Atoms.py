class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        cache = {}

        def slave(formula_slice, count):

            str_l = len(formula_slice)
            if str_l == 0:
                return
            left = []
            right = []
            times = []
            result_slice = ''

            tmp = 0
            i = 0
            while i < str_l:
                if formula_slice[i] == '(':
                    tmp += 1
                    if tmp == 1:
                        left.append(i)
                elif formula_slice[i] == ')':
                    tmp -= 1
                    if tmp == 0:
                        right.append(i)
                        time_len = 0
                        for j in range(i + 1, str_l):
                            if not formula_slice[j].isdigit():
                                break
                            else:
                                time_len += 1
                        time = int(formula_slice[i + 1: i + time_len + 1]) if formula_slice[i + 1: i + time_len + 1] else 1
                        times.append(time)
                        i += time_len
                elif tmp == 0:
                    result_slice += formula_slice[i]
                i += 1

            if left:
                for i in range(len(left)):
                    slave(formula_slice[left[i] + 1: right[i]], count * times[i])

            if not result_slice:
                return
            result_slice += 'Q'
            atoms = None
            num = 0

            for i in range(len(result_slice)):

                if result_slice[i].isalpha():
                    if result_slice[i].isupper():
                        if atoms:
                            if num == 0:
                                num = 1
                            cache[atoms] = cache[atoms] + num * count if cache.get(atoms, '') else num * count
                        atoms = result_slice[i]
                        num = 0
                    else:
                        atoms += result_slice[i]
                else:
                        num = num * 10 + int(result_slice[i])

        slave(formula, 1)

        result = ''
        order_key = sorted([key for key in cache.keys()])
        for key in order_key:
            result += key
            if cache[key] > 1:
                result += str(cache[key])

        return result


a = Solution()
test = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
test1 = "K4(ON(SO3)2)2"
test2 = "H11He49NO35B7N46Li20"
print(a.countOfAtoms(test2))





