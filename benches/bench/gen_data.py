#!/usr/bin/env python3

import random

ROOT = "benches/bench"

enc_rs = []
dec_rs = []
for i in [32, 256, 2048, 16384, 131072, 1048576]:
    data = bytearray([random.randint(0, 255) for _ in range(i)])
    data_bin_fname = f"data_{i}.bin"
    open(f"{ROOT}/{data_bin_fname}", "wb").write(data)
    data_hex_fname = f"data_{i}.hex"
    open(f"{ROOT}/{data_hex_fname}", "wt").write(data.hex())

    enc_rs.append(
        f'pub const ENC_{i}: &[u8; {i}] = include_bytes!("./{data_bin_fname}");'
    )
    dec_rs.append(f'pub const DEC_{i}: &str = include_str!("./{data_hex_fname}");')

enc_rs = "\n".join(enc_rs)
dec_rs = "\n".join(dec_rs)
data_rs = f"""\
// @generated by gen_data.py, do not modify manually

{enc_rs}

{dec_rs}
"""
open(f"{ROOT}/data.rs", "w").write(data_rs)
