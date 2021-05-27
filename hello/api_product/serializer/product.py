from rest_framework import serializers

from webapp.models import Product, OrderProduct, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price')
        read_only_fields = ('id',)

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'quantity')
        read_only_fields = ('id',)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'user', 'name_user', 'telephone', 'adress', 'date_time')
        read_only_fields = ('id', 'order')


    def create(self, validated_data):
        print(validated_data)
        order = Order.objects.create(user=validated_data['user'],
                                     name=validated_data['name_user'],
                                     adress=validated_data['adress'],
                                     phonenumber=validated_data['telephone'])
        for products in validated_data['order_product']:
            order_product = OrderProduct.objects.create(order=order, product=products['product'], quantity=products['quantity'])
            print(order_product)
        return validated_data




