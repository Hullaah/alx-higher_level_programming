#include <python3.10/Python.h>
#include <string.h>
void print_hex(unsigned char c)
{
	int power, c_copy = c;
	char rep;
        if (c == '\0')
        {
                printf("00");
                return;
        }
	for (power = 0x1; c_copy / 0x10; c_copy /= 0x10, power *= 0x10);
	while (power)
	{
		rep = (c / power) % 0x10;
		putchar((rep < 0xa) ?rep + '0' :rep + 'W');
		power /= 0x10;
	}
}
void print_python_bytes(PyObject *p)
{
        int loop;
        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
                printf("  [ERROR] Invalid Bytes Object\n");
        else
        {
                Py_ssize_t bytes_size = PyBytes_Size(p);
                char *byte_string = PyBytes_AsString(p);
                printf("  size: %ld\n", bytes_size);
                printf("  trying string: %s\n", byte_string);
                loop = (bytes_size > 10) ? 10 : bytes_size + 1;
                printf("  first %d bytes: ", loop);
                for (int i = 0; i < loop; i++)
                {
                        /*printf("%hx", byte_string[i]);*/
                        print_hex(byte_string[i]);
                        printf("%c",  (i == loop - 1) ? '\n' : ' ');
                }
        }

}

void print_python_list(PyObject *p)
{
        Py_ssize_t list_size, i;
        PyTypeObject *object_type;
        Py_ssize_t allocated;

        list_size = PyList_Size(p);
        allocated = ((PyListObject *)p)->allocated;
        printf("[*] Size of the Python List = %ld\n", list_size);
        printf("[*] Allocated = %ld\n", allocated);
        for (i = 0; i < list_size; i++)
        {
                PyObject *list_item = PyList_GET_ITEM(p, i);
                object_type = list_item->ob_type;
                printf("Element %ld: %s\n", i, object_type->tp_name);
                if (!strcmp(object_type->tp_name, "bytes"))
                        print_python_bytes(list_item);

        }
}
