Readme

32-bit hash of a file is created according to the following specifications:
1. Initialize the hash to all zeros;
2. Scan the file one byte at a time
3. Before a new byte is read from the file, circularly shift the bit pattern
to the left by 4 positions;
4. XOR the new byte from the file with the least significant byte of the hashmap
5. Scan directory to create hash of all the files.
6. Write another script to check for any collisions (Collision check).
