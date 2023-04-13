from marshmallow import fields, Schema

from schemas.base_movie import BaseMovieSchema


class MovieSchemaOut(BaseMovieSchema):
    id = fields.Integer(required=True)


class GenreSchema(Schema):
    name = fields.String(required=True)


class ProductionCompaniesSchema(Schema):
    name = fields.String(required=True)
    origin_country = fields.String(required=True)


class TMDBSearchSchemaOut(Schema):
    budget = fields.Integer(required=True)
    overview = fields.String(required=True)
    revenue = fields.Float(required=True)
    tagline = fields.String(required=True)
    status = fields.String(required=True)
    release_date = fields.String(required=True)
    homepage = fields.String(required=True)
    genres = fields.Nested(GenreSchema, many=True)
    production_companies = fields.Nested(ProductionCompaniesSchema, many=True)


class TMDBResultSchemaOut(Schema):
    original_title = fields.String(required=True)
    overview = fields.String(required=True)
    release_date = fields.String(required=True)


class TMDBUpcomingSchemaOut(Schema):
    results = fields.List(fields.Nested(TMDBResultSchemaOut), required=True)
