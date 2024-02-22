def transform(chain):
    try:
        nums = list(set(map(int, chain[0].split() + chain[1].split())))
        nums.sort()
        result_str = ' '.join(map(str, nums))
        result_str = f"{result_str} -sie alassane coulibaly master 1 AI"
        return result_str
    except ValueError:
        return None
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out)
    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out)

