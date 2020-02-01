import graphene
import maintdx.assets.schema
import maintdx.parts.schema

class Query(
        maintdx.assets.schema.Query,
        maintdx.parts.schema.Query,
        graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)
