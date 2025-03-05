// File: cprog.c
#include <stdio.h>

struct WinRect {
 int x, y, w, h;
 char *descr;
};

struct WinRect data[] = {
 { 10, 5, 5, 5, "menu" },
 { 0,0, 200, 20, "titlebar" }, 
 { 50, 30, 15, 5, "end button" }, 
};

int main() {
 int tx = 60; // test-x
 int ty = 32;  // test-y

 int nelems = sizeof(data) / sizeof(struct WinRect);
 for (int idx = 0; idx < nelems; idx++) {
  int dx = tx - data[idx].x;
  int dy = ty - data[idx].y;

  if ((dx < 0) || (dx >= data[idx].w)) continue;
  if ((dy < 0) || (dy >= data[idx].h)) continue;
  printf("test point (%d,%d) inside rect '%s'\n", 
	tx, ty, data[idx].descr);
 }
 return 0;
}
