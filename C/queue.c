/**
 * Ciaran Sanders
 * 22 Nov, 2020
 * Queue implementation
 */

#include "queue.h"

int init_q(Queue *q, int size) {
  q->data = malloc(sizeof(void *) * size);
  if (q->data == NULL)
    return -1;

  for(int i = 0; i < size; i++)
    q->data[i] = malloc(sizeof(void *));

  q->head = 0;
  q->tail = -1;
  q->max_size = size;
  q->cur_size = 0;
  return 0;
}

int enqueue_q(Queue *q, void *data) {
  q->cur_size++;
  if (q->cur_size >= q->max_size){
    q->cur_size--;
    return -1;
  }
  
  fprintf(stderr, "%d\n", q->tail);
  q->tail = (q->tail + 1) % q->max_size;
  fprintf(stderr, "%d\n", q->tail);
  q->data[q->tail] = data;
  return 0;
}

void *dequeue_q(Queue *q) {
  if (q->cur_size > 0) {
    q->head = (q->head + 1) % q->max_size;
    q->cur_size--;
    return q->data[q->head];
  } else {
    return NULL;
  }
}

int free_q(Queue *q) {

}

void print_q(Queue *q) {

}
