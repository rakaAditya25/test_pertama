from urllib.request import urlopen 
import json 
from odoo import models,api,fields,_

class WizardFilterProduct(models.TransientModel):
    _name = 'wz.filter.product'
    _description = 'Filter Product By Category'

    type_category = fields.Selection([('product', 'Product'), ('category', 'Category')], required=True, default="product")

    def generate_product(self):
        product_template = self.env['product.template'].search([])
        product_category = self.env['product.category'].search([])
        distinct_pro = []
        if self.type_category == 'category':
            url = "https://dummyjson.com/products/categories"
            response = urlopen(url) 
            data_json = json.loads(response.read())
            for ct in data_json:
                if not product_category.filtered(lambda x: x.name == ct):
                    product_category.create({
                        'name': ct
                    })
        else:
            url = "https://dummyjson.com/products"
            response = urlopen(url) 
            data_json = json.loads(response.read())
            for rec in data_json["products"]:
                pc = product_category.filtered(lambda x: x.name == rec['category'])
                if pc:
                    product_template.create({
                        'name': rec['brand'],
                        'categ_id': pc.id
                    })
                else:
                    product_template.create({
                        'name': rec['brand'],
                        'categ_id': False
                    })