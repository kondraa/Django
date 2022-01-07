from django.shortcuts import render
import os, json

# Create your views here.
MODULE_DIR = os.path.dirname(__file__)


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
    context = {
        'title': 'geekshop',
        'products' : json.load(open(file_path, encoding='utf-8'))
        # 'products': [{'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6090.00',
        #               'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #               'img': 'vendor/img/products/Adidas-hoodie.png'},
        #              {'name': 'Синяя куртка The North Face', 'price': '23725.00',
        #               'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
        #               'img': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
        #              {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3390.00',
        #               'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
        #               'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
        #              {'name': 'Черный рюкзак Nike Heritage', 'price': '2340.00',
        #               'description': 'Плотная ткань. Легкий материал.',
        #               'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
        #              {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13590.00',
        #               'description': 'Гладкий кожаный верх. Натуральный материал.',
        #               'img': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
        #              {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2890.00',
        #               'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
        #               'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        #              ]
    }
    return render(request, 'mainapp/products.html', context)