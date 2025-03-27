def main():
    path = "books/frankenstein.txt"
    print(sort_dic(path=path))

def get_book_txt(path):
    with open(path) as file:
        txt_str = file.read()
    return txt_str    

def get_num_words(path):
    return len(get_book_txt(path).split())

def get_character_dic(txt_str):
    txt_str = txt_str.lower()
    char_dic = {}
    for char in txt_str:
        if char.isalpha():            
            if char not in char_dic:
                char_dic[char] = 1
            else :
                char_dic[char] +=1
    return char_dic      

def sort_dic(dic=None,path=None):
    if path:        
        dic = get_character_dic(get_book_txt(path))
    return sorted(dic.items(),key=lambda kv: kv[1],reverse=True)

if __name__ == "__main__":
    main() 