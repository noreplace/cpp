#include <iostream>
#include <string>
#include <cstdio>
#include <iconv.h>
#include "coding.h"

std::string detect_encoding(const std::string& file_path) {
    FILE* fp = fopen(file_path.c_str(), "rb");
    if (!fp) {
        throw std::runtime_error("Failed to open file.");
    }

    const int BUFFER_SIZE = 1024;
    char buffer[BUFFER_SIZE];
    size_t bytes_read = fread(buffer, 1, BUFFER_SIZE, fp);
    fclose(fp);

    iconv_t cd_utf8 = iconv_open("UTF-8", "");
    if (cd_utf8 == (iconv_t)-1) {
        throw std::runtime_error("Failed to create UTF-8 converter.");
    }

    for (const char* encoding : {"CP1251", "KOI8-R", "ISO-8859-5"}) {
        iconv_t cd = iconv_open("UTF-8", encoding);
        if (cd != (iconv_t)-1) {
            char* inbuf = (char*)buffer;
            size_t inbytesleft = bytes_read;
            char outbuf[BUFFER_SIZE];
            char* outptr = outbuf;
            size_t outbytesleft = sizeof(outbuf);

            size_t result = iconv(cd, &inbuf, &inbytesleft, &outptr, &outbytesleft);
            if (result != (size_t)-1 && inbytesleft == 0) {
                iconv_close(cd);
                return encoding;
            }
            iconv_close(cd);
        }
    }

    iconv_close(cd_utf8);
    return "Unknown";
}


