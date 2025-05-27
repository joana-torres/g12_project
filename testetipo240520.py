# -*- coding: utf-8 -*-
"""
Created on Sun May 25 22:32:04 2025

@author: kinaa
"""

import datetime 

class Produto:

    def __init__(self, id, descricao, preco_venda, preco_custo):
        self._id = str(id)                                   # Identificador do produto
        self._descricao = str(descricao)                     # Nome/Descrição do produto
        self._preco_venda = max(0.00, float(preco_venda))    # Preço de venda do produto
        self._preco_custo = max(0.00, float(preco_custo))    # Preço de custo do produto
        self._data_criacao = datetime.date.today()           # Data criação do produto

    @property
    def id(self):
        return self._id
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco_venda(self):
        return self._preco_venda
    @property
    def preco_custo(self):
        return self._preco_custo
    @property
    def data_criacao(self):
        return self._data_criacao
    
    def __str__(self):
        return "[%s] %s: PV %.2f; PC %.2f" % (self._id, self._descricao, self._preco_venda, self._preco_custo)
    
    @preco_venda.setter
    def preco_venda(self, preco_novo):
        self._preco_venda  = max(self._preco_custo, preco_novo)
    
    @preco_venda.setter
    def preco_custo(self, preco_novo):
        if preco_novo < self._preco_venda:
            self._preco_custo = preco_novo
            
    def margem(self):
        margem = (self._preco_venda - self._preco_custo) / self._preco_custo
        return margem
    
class ProdutoLote(Produto):
    def __init__(self, id, descricao, preco_venda, preco_custo, lotes=[]):
        super().__init__(id, descricao, preco_venda, preco_custo)
        self.lotes = lotes
        
    @property
    def lotes(self):
        return self.lotes
    
    @lotes.setter
    def lotes(self, lotes):
        self.lotes = lotes
    
    def addLote(self, data, quan, perc):
        dt = datetime.date.fromisoformat(data)
        k=0
        if len(self.lotes) == 0:
            lote = [dt, quan, perc]
            self.lotes.append(lote)
        else:
            for i in range(len(self.lotes)):
                lote = self.lotes[i]
                if lote[0] == dt:
                    qt_antiga = lote[1]
                    desc_antigo = lote[2]
                    k += 1
                    lote[1] += quan
                    lote[2] = (qt_antiga * desc_antigo + quan * perc)/(qt_antiga+quan)
            if k == 0:
                lote = [dt, quan, perc]
                self.lotes.append(lote)
        return self.lotes
        
iogurte = ProdutoLote("P250", "Iogurte Grego X", 2.25, 1.80)
iogurte.addLote('2024-06-30', 10, 0.00)
print("LOTES DISPONÍVEIS #1")
print("\n".join([f"{l[0]}, {l[1]} un, desconto {round(l[2], 3)}" for l in iogurte.lotes]))

iogurte.addLote('2024-06-15', 30, 0.25)
print("\nLOTES DISPONÍVEIS #2")
print("\n".join([f"{l[0]}, {l[1]} un, desconto {round(l[2], 3)}" for l in iogurte.lotes]))

iogurte.addLote('2024-06-15', 20, 0.10)
print("\nLOTES DISPONÍVEIS #3")
print("\n".join([f"{l[0]}, {l[1]} un, desconto {round(l[2], 3)}" for l in iogurte.lotes]))
                
                
                