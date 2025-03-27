from stats import sort_dic,get_num_words
import sys
import os
def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        print("File path doesn't exit")   
        exit(1)
    path = sys.argv[1]
    print(f"============ BOOKBOT ============\n\
Analyzing book found at {path}...\n\n\
----------- Word Count ----------\n\
Found {get_num_words(path)} total words\n\n\
--------- Character Count -------")
    ch_ls = sort_dic(path=path)
    for ch_t in ch_ls:
        print(f"{ch_t[0]}: {ch_t[1]}")














if __name__ == "__main__":
    main()        
