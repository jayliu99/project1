# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    return seq.replace("T", "U")


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    rna = transcribe(seq)

    # Reverse the sequence
    for i in range(len(rna)):
        if rna[i] == 'A': rna[i] = 'U'
        elif rna[i] == 'U': rna[i] = 'A'
        elif rna[i] == 'C': rna[i] = 'G'
        else: rna[i] = 'C'

    return rna