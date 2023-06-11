#include "lists.h"
#include <stdio.h>
/**
 * list_length - calculates the length of a linked list
 * @head: ptr to list head
 * Return: list length
*/
int list_length(listint_t *head)
{
	listint_t *ptr = head;
	int i = 0;

	while (ptr)
	{
		ptr = ptr->next;
		i++;
	}
	return (i);
}
/**
 * get_node - gets the value stored in a node of a linked list
 * @head: head of node
 * @idx: index of node whose value is to be got
 * Return: value stored in node specified by index idx
*/
int get_node(int idx, listint_t *head)
{
	int i = 0, length;
	listint_t *ptr = head;

	length = list_length(head);
	if (idx >= length || idx < 0)
	{
		printf("invalid index\n");
		exit(2);
	}
	while (i < length)
	{
		if (i == idx)
			break;
		i++;
		ptr = ptr->next;
	}
	return (ptr->n);
}
/**
 * is_palindrome_base - serves as the base algorithm for the is_palindrome
 * function
 * @head: head of linked list
 * @next: next field of linked list starting from head
 * @last_idx: last index of linked list
 * @half_length: middle index
 * Return: 1 if list is palindrome, 0 otherwise
 * Description: on first call head stores the same value as next so that
 * when the get_node function is called recursively on a next node, it
 * won't return the same value. So next gets updated while head doesn't
*/
int is_palindrome_base(
	listint_t *head, listint_t *next, int last_idx, int half_length)
{
	int n_last = get_node(last_idx, head);

	if (last_idx == half_length)
		return ((n_last == next->n) ? 1 : 0);
	else
		return (
			n_last == next->n &&
			is_palindrome_base(head, next->next, last_idx - 1, half_length)
			);
}
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: list head
 * Return: 1 if list is palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	int node_length = list_length(*head), half_length, last_idx;

	last_idx = node_length - 1;
	half_length = node_length % 2 ? node_length / 2 : node_length / 2 - 1;

	return (is_palindrome_base(*head, *head, last_idx, half_length));
}
