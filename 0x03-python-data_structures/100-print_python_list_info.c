#include <python3.10/Python.h>
void print_python_list_info(PyObject *p)
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
                object_type = Py_TYPE(PyList_GetItem(p, i));
                printf("Element %ld: %s\n", i, object_type->tp_name);
        }
}
