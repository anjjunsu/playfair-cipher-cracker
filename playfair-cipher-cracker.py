import itertools
from ftlangdetect import detect

def is_english_language(text):
    language_code = detect(text=text, low_memory=False)
    target_language_code = 'en'

    if target_language_code == language_code['lang'] and language_code['score'] > 0.9:
        return True

def create_matrix(key):
    matrix = []
    for i in range(5): 
        row = []
        for j in range(5):  
            row.append(key[i*5 + j])
        matrix.append(row)
    return matrix

def decrypt_playfair(ciphertext, matrix):
    def find_position(letter):
        for row in range(5):
            for column in range(5):
                if matrix[row][column] == letter:
                    return row, column

    def decrypt_digraph(digraph):
        row1, col1 = find_position(digraph[0])
        row2, col2 = find_position(digraph[1])

        if row1 == row2: 
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  
            return matrix[row1][col2] + matrix[row2][col1]

    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'  

    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_digraph(ciphertext[i:i+2])

    return plaintext

cipher_text = "SUUVQPUQXOBFXKQPZGKSPMVSQPVXVARNNBIPZPATZNONZFIYGITZZCQPRKKQWFAXUOIYGITZYWYZZPEPRTGZYNMITZRPPBRKGAQIMITZYWYZZPQPVERTGZOPZCEVSUGNQPZXYPVYFZZBFIZIBTQKMITZSVTNFWKLLZAVMRULKMSKQPBPMRWANWVNONBFWUZBMVITRPOQKMZFSUGNQPAVAZAVVEVYYABTMDIYGITZEPMUVURPPBUVVSIYGITZYWXISQBPZVXAUVMIRPPLSCPOVIMIIYPNZNXAPBUYPMUQVIUIXKQXVIUIPMVRWXMITZWNRDZURTHPVUQPBFSZFWHIMITZRNBWGBIYGITZQPVAZVVPVYYNPWNOHIMITZRPPLFWWAHFSULRKIGBFWPTRWKPBRPNZGPWPBZKLEBFXKRIWXVUXAYNMITZRPFKSUUVQPRWMKGNLQAWBFXKRPRMFWYNVUXAUPRMQPAVAZZPIRTEVNVANRNRGKQKMITZRPPKYIBGTBVANIAFNRZIBTQDUMBFVLXKQPVXUVRKHKMITZNWGKGBPBHQKQRIWXBGTBYNMITZYWAVAGFWPEISQUIYLKFLMSKIZPZVXAVSQPMZVXVARNYWNOQBXKHFRTMZWXMITZISQFQRAXVYQFMRNYODPWCRULKMSKXTXKNMFDRNSHRMNMZBPOABHWBFWURNTRDHVIVUXKQPZGKSBKZVPGFWDGVIVUIYGITZPVMIYWXIPWTBFKFBUTBFSUACXKMRQPZFTZGKQKMITZPBUNSYGBSUQAFWKPVURMWQPMVIUSXKQPBFVIVUZBRWKPMUUIBFRTVYKPIYGITZFSWXVYKBFZAXRMSCXTULGNQPVXVARNTVWRATZNONZVXAGVUOZSFBSUNPRMRNVAAXVUWPVYFZAUUIAGFWAURZHFZAAFVSDGRNIYRKNTRQPWNTABHWBFMRQPVFBFXVVSQPZFCUXKBTKBNOWXMNRIFHRMQPZFRKPWBUBNBFQPAFMUZABKRPSKPNRZTVWRTZFIHIMITZZCQPMKGNLQWXTRICPORKKXXTQPUVVLSCLPRMVGAXQPVXTRFIHZZPIRLTVAAXIYGITZSVTNFWDOCPBPULTPBFQPAGRSZMPGFWMUXTUKBPZFRKMNQLFWQYAVAGFWPZGZTVWRIYMUTNUZZFVFAXVGAVQYFWVASUMRKIAGFWSYODWFBPWAAXARXKGAHKMITZULGNQPZFRKUKSZGAVAPLFWARXKNRKPQPAVZNIPZBFSBFNMBZWRIYGITZRPPKYZQPWFVYFZZBPZFHLKTBKPTVWRZPVGAVRQSCXTBGFZSUQAFWPRRKGAQIZTAGFWVAMRMKGVFSAZZPWRVYXTIYGITZATAGQRZCEVSUGNQPZFRKRPHBXKHSBPHWRPXVHSAVIYGITZMRUSRMQPWVPWPLBNAXQPZFARUNGBPVMIFWVAVWPZKPGBPGQPZGZPUZAVTVWRQPWVPWPLBNAXQPAVBFPVMIFWYNFWBXPZKPMKDFIYGITZRPPLFWQYAVVXTRRWMDUSRMFSAZZPQPXKRPFLBRPNIYGITZRPPKVGAVZIKMBFIRBHRMYWAXSUUVQPQHMITZYWYZZPRPVUDSRPIYGITZSXOPQNZTAGYSAVIYGITZBRPNZGPWBUVFAXZMPMRTLQBFWUQPWXSCKBDMBRQFGATNPWMPFWZYLKHFNYABTZKPATZFFSAVPWKPRDRIFWYPABTNYWAXVGAVSUUVQPOHGZVNUORVXIAVABHWBFFWVARTPZKPFSZFMNGKGKMUUIBFRNQPBGNMLQVXNOQBNMWYRIFBTNPWMPFWIYLKHPXKPBCRQPXKTLUMBRQFRNSULRKIGBFWPTRCVGAVTBVLFWFKSUQPAZVUXBHSRTHPUVGIIMTPXKTLKMTKXMPQRPFKSKPKRMCKYZYWRNSMQYZPSUQPAZZPTVWRBTZMIYGITZPVMISCDMRILEABUPMRSCPOVYQFZURMHIMITZRPHSBGVIUIBFPMAVPRKPZMGBTIIYGITZRPPURTBGOHSRXBSUMNQAZPMRMRQPRNTZFBSUUVQPUQBRQFIYGITZRPHFERBFFWVPUVGTUVZCXTZPTVWRZPFWUVQPAVDOVNUVRKSKXTFHRMMRMRZBPIRMTVWRFWZBPZMKGNLQAWTBICSUQXMITZZCQPMUXTZSKDQWZNTRKPZIBTKUTBICWVZFQPRNQAXKDKBFGZVNONQURIZXQPAVZSFBVSSCFPRKCRIYGITZZAAXMZBFRMMRMRDTWRBFBTKBWRMUXTIYGITZRPFKSUUVQPRHTBVWHBNMFCSCQIMITZRPBKVRBFSCLSABUTUHRMMRPBQHMITZSYZAGVYNMITZQPWVZAVAIRNATBOCXTSULRKIGBFWPTOHRNRDRIQPBFVIVUPMAFRPBKVIUIBFRPNXVYDMRWGNQPZFCUIYGITZYWXIWYZPVGAXTVWRAVQPRPODRBKBRMSUUVQPOHMRUSXKQPBFVIVUZCQPMRMRXKFWTROTHIMITZRPBKVIUIBFRNQPZFCUMRUSRMBRPNZGZBHZZPSCXTQPBFSZFWFHRMPVMIQPVERTIRTNPQFWQWABUPBTYZZBKMVSQPAZXKHKMITZRPBLKIGBFWPTRWKPSUUVQPQHVYKBFZAZFWVAQPBGRIXFTVZPDZYZBFXKZBGVDZVEVUAGFWIYISXTPMVUGI"

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
keys = itertools.permutations(alphabet, 25)
small_count = 0

# Brute force
for key in keys:
    matrix = create_matrix(key)
    plaintext = decrypt_playfair(cipher_text, matrix)
    if is_english_language(plaintext):
        with open('decryption_results.txt', 'a') as file:
            file.write(f"Key: {''.join(key)}\nPlaintext: {plaintext}\nscore:\n")

    small_count += 1
    print("." * small_count)
    if small_count == 100:
        small_count = 0
