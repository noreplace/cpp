#ifndef AES_H
#define AES_H
#include <openssl/evp.h>
#include <openssl/rand.h>

#include <string>
#include <cstring>

int decryptFile(const std::string& inputFilePath, const std::string& outputFilePath,
                const unsigned char* key, const unsigned char* iv);
bool generateKeyAndIv(unsigned char* key, unsigned char* iv);
void handleErrors();
int encryptFile(const std::string& inputFilePath, const std::string& outputFilePath,
                const unsigned char* key, const unsigned char* iv);
bool saveKeyAndIvToFile(const std::string& filename, const unsigned char* key, const unsigned char* iv);
bool loadKeyAndIvFromFile(const std::string& filename, unsigned char* key, unsigned char* iv);
#endif // AES_H
