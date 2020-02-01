import graphene
import maintdx.assets.schema


class Query(
        maintdx.assets.schema.Query,
        graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)
