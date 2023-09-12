#!/bin/sh

openssl enc -aes-128-cbc -e -in plain.txt -out cipher-aes-128-cbc.bin \
-K 00112233445566778889aabbccddeeff \
-iv 0102030405060708
openssl enc -bf-cbc -e -in plain.txt -out cipher-bf-cbc.bin \
-K 00112233445566778889aabbccddeeff \
-iv 0102030405060708
openssl enc -aes-128-cfb -e -in plain.txt -out cipher-bf-cfb.bin \
-K 00112233445566778889aabbccddeeff \
-iv 0102030405060708

openssl enc -aes-128-cbc -e -in pic_original.bmp -out pic_cbc.bmp \
-K 00112233445566778889aabbccddeeff \
-iv 0102030405060708

openssl enc -aes-128-ecb -e -in pic_original.bmp -out pic_ecb.bmp \
-K 00112233445566778889aabbccddeeff \
-iv 0102030405060708