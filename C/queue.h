/**
 * Ciaran Sanders
 * 22 Nov, 2020
 * Queue header file
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct {
  void **data;
  int head;
  int tail;
  int max_size;
  int cur_size;
} Queue;

int init_q(Queue *q, int size);
int enqueue_q(Queue *q, void *data);
void *dequeue_q(Queue *q);
int free_q(Queue *q);
void print_q(Queue *q);
 
