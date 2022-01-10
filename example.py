from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)
import filecmp
def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
    f_write = open('test_fa_temp.txt', 'w')
    f_read = open("./data/test.fa", 'r')
    parser = FastaParser("./data/test.fa")
    for p in parser: 
        #print(p)
        name = p[0]
        seq = p[1]
        L = [name, seq]
        f_write.writelines(L)
    f_write.close()
    print(filecmp.cmp('test_fa_temp.txt', "./data/test.fa"))

    # myTup = ('','','')
    # myStr = ''.join(myTup)
    # if not myStr:
    #     print("Empty")
    # else:
    #     print("Full")

    # with open("./data/test.fa", "r") as f_obj:
    #         f_obj.seek(0)
    #         while True:
    #             # header = f_obj.readline()
    #             # seq = f_obj.readline()
    #             # if header == '':
    #             #     break
    #             # print (header, seq)
    #             header = f_obj.readline()
    #             seq = f_obj.readline()
    #             print (header, seq)
                    
    #             except: 
    #                 f_obj.close()
    #                 print("End of File")
    #                 break
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
