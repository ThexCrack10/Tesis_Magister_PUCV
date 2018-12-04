from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
#from .utils import URLUtil
#VALORES MD CON API
from tablib import Dataset
from django.shortcuts import render
#API
from rest_framework import generics
from .models import *
from .serializers import *
from .resources import *
from django.shortcuts import get_object_or_404

# connect scrapyd service
scrapyd = ScrapydAPI('http://localhost:6800')


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)  # check if url format is valid
    except ValidationError:
        return False

    return True

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def crawl(request):
    # Post requests are for new crawling tasks
    if request.method == 'POST':

        url = request.POST.get('url', None)  # take url comes from client. (From an input may be?)

        if not url:
            return JsonResponse({'error': 'Missing  args'})

        if not is_valid_url(url):
            return JsonResponse({'error': 'URL is invalid'})

        domain = urlparse(url).netloc  # parse the url and extract the domain
        unique_id = str(uuid4())  # create a unique ID.

        # This is the custom settings for scrapy spider.
        # We can send anything we want to use it inside spiders and pipelines.
        # I mean, anything
        settings = {
            'unique_id': unique_id,  # unique ID for each record for DB
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }

        # Here we schedule a new crawling task from scrapyd.
        # Notice that settings is a special argument name.
        # But we can pass other arguments, though.
        # This returns a ID which belongs and will be belong to this task
        # We are goint to use that to check task's status.
        task = scrapyd.schedule('default', 'icrawler',
                                settings=settings, url=url, domain=domain)

        return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})

    # Get requests are for getting result of a specific crawling task
    elif request.method == 'GET':
        # We were passed these from past request above. Remember ?
        # They were trying to survive in client side.
        # Now they are here again, thankfully. <3
        # We passed them back to here to check the status of crawling
        # And if crawling is completed, we respond back with a crawled data.
        task_id = request.GET.get('task_id', None)
        unique_id = request.GET.get('unique_id', None)

        if not task_id or not unique_id:
            return JsonResponse({'error': 'Missing args'})

        # Here we check status of crawling that just started a few seconds ago.
        # If it is finished, we can query from database and get results
        # If it is not finished we can return active status
        # Possible results are -> pending, running, finished
        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                # this is the unique_id that we created even before crawling started.
                item = ScrapyItem.objects.get(unique_id=unique_id)
                return JsonResponse({'data': item.to_dict['data']})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'status': status})

class RubroList(generics.ListCreateAPIView):
        queryset = RubroComercio.objects.all()
        serializer_class = RubroSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class ComercioList(generics.ListCreateAPIView):
        queryset = Comercio.objects.all()
        serializer_class = ComercioSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class SucursalList(generics.ListCreateAPIView):
        queryset = Sucursal.objects.all()
        serializer_class = SucursalSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class PrecioList(generics.ListCreateAPIView):
        queryset = Precio.objects.all()
        serializer_class = PrecioSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class ProductoList(generics.ListCreateAPIView):
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class CategoriaProductoList(generics.ListCreateAPIView):
        queryset = CategoriaProducto.objects.all()
        serializer_class = CategoriaProductoSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class CategoriaList(generics.ListCreateAPIView):
        queryset = Categoria.objects.all()
        serializer_class = CategoriaSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class CaracteristicaProductoList(generics.ListCreateAPIView):
        queryset = CaracteristicaProducto.objects.all()
        serializer_class = CaracteristicaProductoSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class CaracteristicaList(generics.ListCreateAPIView):
        queryset = Caracteristica.objects.all()
        serializer_class = CaracteristicaSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class ValorMedidaList(generics.ListCreateAPIView):
        queryset = ValorMedida.objects.all()
        serializer_class = ValorMedidaSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class UnidadDeMedidaList(generics.ListCreateAPIView):
        queryset = UnidadDeMedida.objects.all()
        serializer_class = UnidadDeMedidaSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class CodigoProductoList(generics.ListCreateAPIView):
        queryset = CodigoProducto.objects.all()
        serializer_class = CodigoProductoSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

class TipoCodigoList(generics.ListCreateAPIView):
        queryset = TipoCodigo.objects.all()
        serializer_class = TipoCodigoSerializer
        def get_object(self):
                queryset = self.get_queryset()
                obj = get_object_or_404(
                        queryset,
                        pk = self.kwargs['pk'],
                )
                return obj

def simple_upload(request):
    if request.method == 'POST':
        producto_resource = ProductoResource()
        dataset = Dataset()
        new_products = request.FILES['myfile']

        result = producto_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            producto_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')