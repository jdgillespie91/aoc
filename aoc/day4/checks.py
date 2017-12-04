def contains_no_anagrams(l):
    for index, element in enumerate(l):
        for otherElement in l[index + 1:]:
            if is_anagram(element, otherElement):
                return False
    return True


def is_anagram(str_a, str_b):
    return ''.join(sorted(str_a)) == ''.join(sorted(str_b))


def contains_unique_elements(l):
    return True if len(l) == len(set(l)) else False
