/** 
 * Ciaran Sanders
 * 22 Nov, 2020
 * test file for queue
 */
#include <stdio.h>
#include "queue.h"


int main(int argc, char **argv) {
  Queue queue;
  if (init_q(&queue, 30))
    return -1;
  char *a = "a";
  char *b = "b";
  char *c = "c";
  char *d = "d";
  char *e = "e";

  enqueue_q(&queue, a);
  enqueue_q(&queue, b);
  enqueue_q(&queue, c);
  void *data;
  while(data = dequeue_q(&queue))
    printf("%s\n", "nice");

  for(int i = 0; i < 35; i++) {
    if(enqueue_q(&queue,a)) {
      printf("bad\n");
    } else {
      printf("good\n");
    }
  }
  printf("success!\n");
}
