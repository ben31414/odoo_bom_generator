# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp import exceptions

class bomGeneratorWizard(models.TransientModel):
	_name = 'bom_generator.wizard'
	product_id = fields.Many2one('product.template', String="Product")
	attributes = fields.Many2many('product.attribute', String="Attributes")
	start_date = fields.Date('Valid From:')
	bom_wizzard_line_ids = fields.Many2many('bom_generator.wizzard_line', String="BOM Products")


	def hasAllAttributeValues(self, productAttributeValues, lineAttributeValues):
		for lineAttributeValue in lineAttributeValues:
			if (lineAttributeValue not in productAttributeValues):
				return False
		return True

	def get_current_product(self):
		active_id = self._context.get('active_id', False)
		if active_id:
			return self.env['bomGeneratorWizard'].browse(active_id).product_id

	@api.multi
	def create_bom(self):
		self.ensure_one()
		if not(self.product_id):
			raise exceptions.ValidationError('No product chosen')
		product = self.product_id
		lines = self.bom_wizzard_line_ids
		bom_obj = self.env['mrp.bom']
		bom_line_obj = self.env['mrp.bom.line']
		for product_variant in product.product_variant_ids:
			bom_id = bom_obj.create({'name': product.name,
				'product_tmpl_id': product.id,
				'product_id': product_variant.id})

			for line in lines:
				if(self.hasAllAttributeValues(product_variant.attribute_value_ids, line.attribute_value_ids)):
					bom_line_obj.create({'bom_id': bom_id.id,'product_id': line.bom_product_id.id})
		return True

class bomGeneratorWizzardLine(models.TransientModel):
	_name = 'bom_generator.wizzard_line'
	bom_product_id = fields.Many2one('product.product', String="BOM Product")
	product_qty = fields.Float(default= 1, String = 'Product Quantity')
	attribute_value_ids = fields.Many2many('product.attribute.value', String="Attribute Value Conditions")







