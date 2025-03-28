#include <openssl/evp.h>
#include <openssl/rand.h>
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

// Функция для обработки ошибок
void handleErrors() {
    std::cout << "Произошла ошибка" << std::endl;
    abort();
}

// Функция для шифрования файла
int encryptFile(const std::string& inputFilePath, const std::string& outputFilePath,
                const unsigned char* key, const unsigned char* iv) {
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        handleErrors();
    }

    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        handleErrors();
    }

    std::ifstream inFile(inputFilePath, std::ios::binary | std::ios::in);
    if (!inFile.is_open()) {
        std::cerr << "Не удалось открыть файл для чтения: " << inputFilePath << std::endl;
        return 1;
    }

    std::ofstream outFile(outputFilePath, std::ios::binary | std::ios::out);
    if (!outFile.is_open()) {
        std::cerr << "Не удалось создать файл для записи: " << outputFilePath << std::endl;
        return 1;
    }

    // Буфер для чтения и записи
    constexpr size_t bufferSize = 1024;
    unsigned char buffer[bufferSize];
    int readBytes, writtenBytes;

    while ((readBytes = inFile.readsome(reinterpret_cast<char*>(buffer), bufferSize))) {
        if (readBytes <= 0) {
            break;
        }

        if (EVP_EncryptUpdate(ctx, buffer, &writtenBytes, buffer, readBytes) != 1) {
            handleErrors();
        }

        outFile.write(reinterpret_cast<const char*>(buffer), writtenBytes);
    }

    if (EVP_EncryptFinal_ex(ctx, buffer, &writtenBytes) != 1) {
        handleErrors();
    }

    outFile.write(reinterpret_cast<const char*>(buffer), writtenBytes);

    EVP_CIPHER_CTX_free(ctx);
    inFile.close();
    outFile.close();

    return 0;
}

// Функция для дешифрования файла
int decryptFile(const std::string& inputFilePath, const std::string& outputFilePath,
                const unsigned char* key, const unsigned char* iv) {
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        handleErrors();
    }

    if (EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        std::cout << "тут ошибка" << std::endl;
        handleErrors();
    }

    std::ifstream inFile(inputFilePath, std::ios::binary | std::ios::in);
    if (!inFile.is_open()) {
        std::cerr << "Не удалось открыть файл для чтения: " << inputFilePath << std::endl;
        return 1;
    }

    std::ofstream outFile(outputFilePath, std::ios::binary | std::ios::out);
    if (!outFile.is_open()) {
        std::cerr << "Не удалось создать файл для записи: " << outputFilePath << std::endl;
        return 1;
    }

    // Буфер для чтения и записи
    constexpr size_t bufferSize = 1024;
    unsigned char buffer[bufferSize];
    int readBytes, writtenBytes;

    while ((readBytes = inFile.readsome(reinterpret_cast<char*>(buffer), bufferSize))) {
        if (readBytes <= 0) {
            break;
        }

        if (EVP_DecryptUpdate(ctx, buffer, &writtenBytes, buffer, readBytes) != 1) {
            std::cout << "тут ошибка 104" << std::endl;
            handleErrors();
        }

        outFile.write(reinterpret_cast<const char*>(buffer), writtenBytes);
    }

    int padding = 0;
    if (EVP_DecryptFinal_ex(ctx, buffer, &padding) != 1) {
        std::cout << "тут ошибка 113" << std::endl;
        handleErrors();
    }

    outFile.write(reinterpret_cast<const char*>(buffer), padding);

    EVP_CIPHER_CTX_free(ctx);
    inFile.close();
    outFile.close();

    return 0;
}

// Генерация ключа и IV
bool generateKeyAndIv(unsigned char* key, unsigned char* iv) {
    RAND_bytes(key, 32);  // 256 битный ключ
    RAND_bytes(iv, 16);   // 128 битный IV

    return true;
}

// Функция для сохранения ключа и IV в файл
bool saveKeyAndIvToFile(const std::string& filename, const unsigned char* key, const unsigned char* iv) {
    std::ofstream keyIvFile(filename, std::ios::binary | std::ios::out);
    if (!keyIvFile.is_open()) {
        std::cerr << "Не удалось создать файл для записи ключа и IV: " << filename << std::endl;
        return false;
    }

    keyIvFile.write(reinterpret_cast<const char*>(key), 32);
    keyIvFile.write(reinterpret_cast<const char*>(iv), 16);

    keyIvFile.close();
    return true;
}

// Функция для загрузки ключа и IV из файла
bool loadKeyAndIvFromFile(const std::string& filename, unsigned char* key, unsigned char* iv) {
    std::ifstream keyIvFile(filename, std::ios::binary | std::ios::in);
    if (!keyIvFile.is_open()) {
        std::cerr << "Не удалось открыть файл с ключом и IV: " << filename << std::endl;
        return false;
    }

    keyIvFile.read(reinterpret_cast<char*>(key), 32);
    keyIvFile.read(reinterpret_cast<char*>(iv), 16);

    keyIvFile.close();
    return true;
}


