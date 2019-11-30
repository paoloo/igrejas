import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import *

class Igrejas(SQLAlchemyObjectType):
    class Meta:
        model = IgrejasModel
        interfaces = (graphene.relay.Node, )

class Socios(SQLAlchemyObjectType):
    class Meta:
        model = SociosModel
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    igreja = graphene.List(Igrejas,
                           cnpj = graphene.String(),
                           matrizFilial = graphene.Int(),
                           uf = graphene.String(),
                           municipio = graphene.String(),
                           bairro = graphene.String(),
                           razaoSocial = graphene.String(),
                           nomeCidadeExterior = graphene.String()
    )

    def resolve_igreja(self, info, cnpj=None, matrizFilial=None, uf=None, municipio=None, bairro=None, razaoSocial=None, nomeCidadeExterior=None, **kwargs):
        query = Igrejas.get_query(info)
        if cnpj:
            query = query.filter(IgrejasModel.cnpj == cnpj)
        if razaoSocial:
            query = query.filter(IgrejasModel.razaoSocial.like('%{}%'.format(razaoSocial)))
        if matrizFilial:
            query = query.filter(IgrejasModel.matrizFilial == matrizFilial)
        if uf:
            query = query.filter(IgrejasModel.uf == uf)
        if municipio:
            query = query.filter(IgrejasModel.municipio == municipio)
        if bairro:
            query = query.filter(IgrejasModel.bairro == bairro)
        if nomeCidadeExterior:
            query = query.filter(IgrejasModel.nomeCidadeExterior == nomeCidadeExterior)
        return query.all()

schema = graphene.Schema(query=Query)
