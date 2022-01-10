# write tests for parsers

import filecmp

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    f_write = open('test_fa_temp.txt', 'w')

    parser = FastaParser("./data/test.fa")
    for p in parser: 
        name = p[0]
        seq = p[1]
        L = [name, seq]
        f_write.writelines(L)
    f_write.close()

    assert filecmp.cmp('test_fa_temp.txt', "./data/test.fa")


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    f_write = open('test_fq_temp.txt', 'w')

    parser = FastqParser("./data/test.fq")
    for p in parser: 
        name = p[0]
        seq = p[1]
        qual = p[2]
        L = [name, seq, "+\n", qual]
        f_write.writelines(L)
    f_write.close()

    assert filecmp.cmp('test_fq_temp.txt', "./data/test.fq")
