from collections import Counter

def frequency_analysis(ciphertext):
    # Count frequency of each character in the ciphertext
    freq_counter = Counter(ciphertext)
    
    # Remove spaces from the frequency count
    if ' ' in freq_counter:
        del freq_counter[' ']
        
    # Sort the characters by frequency
    sorted_freq = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)
    
    # Display the sorted frequency
    print("Character Frequency Analysis:")
    for char, freq in sorted_freq:
        print(f"{char}: {freq}")
        
    return sorted_freq

# Your ciphertext
ciphertext = "qbqxfyvyu lnso q anfqo sl uqyaqml izf unfr wqiimvyu izf wqmnsu lnsas wquuvyj qya zvj lnvfya jqobvjf uqouff lvya izfojfmgfj msji vy izf fory ohvm yfqn osnasn qya jssy wfesof qbqnf izqi izfr qnf wfvyu jiqmxfa wr usmmho izf lsnofn sbyfn sl izf syf nvyu qlifn eqkihnvyu zvo q jrokqizfive lnsas afevafj is hjf usmmho qj q uhvaf is osnasn afjkvif jqoj swdfeivsyj"

# Run frequency analysis
sorted_frequency = frequency_analysis(ciphertext)
