converting to binary:

echo "that thing" | xxd -r -p > program

opening it in godbolt gives the plaintext secret, now need to figure how to do it within the time constraint

Nvm plaintext secret is provided at the beginning of the welcome message
write script to take that line and do it 20 times

TIP: not using .strip() was causing issues with the key

picoCTF{4u7o_r3v_g0_brrr_78c345aa}
