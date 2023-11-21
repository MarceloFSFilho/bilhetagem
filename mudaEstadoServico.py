#!/usr/bin/env python
# coding: utf-8

# In[113]:


def mudaEstadoServico(conteudo):
    
    for linha in conteudo:
        tipoRegistro = linha[:3]
        versaoRegistro = linha[3:6]
        codEmpresa = linha[6:9]
        numOnibus = linha[14:19]
        estServico = linha[19:22]
        data = linha[22:27]
        hora = linha[27:32]
        codEmpMotorista = linha[32:35]
        codMotProdata = linha[35:45]
        matricMotorista = linha[45:55]
        codEmpCobrador = linha[55:58]
        codProdCobrador = linha[58:68]
        matricCobrador = linha[68:78]
        codLinhaDetalhe = linha[78:82]
        codLinhaPrincipal = linha[82:88]
        codSecao = linha[88:91]
        sentido = linha[91:94]
        turno = linha[94:95]
        assinatura = linha[95:100]
    return mudaEstadoServico()


# In[ ]:





# In[ ]:




