https://github.com/lucadentella/TOTP-Arduino

https://github.com/maniacbug/Cryptosuite


uint8_t hmacKey[] = {0x4d, 0x79, 0x4c, 0x65, 0x67, 0x6f, 0x44, 0x6f, 0x6f, 0x72};


TOTP(uint8_t* hmacKey, int keyLength, int timeStep);


char* getCode(long timeStamp);
