#ifndef APPSETTING_H
#define APPSETTING_H




// APP SETTINGS
const int MENU_STANDARD   = 60;
const int MENU_WIDTH      = 240;

const int LEFT_BOX_MIN    = 0;
const int LEFT_BOX_WIDTH  = 345;

const int RIGHT_BOX_MIN   = 0;
const int RIGHT_BOX_WIDTH = 240;

const int TIME_ANIMATION  = 250;

// BTNS LEFT AND RIGHT BOX COLORS
char BTN_LEFT_BOX_COLOR[] = "background-color: #00ADEE;";
char BTN_RIGHT_BOX_COLOR[] = "background-color: #00ADEE;";

// MENU SELECTED STYLESHEET
char MENU_SELECTED_STYLESHEET[] = "border-left: 22px solid \
    qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 #00ADEE, \
    stop:0.5 rgba(85, 170, 255, 0)); background-color: #9DCEEC;";
#endif // APPSETTING_H
