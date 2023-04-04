from django.test import TestCase

from product.models import Category, Product, ProductGallery


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category', slug='test-category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_slug_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_slug_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('slug').max_length
        self.assertEqual(max_length, 100)

    def test_unique_slug(self):
        category1 = Category.objects.get(id=1)
        Category.objects.create(name='Test Category 2', slug='test-category-2')
        category2 = Category.objects.get(id=2)
        self.assertNotEqual(category1.slug, category2.slug)

    def test_object_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.name
        self.assertEqual(str(category), expected_object_name)

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        url = f'/{category.slug}/'
        self.assertEqual(category.get_absolute_url(), url)


class ProductTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category',
                                                slug='test-category')
        self.product1 = Product.objects.create(category=self.category,
                                               name='Product 1',
                                               slug='product-1',
                                               description='This is Product 1',
                                               price=10.99)
        self.product2 = Product.objects.create(category=self.category,
                                               name='Product 2',
                                               slug='product-2',
                                               description='This is Product 2',
                                               price=20.99)

    def test_product_str(self):
        self.assertEqual(str(self.product1), 'Product 1')
        self.assertEqual(str(self.product2), 'Product 2')

    # def test_product_absolute_url(self):
    #     self.assertEqual(self.product1.get_absolute_url(),
    #                      '/test-category/product-1/')
    #     self.assertEqual(self.product2.get_absolute_url(),
    #                      '/test-category/product-2/')

    def test_product_get_image(self):
        self.assertIsNone(self.product1.get_image())
        self.assertIsNone(self.product2.get_image())

        self.product1.image = 'test.jpg'
        self.product1.save()
        self.assertEqual(self.product1.get_image(),
                         'http://127.0.0.1:8000/store/products/test.jpg')

        self.product2.image = 'test.png'
        self.product2.save()
        self.assertEqual(self.product2.get_image(),
                         'http://127.0.0.1:8000/store/products/test.png')


# class ProductGalleryModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         product = Product.objects.create(name='Product1')
#         ProductGallery.objects.create(image='store/gallery/image1.jpg',
#                                       product=product)

#     def test_image_label(self):
#         product_gallery = ProductGallery.objects.get(id=1)
#         field_label = product_gallery._meta.get_field('image').verbose_name
#         self.assertEquals(field_label, 'image')

#     def test_product_label(self):
#         product_gallery = ProductGallery.objects.get(id=1)
#         field_label = product_gallery._meta.get_field('product').verbose_name
#         self.assertEquals(field_label, 'product')

#     def test_image_upload_to(self):
#         product_gallery = ProductGallery.objects.get(id=1)
#         upload_to = 'store/gallery/'
#         self.assertEquals(product_gallery.image.field.upload_to, upload_to)

#     def test_object_name_is_product_name(self):
#         product_gallery = ProductGallery.objects.get(id=1)
#         expected_object_name = f'{product_gallery.product.name}'
#         self.assertEquals(expected_object_name, str(product_gallery))

#     def test_verbose_name_plural(self):
#         self.assertEquals(str(ProductGallery._meta.verbose_name_plural),
#                           'Product Gallery')
