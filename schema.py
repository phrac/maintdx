import graphene
import maintdx.assets.schema
import maintdx.parts.schema
import maintdx.vendors.schema
import maintdx.workorders.schema

class Query(
        maintdx.assets.schema.Query,
        maintdx.parts.schema.Query,
        maintdx.vendors.schema.Query,
        maintdx.workorders.schema.Query,
        graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)
