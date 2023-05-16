/**
 * File: 13-is_palindrome.c
 * Author: Olorundamisi Dunmade <github.com/olorundamisi>
 */


#include "lists.h"


int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **head);


/**
 * is_palindrome - Check if a singly-linked list is a palindrome.
 * @head: Pointer to the head node of the singly-linked list.
 *
 * Return: 0 - If the list is not a palindrome.
 *         1 - If the list is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	listint_t *rev;

	size_t len, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	len = 0;
	tmp = *head;
	while (tmp)
	{
		len++;
		tmp = tmp->next; }

	tmp = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		tmp = tmp->next;

	if ((len % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next; }

	return (1);
}


/**
 * reverse_listint - Reverse a singly-linked list.
 * @head: Pointer to the head/starting node of the linked list to reverse.
 *
 * Return: Pointer to the head node of the reversed linked list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *next;
	listint_t *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}
