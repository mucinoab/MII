from django.shortcuts import render


# x, y, z, t = sympy.symbols('x y z t')

def punto_view(request):
    # form = In()
    # context = {"form": form}
    #
    # if request.method == 'GET':
    #     form = In(request.GET)
    #     if form.is_valid():
    #         return newton_calcula(request, form)

    return render(request, "fijo_elejir.html")
