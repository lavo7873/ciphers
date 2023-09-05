import subprocess

#  cipher text
cipher_text = "qbqxfyvyu lnso q anfqo sl uqyaqml izf unfr wqiimvyu izf wqmnsu lnsas wquuvyj qya zvj lnvfya jqobvjf uqouff lvya izfojfmgfj msji vy izf fory ohvm yfqn osnasn qya jssy wfesof qbqnf izqi izfr qnf wfvyu jiqmxfa wr usmmho izf lsnofn sbyfn sl izf syf nvyu qlifn eqkihnvyu zvo q jrokqizfive lnsas afevafj is hjf usmmho qj q uhvaf is osnasn afjkvif jqoj swdfeivsyj" 
# List of cipher types to try
cipher_types = [
    "-aes-128-cbc",
    "-aes-256-cbc",
    "-bf-cbc",

]

# Full path to the openssl executable
openssl_path = "C:/Users/Public/Github/ciphers/ciphertext-o2.txt"  # Replace with the actual path

# Loop through each cipher type and perform encryption using openssl command
for cipher_type in cipher_types:
    output_file = f"cipher_{cipher_type}.bin"
    command = (
        f'echo "{cipher_text}" | {openssl_path} enc {cipher_type} -e -out {output_file} '
        f'-K 00112233445566778889aabbccddeeff -iv 0102030405060708'
    )

    subprocess.run(command, shell=True)
    print(f"Encrypted using {cipher_type}: {output_file}")
